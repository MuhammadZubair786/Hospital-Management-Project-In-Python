from tkinter import *
import tkinter.ttk as ttk
import os
import time
from tkinter import messagebox
import tkinter.messagebox
import sqlite3
import pyttsx3


conn = sqlite3.connect('database1.db')
c = conn.cursor()
root = Tk()
root.title("HOSPITAL MANAGEMENT SYSTEM")
root.configure(width=1500,height=600,bg='BLACK')
root.geometry("1350x900")
engine = pyttsx3.init()


volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-5000)

voices = engine.getProperty("voices")
engine.say("Patients Registration ")
engine.runAndWait()

TableMargin = Frame(root)
TableMargin.place(x=400,y=100)
ids = []
PId = StringVar()
PName = StringVar()
PAge = StringVar()
PGender = StringVar()
PPhone = StringVar()
PBGroup = StringVar()
PLoc = StringVar()
PEmail = StringVar()
localtime = StringVar()

gender = IntVar()
engine1 = pyttsx3.init()

volume = engine1.getProperty('volume')
engine1.setProperty('volume', volume-0)

rate = engine1.getProperty('rate')


voices = engine1.getProperty("voices")
for voice in voices:
    engine1.setProperty("voice", voice.id)

engine1.runAndWait()

def OnSelected(event):
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    ids = selecteditem[0]
    name = selecteditem[1]
    age = selecteditem[2]
    gender = selecteditem[3]
    phone = selecteditem[4]
    bg = selecteditem[5]
    lo = selecteditem[6]
    email = selecteditem[7]


    PId.set(ids)
    PName.set(name)
    PAge.set(age)
    PGender.set(gender)
    PPhone.set(phone)
    PBGroup.set(bg)
    PLoc.set(lo)
    PEmail.set(email)
    engine1.say(f"patient's ID:{ids}")
    engine1.runAndWait()

    
def new():
    if PId.get() != "" or PName.get() != ""or PAge.get() != "" or PGender.get()!="" or PBGroup.get() != "" or PLoc.get() != "" or PEmail.get() != "":
        engine1.say("You click New Button So all Entry Box BLANKS ")
        engine1.runAndWait()
    PId.set("")
    PName.set("")
    PAge.set("")
    PGender.set("")
    PPhone.set("")
    PBGroup.set("")
    PLoc.set("")
    PEmail.set("")


def back():

    root.destroy()
    os.system('python menu.py')


def delete():
    if PId.get() != "":

        sql = "SELECT * FROM Patients_reg WHERE ID LIKE ?"
        sear = c.execute(sql, (PId.get(),))
        l = 0
        for j in sear:
            l = l+1
        if l != 0:
            tkinter.messagebox.showinfo("DELETE", "SUCCESSFULLY DELETE DATA")
            engine1.say("SUCCESSFULLY DELETE DATA")
            sql2 = "DELETE FROM Patients_reg WHERE ID LIKE ?"
            c.execute(sql2, (PId.get(),))
            conn.commit()
            engine1.runAndWait()
            PId.set("")
            PName.set("")
            PAge.set("")
            PGender.set("")
            PPhone.set("")
            PBGroup.set("")
            PLoc.set("")
            PEmail.set("")

        elif l == 0:
            engine1.say("Your Enter Patients Id Is Not Present in database ")
            engine1.runAndWait()
            tkinter.messagebox.showinfo("Warning", "Your Enter Patients Id Is Not Present in Database")

    else:
        engine1.say("Please  Enter Patients Id  ")
        engine1.runAndWait()
        tkinter.messagebox.showinfo("Warning", "Please  Enter Patients Id ")


def add():
    var1 = PId.get()
    var2 = PName.get()
    var3 = PAge.get()
    var4 = PGender.get()
    var5 = PPhone.get()
    var6 = PBGroup.get()
    var7 = PLoc.get()
    var8 = PEmail.get()

    if var1 == "":
        print("please enter all values")
        engine1.say("Please Fill All ENTRY Box")
        engine1.runAndWait()

    elif var2 == "":
        print("please enter all values")
        engine1.say("Please Fill All ENTRY Box")
        engine1.runAndWait()
     
    elif var3 == "":
        print("please enter all values")
        engine1.say("Please Fill All ENTRY Box")
        engine1.runAndWait()
        
    elif var4 == "":
        print("please enter all values")
        engine1.say("Please Fill All ENTRY Box")
        engine1.runAndWait()

    elif var5 == "":
        print("please enter all values")
        engine1.say("Please Fill All ENTRY Box")
        engine1.runAndWait()

    elif var6 == "":
        print("please enter all values")
        engine1.say("Please Fill All ENTRY Box")
        engine1.runAndWait()
         
    elif var7 == "":
        print("please enter all values")
        engine1.say("Please Fill All ENTRY Box")
        engine1.runAndWait()
         
    elif var8 == "":
        print("please enter all values")
        engine1.say("Please Fill All ENTRY Box")
        engine1.runAndWait()
       
    else:
        engine1.say("Now You Fill All Entry Box So Try add DATA Store IN DATABASE SYSTEM")
        engine1.runAndWait()
        # ADD DATA INTO THE DATABASE SQLLITE3
        '''command="create table Patients_reg(name text,age text,gender text,phone text,Bgroup text,ploc text,sch_time text) "
        conn.execute(command)'''
        command = "create table if not exists Patients_reg(name text,age text,gender text,phone text,Bgroup text,ploc text,Email text) "
        conn.execute(command)
        command = "insert into Patients_reg(id,name,age,gender,phone,Bgroup,ploc,Email)values(?,?,?,?,?,?,?,?)"
        add=conn.execute(command, ( var1,var2, var3, var4, var5, var6, var7,var8))
        conn.commit()
        tkinter.messagebox.showinfo("Data Store", "SUCCESSFULLY Data Store")
        engine1.say("Patients DATA Store  IN DATABASE SYSTEM")
        engine1.runAndWait()


