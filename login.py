from tkinter import *
from tkinter import messagebox
import pymysql

global logged_in_username


root = Tk()
root.title('Recap')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)
custom_icon = PhotoImage(file='home2.png')

# Set the custom icon
root.tk_setPalette(background='#fff', foreground='#000',
                   activeBackground='#57a1f8', activeForeground='white')
root.iconphoto(True, custom_icon)


def signin():
    global logged_in_username
    if user.get() == '' or code.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='')
            my_cursor = con.cursor()
        except:
            messagebox.showerror(
                'Error', 'Database Connection Issue, Please Try Again')
            return
        query = 'use userdata'
        my_cursor.execute(query)

        query = 'select * from data where username=%s and password=%s'
        my_cursor.execute(query, (user.get(), code.get()))

        row = my_cursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid Username or Password')
        else:
            logged_in_username = user.get()
            root.destroy()
            import home
            home.initialize_home(logged_in_username)


def signup_command():
    root.destroy()
    import signup


img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign In', fg='#57a1f8', bg='white',
                font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width=25, fg='black', border=0,
             bg="white", font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)


def on_enter(e, code):
    code.delete(0, 'end')
    code.config(show='*')


def on_leave(e, code):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')
        code.config(show='')


code = Entry(frame, width=25, fg='black', border=0,
             bg="white", font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.config(show='')
code.bind('<FocusIn>', lambda e: on_enter(e, code))
code.bind('<FocusOut>', lambda e: on_leave(e, code))
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)


Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8',
       fg='white', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black',
              bg='white', font=('Microsoft Yahei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign Up', border=0, bg='white',
                 cursor='hand2', fg='#57a1f8', command=signup_command)
sign_up.place(x=215, y=270)


root.mainloop()
