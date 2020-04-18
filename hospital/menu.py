from tkinter import *
import os



master = Tk()
master.configure(bg="black")
master.geometry("1350x900")
l = Label(master, text="Hospital Management System ", bg="red", fg="white", font=("arial", 30, "bold"))
l.place(x=280, y=15)




def Out():
    master.destroy()
    os.system('python test.py')


def exit1():
    master.destroy()

    
def pdata():
    master.destroy()
    os.system('python new.py')


def edata():
    master.destroy()
    os.system('python employee.py')


def rdata():
    master.destroy()
    os.system('python roomallocated.py')


def aapp():
    master.destroy()
    os.system('python Booking_Appoitement.py')


def pbill():
    master.destroy()
    os.system('python bill.py')
    

b = Button(master, text="***********>PATIENT'S DATA<**********", font=("arial", 20, ""), activebackground="yellow", command=pdata)
b.place(x=300,y=100)

b = Button(master, text="***********>EMPLOYEE DATA<*********", font=("arial", 20, ""), activebackground="yellow", command=edata)
b.place(x=300,y=200)


b = Button(master, text="********>ROOM ALLOCATTED<*******", font=("arial", 20, ""), activebackground="yellow", command=rdata)
b.place(x=300, y=300)

b = Button(master, text="*********>ADD APPOITEMENT<*******", font=("arial", 20, ""), activebackground="yellow", command=aapp)
b.place(x=300, y=400)

b = Button(master, text="***********>PATIENT'S BILL<**********", font=("arial", 20, ""), activebackground="yellow", command=pbill)
b.place(x=300, y=500)

b = Button(master, text="***> Log  Out <***", font=("arial", 22, ""), activebackground="yellow", command=Out)
b.place(x=300, y=600)

b = Button(master, text="***> Exit <***", font=("arial", 22, ""), activebackground="yellow", command=exit1)
b.place(x=590, y=600)


master.mainloop()