def update():
    var1 = PId.get()
    var2 = PName.get()
    var3 = PAge.get()
    var4 = PGender.get()
    var5 = PPhone.get()
    var6 = PBGroup.get()
    var7 = PLoc.get()
    var8 = PEmail.get()
    if var1 != "":
        sql = "SELECT * FROM Patients_reg WHERE ID LIKE ?"
        sear = c.execute(sql, (var1,))
        l = 0
        for j in sear:
            l = l+1
        if l == 0:
            engine1.say("Your Enter Patients Id Is Not Present in database So Not Update Any Data ")
            engine1.runAndWait()
            tkinter.messagebox.showinfo("Warning", "Your Enter Patients Id Is Not Present in Database So Not Update Any Data")

        else:
            query = "UPDATE Patients_reg SET name=?,age=?,gender=?,phone=?,bgroup=?,ploc=?,Email=? WHERE ID LIKE?"
            c.execute(query, (var2, var3, var4, var5, var6, var7, var8, var1))
            conn.commit()
            engine1.say("Successfully DATA UPDATED")
            engine1.runAndWait()
            tkinter.messagebox.showinfo("UPDATE","SUCCESSFULLY UPDATE DATA")
            print("Patient's Name: "+var2+" Data Update")
            PId.set("")
            PName.set("")
            PAge.set("")
            PGender.set("")
            PPhone.set("")
            PBGroup.set("")
            PLoc.set("")
            PEmail.set("")
    else:
        engine1.say("Please  Enter Patients Id  ")
        engine1.runAndWait()
        tkinter.messagebox.showinfo("Warning", "Please  Enter Patients Id ")


def search():
    enter = Id_en.get()
    print("YOUR INPUT IS :"+enter)

    sql = "SELECT * FROM Patients_reg WHERE ID LIKE ?"
    execute = c.execute(sql, (enter,))
    l=0
    for i in execute:
        l = l+1
        ID = i[0]
        name = i[1]
        age = i[2]
        gender = i[3]
        phone = i[4]
        bgroup = i[5]
        location = i[6]
        email = i[7]

    if l == 0:
        PId.set("")
        PName.set("")
        PAge.set("")
        PGender.set("")
        PPhone.set("")
        PBGroup.set("")
        PLoc.set("")
        PEmail.set("")
        engine1.say("Please Enter Correct Id   ")
        engine1.runAndWait()
    else:
        PId.set(ID)
        PName.set(name)
        PAge.set(age)
        PGender.set(gender)
        PPhone.set(phone)
        PBGroup.set(bgroup)
        PLoc.set(location)
        PEmail.set(email)
        engine1.say(f"Your Patient's ID is {ID}")
        engine1.runAndWait()


label0 = Label(root,text="                                              Hospital MANAGEMENT SYSTEM ", bg="black",
               fg="white", font=("Times", 30))
label0.grid(columnspan=6, padx=10, pady=10)


label = Label(root, text=" Date : ", bg="black", fg="white", font=("Times", 17))
label.place(x=530, y=60)
a=time.asctime(time.localtime(time.time()))
localtime.set(a)
print(a)
e=Entry(root, textvariable=localtime, font=("arial", 20, "bold"), width=22, bg="orange")
e.place(x=615, y=60)

logo = Label(root, text="Total Patient's Register:", font=("arial", 12, "bold"), fg="orange", bg="black",)
logo.place(x=70, y=80)
box = Text(root, font=("arial", 10, "bold"), width=35, height=1)
box.place(x=60, y=110)


Id = Label(root, text="Patient's ID :", font=("arial", 14, "bold"), fg="white", activebackground="RED",
           background="black")
Id.place(x=0, y=150)
Id_en = Entry(root, font=("arial",12,"bold"), textvariable=PId)
Id_en.place(x=160, y=150)

