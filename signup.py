from tkinter import *
from tkinter import messagebox
import pymysql

global logged_in_username

window = Tk()
window.title("Recap")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)
custom_icon = PhotoImage(file='home2.png')
window.tk_setPalette(background='#fff', foreground='#000',
                     activeBackground='#57a1f8', activeForeground='white')
window.iconphoto(True, custom_icon)


# Set the custom icon


def clear():
    user.delete(0, END)
    code.delete(0, END)
    confirm_code.delete(0, END)


def signin():
    window.destroy()
    import signin


def connect_database():
    if user.get() == '' or code.get() == '' or confirm_code.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif code.get() != confirm_code.get():
        messagebox.showerror('Error', 'Password Does not Match')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='')
            my_cursor = con.cursor()
        except:
            messagebox.showerror(
                'Error', 'Database Connection Issue, Please Try Again')
            return
        try:

            query = 'create database userdata'
            my_cursor.execute(query)

            query = 'use userdata'
            my_cursor.execute(query)

            query = 'create table data(id int auto_increment primary key not null, username varchar(50),password varhcar(50))'
            my_cursor.execute(query)
        except:
            my_cursor.execute('use userdata')

        query = 'insert into data(username , password) values(%s ,%s)'
        my_cursor.execute(query, (user.get(), code.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success', 'Registration is Successfull')
        window.destroy()
        import signin



img = PhotoImage(file='signup.png')
Label(window, image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(window, width=350, height=390, bg='#fff')
frame.place(x=480, y=50)

heading = Label(frame, text='Sign Up', fg='#57a1f8', bg='white',
                font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


##################------------#####################


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


################------------------##################


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


################------------------##################


def on_enter(e, confirm_code):
    confirm_code.delete(0, 'end')
    confirm_code.config(show='*')


def on_leave(e, confirm_code):
    if confirm_code.get() == '':
        confirm_code.insert(0, 'Confirm password')
        confirm_code.config(show='')


confirm_code = Entry(frame, width=25, fg='black', border=0,
                     bg="white", font=('Microsoft Yahei UI Light', 11))
confirm_code.place(x=30, y=220)
confirm_code.insert(0, 'Confirm password')
confirm_code.config(show='')
confirm_code.bind('<FocusIn>', lambda e: on_enter(e, confirm_code))
confirm_code.bind('<FocusOut>', lambda e: on_leave(e, confirm_code))
Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

###----------------------------

Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8',
       fg='white', border=0, command=connect_database).place(x=35, y=280)
label = Label(frame, text="I have an account.", fg='black',
              bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=90, y=340)

signin = Button(frame, width=6, text='Sign in', border=0,
                bg='white', cursor='hand2', fg='#57a1f8', command=signin)
signin.place(x=200, y=340)
window.mainloop()
