import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

from tkinter import filedialog
import shutil
import pymysql
from tkVideoPlayer import TkinterVideo
global filename
global logged_in_username


def result_video(logged_in_username):
    def play_video():
        videoplayer.play()

    def pause_video():
        videoplayer.pause()

    def download_file():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
        if file_path:
            # Get the video file path from the database
            video_file_path = get_last_video_for_user(logged_in_username)
            if video_file_path:
                # Copy the video file to the selected location
                shutil.copy(video_file_path, file_path)
        messagebox.showinfo("Downloaded successfully!", "Thank you for using Recap.")
        window.destroy()
        import home
        home.initialize_home(logged_in_username)

    def get_last_video_for_user(username):
        try:
            con = pymysql.connect(
                host='localhost', user='root', password='', database='userdata')
            cursor = con.cursor()
            query = "SELECT file_path FROM detectobject WHERE username = %s ORDER BY date_time DESC LIMIT 1"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            if result:
                return result[0]  # Return the file path
        except pymysql.Error as e:
            print(f"Error: {str(e)}")
        finally:
            con.close()

    def go_home():
        window.destroy()
        import home
        home.initialize_home(logged_in_username)

    def go_back():
        window.destroy()
        import object_detect
        object_detect.summarize(logged_in_username)

    def logout():
        window.destroy()
        import signin

    window = tk.Tk()
    window.title("Recap")
    window.geometry('925x550+300+200')
    window.configure(bg='#fff')
    window.resizable(False, False)
    img = PhotoImage(file='home10.png')
    image_label = Label(window, image=img, bg='white')
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    custom_icon = PhotoImage(file='home2.png')
    window.tk_setPalette(background='#fff', foreground='#000',
                         activeBackground='#57a1f8', activeForeground='white')
    window.iconphoto(True, custom_icon)
    style = ttk.Style()
    style.configure('Rounded.TButton', borderwidth=0,
                    relief="flat", background="#ededed")

    # Create and configure widgets
    label = ttk.Label(window, text='Here is your result!',
                      style='Rounded.TButton')
    label.pack(side="top", anchor="center")

    player_window = tk.Frame(window, width=750, height=450,
                             highlightbackground="black", highlightthickness=3)
    player_window.pack_propagate(False)
    player_window.pack(side=tk.TOP)

    video_path = get_last_video_for_user(logged_in_username)

    # if video_path:
    videoplayer = TkinterVideo(master=player_window, scaled=True)
    videoplayer.load(video_path)
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play()

    # Create a frame for the Play and Pause buttons
    button_frame = tk.Frame(window, bg='#ffd0be')
    button_frame.pack(side=tk.BOTTOM)

    style = ttk.Style()
    style.configure('Rounded.TButton', borderwidth=0,
                    relief="flat", background="#ededed")

    context_menu = tk.Menu(window, tearoff=0)

    # Add options to the context menu
    context_menu.add_command(label="Home", command=go_home)
    context_menu.add_command(label="Back", command=go_back)
    context_menu.add_command(label="Logout", command=logout)

    # Configure the context menu to be always visible
    window.config(menu=context_menu)

    # Place Play and Pause buttons in the button frame
    play_button = ttk.Button(button_frame, text="Play",
                             style="Rounded.TButton", command=play_video)
    play_button.pack(side=tk.LEFT, padx=5, pady=20)

    uploadbtn = ttk.Button(button_frame, text='Save File',
                           style="Rounded.TButton", command=download_file)
    uploadbtn.pack(side=tk.LEFT, padx=5, pady=20)

    pause_button = ttk.Button(
        button_frame, text="Pause", style="Rounded.TButton", command=pause_video)
    pause_button.pack(side=tk.LEFT, padx=5, pady=20)

    # Configure the timeline slider

    # Start the main loop
    window.mainloop()
