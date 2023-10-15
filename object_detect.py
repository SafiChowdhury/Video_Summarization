import threading
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.filedialog import askopenfile
from tkinter.ttk import Scale
import cv2
import numpy as np
from tkVideoPlayer import TkinterVideo
import time
import pymysql
from datetime import datetime
from tkinter import PhotoImage


# Global variables
global logged_in_username
video_capture = None
video_duration = 0
current_time = 0
is_playing = False
videoplayer = None
timer_window = None
timer_label = None
#global filename


def summarize(logged_in_username):
    def show_timer_window():
        global timer_window, timer_label
        # if timer_window:
        #     timer_window.destroy()
        timer_window = tk.Toplevel(window)
        timer_window.title("Processing")
        timer_window.geometry("300x100")
        timer_window.resizable(False, False)
        timer_label = tk.Label(
            timer_window, text="Video is Processing", font=("Times", 12))
        timer_label.pack(pady=20)
        countdown_timer(3)

    def countdown_timer(seconds):
        global timer_label
        if seconds > 0:
            timer_label.config(
                text="Video is Processing.Wait for confirmation!")
            timer_window.after(1000, lambda: countdown_timer(seconds - 1))
        else:
            selected = selected_option.get()
            upload_file()
            timer_window.destroy()

    # Function to initialize videoplayer
    def initialize_videoplayer():
        global videoplayer
        # if videoplayer:
        #     videoplayer.destroy()
        videoplayer = TkinterVideo(master=window, scaled=True)

    # Function to open a video file
    import os

    def open_file():
        global filename, video_capture, video_duration, is_playing, current_time
        file = askopenfile(mode='r', filetypes=[('Video Files', ['*.mp4'])])
        if file:
            full_path = file.name
            # Extract the filename from the full path
            filename = os.path.basename(full_path)
            if video_capture:
                video_capture.release()  # Release previous video capture if it exists
            video_capture = cv2.VideoCapture(full_path)
            video_duration = int(video_capture.get(
                cv2.CAP_PROP_FRAME_COUNT) / video_capture.get(cv2.CAP_PROP_FPS))
            is_playing = True
            current_time = 0

            initialize_videoplayer()  # Initialize or reinitialize the videoplayer
            videoplayer.load(full_path)
            videoplayer.pack(expand=True, fill="both")
            videoplayer.play()

            # Configure the timeline slider
            timeline_slider.config(from_=0, to=video_duration)
            timeline_slider.set(0)

            # Update the duration label
            duration_label.config(
                text=f"Duration: {format_time(video_duration)}")
            try:
                con = pymysql.connect(
                    host='localhost', user='root', password='', database='userdata')
                cursor = con.cursor()
                current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                insert_query = "INSERT INTO uploadvideo (username , file_name, file_path, date_time) VALUES (%s, %s, %s ,%s)"
                cursor.execute(insert_query, (logged_in_username,
                               filename, full_path, current_datetime))
                con.commit()
                con.close()
                print("Video information inserted into the database.")
            except pymysql.Error as e:
                print(
                    f"Error inserting video information into the database: {str(e)}")
            # Start video playback
            play_video()

    # Function to play the video
    def play_video():
        global is_playing
        is_playing = True
        videoplayer.play()
        update_current_time()

    # Function to pause the video
    def pause_video():
        global is_playing
        is_playing = False
        videoplayer.pause()

    # Function to update the current time and timeline slider
    def update_current_time():
        global current_time, is_playing
        if is_playing and current_time < video_duration:
            ret, _ = video_capture.read()
            if ret:
                current_time += 1
                timeline_slider.set(current_time)
                current_time_label.config(
                    text=f"Current Time: {format_time(current_time)}")
                window.after(1000, update_current_time)
            else:
                is_playing = False

    # Function to format time as "mm:ss"
    def format_time(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    # Function to seek the video to the specified time
    def seek_video(value):
        global current_time
        current_time = int(value)
        if is_playing:
            # Seek the video to the specified time
            videoplayer.seek(current_time)
            current_time_label.config(
                text=f"Current Time: {format_time(current_time)}")

    def upload_file():
        global filename
        selected = selected_option.get()

        video = cv2.VideoCapture(filename)
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        threshold = 20.

        original_filename = filename.split('/')[-1].split('.')[0]

        output_filename = f"{original_filename}_objDect_{selected}.mp4"

        writer = cv2.VideoWriter(
            output_filename, cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))
        ret, frame1 = video.read()
        prev_frame = frame1

        a = 0
        b = 0
        c = 0

        protopath = 'MobileNetSSD_deploy.prototxt'
        modelpath = 'MobileNetSSD_deploy.caffemodel'

        detector = cv2.dnn.readNetFromCaffe(
            prototxt=protopath, caffeModel=modelpath)

        CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
                   "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
                   "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
                   "sofa", "train", "tvmonitor"]
        start_time = time.time()
        while True:
            ret, frame = video.read()
            if not ret:
                break
            (H, W) = frame.shape[:2]

            blob = cv2.dnn.blobFromImage(frame, 0.007843, (W, H), 127.5)

            detector.setInput(blob)
            person_detections = detector.forward()

            for i in np.arange(0, person_detections.shape[2]):
                confidence = person_detections[0, 0, i, 2]
                if confidence > 0.5:
                    idx = int(person_detections[0, 0, i, 1])

                    if CLASSES[idx] != selected:
                        continue

                    person_box = person_detections[0, 0,
                                                   i, 3:7] * np.array([W, H, W, H])
                    (startX, startY, endX, endY) = person_box.astype("int")

                    cv2.rectangle(frame, (startX, startY),
                                  (endX, endY), (0, 0, 255), 2)

                    if (((np.sum(np.absolute(frame - prev_frame)) / np.size(frame)) > threshold)):
                        writer.write(frame)
                        prev_frame = frame
                        a += 1
                    else:
                        prev_frame = frame
                        b += 1

            c += 1

            if time.time() - start_time >= 60:
                break
            # if ret is False:
            #     break
        try:
            con = pymysql.connect(
                host='localhost', user='root', password='', database='userdata')
            cursor = con.cursor()
            current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Insert summarized video information into the database
            # Change this to the actual output video file path
            #output_filepath = f'Z:/soft/final/{output_filename}'
            output_filepath = f'C:/Users/Lab4PC/Desktop/VideoSumm/{output_filename}'

            insert_query = "INSERT INTO detectobject (username,file_name, file_path, date_time) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (logged_in_username,
                           output_filename, output_filepath, current_datetime))
            con.commit()
            con.close()
            print("Video information inserted into the database.")
        except pymysql.Error as e:
            print(
                f"Error inserting video information into the database: {str(e)}")
        print("Total frames: ", c)
        print("Unique frames: ", a)
        print("Common frames: ", b)
        video.release()
        writer.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Done!", "Click OK to show result")
        window.destroy()
        import objdet_output
        objdet_output.result_video(logged_in_username)

    def start_timer_and_upload():
        timer_thread = threading.Thread(target=show_timer_window)
        timer_thread.start()

    def go_home():
        window.destroy()
        import home
        home.initialize_home(logged_in_username)

    def go_back():
        window.destroy()
        import home
        home.initialize_home(logged_in_username)

    def logout():
        window.destroy()
        import signin

    def on_object_selected(event):
        selected_option.set(event)

    # Create the main window
    window = tk.Tk()
    window.title("Recap")
    window.geometry('925x550+300+200')
    window.configure(bg='#fff')
    window.resizable(False, False)
    img = PhotoImage(file='home10.png')
    image_label = tk.Label(window, image=img, bg='white')
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    selected_option = tk.StringVar()
    custom_icon = PhotoImage(file='home2.png')

    # Set the custom icon
    window.tk_setPalette(background='#fff', foreground='#000',
                         activeBackground='#57a1f8', activeForeground='white')
    window.iconphoto(True, custom_icon)
    # Create and configure widgets
    style = ttk.Style()
    style.configure('Rounded.TButton', borderwidth=0,
                    relief="flat", background="#ededed")

    open_button = ttk.Button(window, text='Choose File',
                             style='Rounded.TButton', command=open_file)
    open_button.pack(side=tk.TOP, pady=2)

    object_detection_options = ["objects", "person", "table", "cat", "dog"]

    # Variable to store the selected option
    selected_option = tk.StringVar()
    selected_option.set(object_detection_options[0])

    # Create the OptionMenu
    object_dropdown = ttk.OptionMenu(
        window, selected_option, *object_detection_options)
    object_dropdown['style'] = 'Rounded.TButton'
    object_dropdown.pack(side=tk.TOP, padx=6)

    # Bind the function to the OptionMenu to handle the selection
    object_dropdown.bind(
        "<Configure>", lambda event: on_object_selected(selected_option.get()))

    # object_detection_options = ["Person", "Table", "Cat", "Dog"]
    # object_dropdown = ttk.OptionMenu(window, selected_option, style='Rounded.TButton', *object_detection_options)
    # object_dropdown.pack(side=tk.TOP, padx=6)
    #object_dropdown.config(width=15, height=1)
    duration_label = tk.Label(window, text="Duration: 0:00", bg='#ffd0be')
    current_time_label = tk.Label(
        window, text="Current Time: 0:00", bg='#ffd0be')

    context_menu = tk.Menu(window, tearoff=0)

    # Add options to the context menu
    context_menu.add_command(label="Home", command=go_home)
    context_menu.add_command(label="Back", command=go_back)
    context_menu.add_command(label="Logout", command=logout)

    # Configure the context menu to be always visible
    window.config(menu=context_menu)

    # Use pack manager for labels
    current_time_label.pack(side=tk.LEFT, anchor="sw")
    duration_label.pack(side=tk.RIGHT, anchor="se")

    timeline_slider = Scale(window, from_=0, to=0,
                            orient=tk.HORIZONTAL, length=700)
    timeline_slider.pack(side=tk.BOTTOM)

    # Create a frame for the Play and Pause buttons
    button_frame = tk.Frame(window, bg='#ffd0be')
    button_frame.pack(side=tk.BOTTOM)

    # Place Play and Pause buttons in the button frame
    play_button = ttk.Button(button_frame, text="Play",
                             style='Rounded.TButton', command=play_video)
    play_button.pack(side=tk.LEFT, padx=5, pady=5)

    uploadbtn = ttk.Button(button_frame, text='Detect Object',
                           style='Rounded.TButton', command=start_timer_and_upload)
    uploadbtn.pack(side=tk.LEFT, padx=5, pady=5)

    pause_button = ttk.Button(
        button_frame, text="Pause", style='Rounded.TButton', command=pause_video)
    pause_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Configure the timeline slider
    timeline_slider.config(from_=0, to=video_duration)
    timeline_slider.set(0)
    timeline_slider.bind("<ButtonRelease-1>",
                         lambda event: seek_video(timeline_slider.get()))  # Bind to slider value change event

    # Start the main loop

    window.mainloop()