name = Label(root, text="Patient's Name:", font=("arial", 14, "bold"), fg="white", activebackground="RED", background="black")
name.place(x=0, y=190)
name_en = Entry(root, font=("arial",12,"bold"),textvariable=PName)
name_en.place(x=160, y=190)

age = Label(root,text="Patient's Age :" ,font=("arial", 14, "bold"), fg="white", activebackground="RED", bg="black")
age.place(x=0,y=230)
age_en = Entry(root ,font=("arial", 12, "bold"),textvariable=PAge)
age_en.place(x=160,y=230)

e_gender = Label(root,text="Patient Gender :",font=("arial",14,"bold"),fg="white",activebackground="RED",background="black")
e_gender.place(x=0,y=270)
gender_en = Entry(root ,font=("arial", 12, "bold"),textvariable=PGender)
gender_en.place(x=160,y=270)


Phone = Label(root,text="Contact :",font=("arial",14,"bold"),fg="white",activebackground="RED",background="black")
Phone.place(x=0,y=310)
Phone_en = Entry(root, font=("arial", 12, "bold"),textvariable=PPhone)
Phone_en.place(x=160,y=310)

Bgroup = Label(root,text=" Blood Group :",font=("arial",14,"bold"),fg="white",activebackground="RED",background="black")
Bgroup.place(x=0,y=350)
Bgroup_en = Entry(root, font=("arial", 12, "bold"),textvariable=PBGroup)
Bgroup_en.place(x=160,y=350)


ploc = Label(root,text="location :",font=("arial",14,"bold"),fg="white",activebackground="RED",background="black")
ploc.place(x=0,y=390)
ploc_en = Entry(root, font=("arial", 12, "bold"),textvariable=PLoc)
ploc_en.place(x=160,y=390)
email = Label(root,text="Email:",font=("arial",14,"bold"),fg="white",activebackground="RED",background="black")
email.place(x=0,y=430)
email_en = Entry(root, font=("arial", 12, "bold"),textvariable=PEmail)
email_en.place(x=160, y=430)

b1 = Button(root,text="ADD",font=("arial",12,"bold"),fg="red",activebackground="RED",background="black",command=add)
b1.place(x=0,y=470)
b1 = Button(root,text="UPDATE",font=("arial",12,"bold"),fg="red",activebackground="RED",background="black",command=update)
b1.place(x=60,y=470)
b1 = Button(root,text="SEARCH",font=("arial",12,"bold"),fg="red",activebackground="RED",background="black",command=search)
b1.place(x=150,y=470)
b1 = Button(root,text="DELETE",font=("arial",12,"bold"),fg="red",activebackground="RED",background="black",command=delete)
b1.place(x=250,y=470)
b1 = Button(root,text="NEW",font=("arial",12,"bold"),fg="red",activebackground="RED",background="black",command=new)
b1.place(x=340,y=470)
b1 = Button(root,text="BACK",font=("arial",12,"bold"),fg="red",activebackground="RED",background="black",command=back)
b1.place(x=150,y=520)

L1 = Label(TableMargin,text="Patients Data",font=("arial",20,"bold"),fg="red",)
L1.pack()

scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=( "Patients_ID", "Patient_Name", "Patient_Age", "Patient_Gender", "Contact", "Blood_Group","Address","Email"), height=50, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)


tree.heading('Patients_ID', text="Patients_ID", anchor=W)
tree.heading('Patient_Name', text="Patient_Name", anchor=W)
tree.heading('Patient_Age', text="Patient_Age", anchor=W)
tree.heading('Patient_Gender', text="Patient_Gender", anchor=W)
tree.heading('Contact', text="Contact", anchor=W)
tree.heading('Blood_Group', text="Blood_Group", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.heading('Email', text="Email", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80,)
tree.column('#2', stretch=NO, minwidth=0, width=110)
tree.column('#3', stretch=NO, minwidth=0, width=110)
tree.column('#4', stretch=NO, minwidth=0, width=100)
tree.column('#5', stretch=NO, minwidth=0, width=110)
tree.column('#6', stretch=NO, minwidth=0, width=100)
tree.column('#7', stretch=NO, minwidth=0, width=100)
tree.column('#8', stretch=NO, minwidth=0, width=100)
tree.bind('<Double-Button-1>', OnSelected)

tree.pack()

sql2 = "SELECT ID FROM Patients_reg "
result = c.execute(sql2)
for row in result:
    ID = row[0]
    ids.append(ID)

new = sorted(ids)
final_id = new[len(ids)-1]

box.insert(END,"Total Registration of Patient's :" + str(final_id))


c.execute("SELECT * FROM Patients_reg")
fetch = c.fetchall()
for data in fetch:
    tree.insert('', 'end', values=(data))
    print(data)


root.mainloop()
