from tkinter import *

global timer_label

window = Tk()
window.title("Recap")
window.geometry('925x550+300+200')
window.configure(bg='#fff')
window.resizable(False, False)
img = PhotoImage(file='promo.png')
image_label = Label(window, image=img, bg='white')
image_label.place(x=0, y=0, relwidth=1, relheight=1)
custom_icon = PhotoImage(file='home2.png')
window.tk_setPalette(background='#fff', foreground='#000',
                     activeBackground='#57a1f8', activeForeground='white')
window.iconphoto(True, custom_icon)


def countdown_timer(seconds):
    global timer_label
    if seconds > 0:
        window.after(1000, lambda: countdown_timer(seconds - 1))
    else:
        window.destroy()
        import login


countdown_timer(3)
window.mainloop()
