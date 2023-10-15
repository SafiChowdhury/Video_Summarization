from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter.ttk import Treeview
from tkinter import ttk
import tkinter as tk

# Define the global variable
global logged_in_username


def initialize_home(logged_in_username):
    homepage = Tk()
    homepage.title('Recap')
    homepage.geometry('925x500+300+200')
    homepage.configure(bg="#fff")
    homepage.resizable(False, False)
    img = PhotoImage(file='home1.png')
    image_label = Label(homepage, image=img, bg='white')
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    custom_icon = PhotoImage(file='home2.png')
    homepage.tk_setPalette(background='#fff', foreground='#000',
                           activeBackground='#57a1f8', activeForeground='white')
    homepage.iconphoto(True, custom_icon)

    def fetch_and_display_info():
        option = selected_option.get()
        display_data_in_table(option)

    selected_option = StringVar()
    selected_option.set("Fetch Uploaded Videos")  # Default selected option
    options_menu = OptionMenu(homepage, selected_option, "Fetch Uploaded Videos", "Fetch Summarized Videos",
                              "Fetch Detected Objects")
    options_menu.config(width=23, height=1)
    options_menu.place(x=30, y=50)
    # Create a themed style for the rounded edge button
    style1 = ttk.Style()
    style1.configure('Rounded.TButton', borderwidth=0,
                     relief="flat", background="#57a1f8", foreground="black")

    # Create a rounded edge button
    fetch_button = ttk.Button(
        homepage, text="Fetch", style='Rounded.TButton', command=fetch_and_display_info)
    fetch_button.place(x=235, y=53)

    def display_data_in_table(option):
        # Create a Treeview widget to display the data
        data_tree = Treeview(homepage, columns=(
            "File Name", "Date Time"), show="headings", height=17)
        data_tree.heading("File Name", text="File Name")
        # data_tree.heading("File Path", text="File Path")
        data_tree.heading("Date Time", text="Date Time")
        data_tree.place(x=30, y=100)

        # Display data based on the selected option
        data_tree.delete(*data_tree.get_children())  # Clear previous data
        try:
            con = pymysql.connect(
                host='localhost', user='root', password='', database='userdata')
            cursor = con.cursor()
            if option == "Fetch Uploaded Videos":
                query = 'SELECT file_name,  date_time FROM uploadvideo WHERE username = %s'
            elif option == "Fetch Summarized Videos":
                query = 'SELECT file_name,  date_time FROM summarizedvideo WHERE username = %s'
            elif option == "Fetch Detected Objects":
                query = 'SELECT file_name,  date_time FROM detectobject WHERE username = %s'
            cursor.execute(query, (logged_in_username,))
            data = cursor.fetchall()
            if not data:
                messagebox.showwarning("Info", f'No {option} found.')
            else:
                for row in data:
                    data_tree.insert("", "end", values=row)
        except pymysql.Error as e:
            messagebox.showerror('Error', f'Error fetching data: {str(e)}')

    Label(homepage, text=f'welcome {logged_in_username}!', bg='#bee5e0',
          font=("Times", "20", "bold italic")).place(x=25, y=10)

    def summarize_videos():
        homepage.destroy()
        import summarize
        summarize.summarize(logged_in_username)

    def detect_objects():
        homepage.destroy()
        import object_detect
        object_detect.summarize(logged_in_username)

    def logout():
        homepage.destroy()
        import signin

    context_menu = tk.Menu(homepage, tearoff=0)

    # Add options to the context menu
    context_menu.add_command(label="Logout", command=logout)

    # Configure the context menu to be always visible
    homepage.config(menu=context_menu)
    # Create a themed style for the rounded button
    style = ttk.Style()
    style.configure('Rounded.TButton', borderwidth=0,
                    relief="flat", background="#ededed")

    # Create a rounded button
    summarize_button = ttk.Button(
        homepage, text='Summarizer', style='Rounded.TButton', command=summarize_videos)
    summarize_button.place(x=655, y=174.5)

    # Button to perform object detection
    detect_button = ttk.Button(
        homepage, text='Detect Objects', style='Rounded.TButton', command=detect_objects)
    detect_button.place(x=652.4, y=439.8)

    homepage.mainloop()
