from tkinter import *
import os
import pyttsx3
import sqlite3

conn = sqlite3.connect('database1.db')
c = conn.cursor()
master = Tk()
global Id
global Pass

Id = StringVar()
Pass = StringVar()

master.title("log on ")
master.geometry("700x400+250+200")
master.iconbitmap("project images/icon.ico")
master.configure(background="powder blue")
master.resizable(FALSE, FALSE)
canvas = Canvas(master, height=400, width=700)
canvas.pack()
engine = pyttsx3.init()

volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-5000)

voices = engine.getProperty("voices")
engine.say("Hospital Management System ")
engine.runAndWait()

photo = PhotoImage(file="project images/imgg.png")
canvas.create_image(0, 0, image=photo, anchor=NW)



e1 = Entry(master,font=("arial", 13, "bold"), width=20, textvariable=Id,)
e1.place(x=440, y=183)
e2 = Entry(master, font=("arial", 13, "bold"), width=20, textvariable=Pass, show="*")
e2.place(x=440, y=236)


engine1 = pyttsx3.init()

volume = engine1.getProperty('volume')
engine1.setProperty('volume',volume+390)

rate = engine1.getProperty('rate')
engine1.setProperty('rate', rate-5000)

voices = engine1.getProperty("voices")
for voice in voices:
    engine1.setProperty("voice",voice.id)
engine1.say("Log In  ")
engine1.runAndWait()


def show():
    p1 = Entry(master, font=("arial", 13, "bold"), width=20, textvariable=Pass,)
    p1.place(x=440, y=236)


def hide():
    p2 = Entry(master, font=("arial", 13, "bold"), width=20, textvariable=Pass,show="*")
    p2.place(x=440, y=236)


def sign():
    master.destroy()
    os.system('python sigup.py')


def exit_():
    master.destroy()
    return


def logon():
    name = Id.get()
    password = Pass.get()
    sql = "SELECT * FROM LogIn WHERE Username=? AND password=? "
    execute = c.execute(sql, (name,password))
    for i in execute:
        print(i)
        master.destroy()
        engine1.say("Your Email And password Correct")
        engine1.runAndWait()
        engine.say("MAIN MENU OF HOSPITAL MANAGEMENT SYSTEM")
        engine.runAndWait()

        os.system('python menu.py')


b4 = Button(master, text="Show", font=("arial", 8, "bold"), fg="white", background="green", width=6, command=show,
            activebackground="green",)

b4.place(x=430, y=270)

b4 = Button(master, text="Hide", font=("arial", 8, "bold"), fg="white", background="green", width=6, command=hide,
            activebackground="green",)

b4.place(x=500, y=270)

b1 = Button(master, text="Log in", font=("arial", 12, "bold"), background="blue", command=logon,
            activebackground="green",)

b1.place(x=430, y=310)

b2 = Button(master, text="Sign Up", font=("arial", 12, "bold"), background="blue", command=sign,
            activebackground="green",)
b2.place(x=320, y=310)

b3 = Button(master, text="Exit", font=("arial", 12, "bold"),background="blue", width=6, command=exit_,
            activebackground="green",)
b3.place(x=520, y=310)

master.mainloop()


