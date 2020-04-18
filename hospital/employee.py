from tkinter import *
import os
import time
import tkinter.ttk as ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3
import pyttsx3


conn = sqlite3.connect('database1.db')
c = conn.cursor()
root = Tk()
root.title("HOSPITAL MANAGEMENT SYSTEM")
root.configure(width=1500, height=600, bg='black')
root.geometry("1350x900")


engine = pyttsx3.init()

volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-5000)

voices = engine.getProperty("voices")
engine.say("Employee Registration ")
engine.runAndWait()


TableMargin = Frame(root)
TableMargin.place(x=400, y=100)
ids = []
EId = StringVar()
EName = StringVar()
EAge = StringVar()
EGender = StringVar()
EType = StringVar()
ESalary = StringVar()
EExp = StringVar()
EEmail = StringVar()
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


def back():
    root.destroy()
    os.system('python menu.py')


def on_selected(event):
    cur_item = tree.focus()
    contents = (tree.item(cur_item))
    selected_item = contents['values']
    ids = selected_item[0]
    name = selected_item[1]
    gender = selected_item[2]
    age = selected_item[3]
    etype = selected_item[4]
    salary = selected_item[5]
    exp = selected_item[6]
    email = selected_item[7]

    EId.set(ids)
    EName.set(name)
    EGender.set(gender)
    EAge.set(age)
    EType.set(etype)
    ESalary.set(salary)
    EExp.set(exp)
    EEmail.set(email)

    engine1.say(f"Employee ID:{ids}")
    engine1.runAndWait()

    
def new():
    if EId.get() != "" or EName.get() != ""or EAge.get() != "" or EGender.get()!="" or EType.get() != "" or ESalary.get() != "" or EExp.get() != "" or EEmail:
        engine1.say("You click New Button So all Entry Box BLANKS ")
        engine1.runAndWait()
    EId.set("")
    EName.set("")
    EAge.set("")
    EGender.set("")
    EType.set("")
    ESalary.set("")
    EExp.set("")
    EEmail.set("")


def delete():
    if EId.get() != "":
        sql = "SELECT * FROM Employee_reg WHERE ID LIKE ?"
        sear = c.execute(sql, (EId.get(),))
        l = 0
        for j in sear:
            l = l+1
        if l != 0:
            sql2 = "DELETE FROM Employee_reg WHERE ID LIKE ?"
            c.execute(sql2, (EId.get(),))
            conn.commit()
            tkinter.messagebox.showinfo("DELETE", "SUCCESSFULLY DELETE DATA")
            engine1.say("SUCCESSFULLY DELETE DATA")
            engine1.runAndWait()
            EId.set("")
            EName.set("")
            EAge.set("")
            EGender.set("")
            EType.set("")
            ESalary.set("")
            EExp.set("")
            EEmail.set("")

        elif l == 0:
            engine1.say("Your Enter Patients Id Is Not Present in database ")
            engine1.runAndWait()
            tkinter.messagebox.showinfo("Warning", "Your Enter Patients Id Is Not Present in Database")

    else:
        engine1.say("Please  Enter Patients Id  ")
        engine1.runAndWait()
        tkinter.messagebox.showinfo("Warning", "Please  Enter Patients Id ")


def add():
    var1 = EId.get()
    var2 = EName.get()
    var3 = EGender.get()
    var4 = EAge.get()
    var5 = EType.get()
    var6 = ESalary.get()
    var7 = EExp.get()
    var8 = EEmail.get()

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
        engine1.say("Now You Fill All Entry Box So Try add DATA Store IN DATABASE SYSTEM If Recieve Message Box So your dATA store")
        engine1.runAndWait()

        # ADD DATA INTO THE DATABASE SQLLITE3
        command="create table if not exists Employee_reg(Id integer,name text,gender text,age text,Employee_Type text,Salary text,Experience text,Email text) "
        conn.execute(command)
        
       
         
        command="insert into Employee_reg(Id,name,gender,age,Employee_Type,Salary,Experience,Email)values(?,?,?,?,?,?,?,?)"
        conn.execute(command, ( var1,var2, var3, var4, var5, var6, var7,var8))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Employee Registration for " + str(var2) + " has been created ")
        

