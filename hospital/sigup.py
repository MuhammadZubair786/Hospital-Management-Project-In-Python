from tkinter import *
import os
import sqlite3
import tkinter.messagebox
import pyttsx3

conn = sqlite3.connect('database1.db')
c = conn.cursor()

master1 = Tk()
master1.geometry("700x400")
master1.title("Create Account ")
canvas = Canvas(master1, height=400, width=700)
canvas.pack()

photo = PhotoImage(file="project images/imgg.png")
canvas.create_image(0, 0, image=photo, anchor=NW)

global Name, Age, Gender, Email, Password
Name = StringVar()
Age = StringVar()
Gender = StringVar()
Email = StringVar()
Password = StringVar()
engine = pyttsx3.init()


volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-5000)

voices = engine.getProperty("voices")
engine.say("Sign Up Form ")
engine.runAndWait()


def bck():
    master1.destroy()
    os.system("python test.py")


def create():
    var1 = Email.get()
    var2 = Password.get()

    if var1 == "" and var2 == "" :
        print("please enter all values")
        tkinter.messagebox.showinfo("WARNING", "Please Fill All Field")
    else:
        engine1 = pyttsx3.init()

        volume = engine1.getProperty('volume')
        engine1.setProperty('volume',volume-0)

        rate = engine1.getProperty('rate')
        engine1.setProperty('rate', rate-5000)

        voices = engine1.getProperty("voices")

        for voice in voices:
            engine1.setProperty("voice",voice.id)

        engine1.say("Your Enter Email and password is added in database  "
                    "if message recieved so your data store otherwise not")
        engine1.runAndWait()

        command = "create table if not exists Login(Username text,Password text) "
        conn.execute(command)
        command = "insert into Login(Username ,Password)values(?,?)"
        conn.execute(command, (var1, var2))
        conn.commit()
        
        tkinter.messagebox.showinfo("Success", "Appointment for " + str(var2) + " has been created ")


label = Label(master1, text="Create New Account", font=("arial", 20, "bold"), fg="white", bg="black")
label.place(x=360, y=106)

e1 = Entry(master1, font=("arial", 13, "bold"), width=20, textvariable=Email,)
e1.place(x=440, y=183)
e2 = Entry(master1, font=("arial", 13, "bold"), width=20, textvariable=Password)
e2.place(x=440, y=236)


b1 = Button(master1, text="Create", font=("arial", 14, "bold"), command=create, fg="red", bg="blue",
            activebackground="orange",)
b1.place(x=520, y=300)
b1 = Button(master1, text="Back", font=("arial", 14, "bold"), command=bck, activebackground="orange", fg="red", bg="blue",)
b1.place(x=360, y=300)

master1.mainloop()