def update():
    var1 = EId.get()
    var2 = EName.get()
    var3 = EGender.get()
    var4 = EAge.get()
    var5 = EType.get()
    var6 = ESalary.get()
    var7 = EExp.get()
    var8 = EEmail.get()

    if var1 != "":
        sql = "SELECT * FROM Employee_reg WHERE ID LIKE ?"
        sear = c.execute(sql, (var1,))
        l = 0
        for j in sear:
            l = l+1
        if l == 0:
            engine1.say("Your Enter Employee Id Is Not Present in database So Not Update Any Data ")
            engine1.runAndWait()
            tkinter.messagebox.showinfo("Warning", "Your Enter Employee Id Is Not Present in Database So Not Update Any Data")

        else:
            query = "UPDATE Employee_reg SET name=?,gender=?,age=?,Employee_Type=?,Salary=?,Experience=?,Email=? WHERE ID LIKE?"
            c.execute(query, (var2, var3, var4, var5, var6, var7, var8, var1))
            conn.commit()
            engine1.say("Successfully DATA UPDATED")
            engine1.runAndWait()
            tkinter.messagebox.showinfo("UPDATE","SUCCESSFULLY UPDATE DATA")
            print("Patient's Name: "+var2+" Data Update")
            EId.set("")
            EName.set("")
            EAge.set("")
            EGender.set("")
            EType.set("")
            ESalary.set("")
            EExp.set("")
            EEmail.set("")

    else:
        engine1.say("Please  Enter Patients Id  ")
        engine1.runAndWait()
        tkinter.messagebox.showinfo("Warning", "Please  Enter Patients Id ")


def search():
    enter = Id_en.get()
    print("YOUR INPUT IS :"+ enter)

    sql = "SELECT * FROM Employee_reg WHERE ID LIKE ?"
    execute = c.execute(sql, (enter,))
    l=0
    for i in execute:
        l = l+1
        ID = i[0]
        name = i[1]
        age = i[2]
        gender = i[3]
        type = i[4]
        Sal = i[5]
        exp = i[6]
        email = i[7]
    if l == 0:
        EId.set("")
        EName.set("")
        EAge.set("")
        EGender.set("")
        EType.set("")
        ESalary.set("")
        EExp.set("")
        EEmail.set("")
        engine1.say("Please Enter Correct Id   ")
        engine1.runAndWait()
    else:
        EId.set(ID)
        EName.set(name)
        EAge.set(age)
        EGender.set(gender)
        EType.set(type)
        ESalary.set(Sal)
        EExp.set(exp)
        EEmail.set(email)
        engine1.say(f"Your Patient's ID is {ID}")
        engine1.runAndWait()


label0 = Label(root, text="Hospital MANAGEMENT SYSTEM ", bg="black", fg="white", font=("Times", 30))
label0.place(x=450, y=10)
label = Label(root, text=" Date : ", bg="black", fg="white", font=("Times", 17))
label.place(x=530, y=60)
a = time.asctime(time.localtime(time.time()))
localtime.set(a)
print(a)
e = Entry(root, textvariable=localtime, font=("arial", 20, "bold"), width=22, bg="orange")
e.place(x=615, y=60)

logo = Label(root, text="Total Employee Register:", font=("arial", 12, "bold"), fg="red", bg="black",)
logo.place(x=70, y=80)
box = Text(root, font=("arial", 10, "bold"), width=35, height=1)
box.place(x=60, y=110)


Id = Label(root, text="Employee ID :", font=("arial", 14, "bold"), fg="white", activebackground="red", bg="black")
Id.place(x=0, y=150)
Id_en = Entry(root, font=("arial", 12, "bold"), textvariable=EId)
Id_en.place(x=180, y=150)

name = Label(root, text="Employee Name:", font=("arial", 14, "bold"), fg="white", activebackground="red", bg="black")
name.place(x=0, y=190)
name_en=Entry(root, font=("arial", 12, "bold"), textvariable=EName)
name_en.place(x=180, y=190)

gender = Label(root, text="Employee Gender:", font=("arial", 14, "bold"), fg="white", activebackground="red", bg="black")
gender.place(x=0, y=230)
gender_en = Entry(root, font=("arial", 12, "bold"), textvariable=EGender)
gender_en.place(x=180, y=230)

age = Label(root, text="Employee Age :", font=("arial", 14, "bold"), fg="white", activebackground="red", bg="black")
age.place(x=0, y=270)
age_en = Entry(root, font=("arial", 12, "bold"), textvariable=EAge)
age_en.place(x=180, y=270)


Type = Label(root, text="Employee Type :", font=("arial", 14, "bold"), fg="white", activebackground="red", bg="black")
Type.place(x=0, y=310)
Type_en = Entry(root, font=("arial", 12, "bold"), textvariable=EType)
Type_en.place(x=180, y=310)

Salary = Label(root, text=" Salary :", font=("arial", 14, "bold"), fg="white", activebackground="red", bg="black")
Salary.place(x=0, y=350)
Salary_en = Entry(root, font=("arial", 12, "bold"), textvariable=ESalary)
Salary_en.place(x=180,y=350)


Exp = Label(root, text="Experience :", font=("arial", 14, "bold"), fg="white", activebackground="red", bg="black")
Exp.place(x=0, y=390)
Exp_en = Entry(root, font=("arial", 12, "bold"), textvariable=EExp)
Exp_en.place(x=180, y=390)

   
Email = Label(root, text="Email:", font=("arial", 14, "bold"), fg="white", activebackground="red", bg="black")
Email.place(x=0, y=430)
Email_en = Entry(root, font=("arial", 12, "bold"), textvariable=EEmail)
Email_en.place(x=180, y=430)

b1 = Button(root, text="ADD", font=("arial", 12, "bold"), fg="white", activebackground="yellow", bg="red", command=add)
b1.place(x=0, y=470)

b1 = Button(root, text="UPDATE", font=("arial", 12, "bold"), fg="white", activebackground="yellow", bg="red", command=update)
b1.place(x=60, y=470)

b1 = Button(root, text="SEARCH", font=("arial", 12, "bold"), fg="white", activebackground="yellow", bg="red", command=search)
b1.place(x=150, y=470)

b1 = Button(root, text="DELETE", font=("arial", 12, "bold"), fg="white", activebackground="yellow", bg="red", command=delete)
b1.place(x=250, y=470)

b1 = Button(root, text="NEW", font=("arial", 12, "bold"), fg="white", activebackground="yellow", bg="red", command=new)
b1.place(x=340, y=470)

b1 = Button(root, text="BACK", font=("arial", 12, "bold"), fg="white", activebackground="yellow", bg="red", command=back)
b1.place(x=140, y=520)


L1 = Label(TableMargin, text="EMPLOYEE DATA", font=("arial", 20, "bold"), fg="black",)
L1.pack()
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Employee_ID", "Employee_Name","Employee_Gender", "Employee_Age", "Employee Type", "Salary", "Experience", "Email"), height=50, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)


tree.heading('Employee_ID', text="Employee_ID", anchor=W)
tree.heading('Employee_Name', text="Employee_Name", anchor=W)
tree.heading('Employee_Gender', text="Employee_Gender", anchor=W)
tree.heading('Employee_Age', text="Employee_Age", anchor=W)
tree.heading('Employee Type', text="Employee Type", anchor=W)
tree.heading('Salary', text="Salary", anchor=W)
tree.heading('Experience', text="Experience", anchor=W)
tree.heading('Email', text="Email", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=60)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=110)
tree.column('#4', stretch=NO, minwidth=0, width=100)
tree.column('#5', stretch=NO, minwidth=0, width=110)
tree.column('#6', stretch=NO, minwidth=0, width=100)
tree.column('#7', stretch=NO, minwidth=0, width=100)
tree.column('#8', stretch=NO, minwidth=0, width=100)
tree.bind('<Double-Button-1>', on_selected)

tree.pack()

sql2 = "SELECT ID FROM Employee_reg "
result = c.execute(sql2)
for row in result:
    ID = row[0]
    ids.append(ID)

new = sorted(ids)
final_id = new[len(ids)-1]

box.insert(END, "Total Registration of Employee :" + str(final_id))


c.execute("SELECT * FROM Employee_reg")
fetch = c.fetchall()
for data in fetch:
    tree.insert('', 'end', values=data)
    print(data)

root.mainloop()
