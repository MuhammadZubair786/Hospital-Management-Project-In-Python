from tkinter import *
import os
import tkinter.ttk as ttk
import sqlite3
import pyttsx3
import time
import tkinter.messagebox
conn = sqlite3.connect('database1.db')
c= conn.cursor()
ids = []

print("DATA OF EMPLOYEE:")
sql = "SELECT *  FROM Employee_reg "
result = c.execute(sql)
for r in result:
    print(r)


master = Tk()
master.title("HOSPITAL MANAGEMENT SYSTEM")
master.geometry("1370x700+0+0")
master.configure(background="black")
master.resizable(FALSE,FALSE)
frame = Frame(master)
frame.pack()
TableMargin = Frame(master)
TableMargin.place(x=250,y=80)
TableMargin1 = Frame(master)
TableMargin1.place(x=350,y=100)
TableMargin2 = Frame(master)
TableMargin2.place(x=650,y=100)
gender = IntVar()
location = IntVar()
var4 = IntVar()
localtime = StringVar()
engine = pyttsx3.init()

volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-5000)

voices = engine.getProperty("voices")
engine.say("Patients Appoitement Data ")
engine.runAndWait()

bottomframe = Frame(master, width="230", background="purple", height="500", highlightbackground="YELLOW", highlightcolor="RED", highlightthickness=5)
bottomframe.place( x=30, y=120)
label0 = Label(master, text="  Hospital MANAGEMENT SYSTEM ", bg="black", fg="white", font=("Times", 25))
label0.place(x=500, y=10)
label = Label(master, text=" Date : ", bg="black", fg="white", font=("Times", 25))
label.place(x=530, y=55)
a=time.asctime(time.localtime(time.time()))
localtime.set(a)
print(a)
e=Entry(master, textvariable=localtime, font=("arial", 20, "bold"), width=23, bg="orange")
e.place(x=630, y=55)


def back():
    master.destroy()
    os.system('python menu.py')


def Delete():
    var1 = Ano_en.get()
    sql2 = "DELETE FROM  Booking_App  WHERE App_No LIKE ?"
    c.execute(sql2, (var1,))
    conn.commit()
    tkinter.messagebox.showinfo("DELETE","SUCCESSFULLY DELETE DATA")
    root.destroy()
    

def Update():
    
    var1 = pname_en.get()
    var2 = pgender_en.get()
    var3 = did_en.get()
    var4 = Ano_en.get()
    var5 = Atime_en.get()
    var6 = Adate_en.get()
    var7 = dE_en.get()
    print(var1,var2,var3,var4,var5,var6,var7)
    query="UPDATE Booking_App SET Patients_Name=?,Patients_Gender=?,Doctor_ID=?,App_Time=?,App_Date=?,Description=? WHERE App_No LIKE?"
    c.execute(query,(var1,var2,var3,var5,var6,var7,var4))
    conn.commit()
    tkinter.messagebox.showinfo("UPDATE","SUCCESSFULLY UPDATE DATA")
    print("Data Update")
    root.destroy()


def OnSelected(event):
    global pname_en,pgender_en,did_en,Ano_en,Atime_en,Adate_en,dE_en,root
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    Pname = selecteditem[0]
    Pgen = selecteditem[1]
    Did = selecteditem[2]
    app_no = selecteditem[3]
    app_time = selecteditem[4]
    app_date = selecteditem[5]
    discription = selecteditem[6]

    root = Tk()
    root.config(bg="yellow")
    root.geometry("200x250+780+400")
    l = Label(root,text="Patient's Name ",bg="yellow")
    l.place(x=0,y=0)
    pname_en = Entry(root,width=10)
    pname_en.insert(END,str(Pname))
    pname_en.place(x=90,y=0)

    l = Label(root,text="Patient's Gender ",bg="yellow")
    l.place(x=0,y=30)
    pgender_en=Entry(root,width=10)
    pgender_en.insert(END,str(Pgen))
    pgender_en.place(x=100,y=30)

    l = Label(root,text="Doctor_ID ",bg="yellow")
    l.place(x=0,y=60)
    did_en = Entry(root,width=10)
    did_en.insert(END,str(Did))
    did_en.place(x=100,y=60)

    l = Label(root,text="APP_No ",bg="yellow")
    l.place(x=0,y=90)
    Ano_en = Entry(root,width=10)
    Ano_en.insert(END,str(app_no))
    Ano_en.place(x=100,y=90)

    l = Label(root,text="APP_Time",bg="yellow")
    l.place(x=0,y=120)
    Atime_en = Entry(root,width=10)
    Atime_en.insert(END,str(app_time))
    Atime_en.place(x=100,y=120)

    l = Label(root, text="App_Date", bg="yellow")
    l.place(x=0,y=150)
    Adate_en=Entry(root,width=10)
    Adate_en.insert(END,str(app_date))
    Adate_en.place(x=100,y=150)

    l=Label(root,text="Discription",bg="yellow")
    l.place(x=0,y=180)
    dE_en=Entry(root,width=10)
    dE_en.insert(END,str(discription))
    dE_en.place(x=100,y=180)

    b1 = Button(root,text="Update",command=Update,bg="orange",font=("arial",11,"bold"),fg="blue",activebackground="red")
    b1.place(x=20,y=210)
    b1=Button(root,text="Delete",command=Delete,bg="orange",font=("arial",11,"bold"),fg="blue",activebackground="red")
    b1.place(x=100,y=210)


def Exit():
    master.destroy()


def add_Employee():        
        
    var1 = P_Name_en.get()
    var2 = p_gender_en.get(tkinter.ACTIVE)
    var3 = D_ID_en.get()
    var4 = App_no_en.get(tkinter.ACTIVE)
    var5 = App_Time_en.get()
    var6 = App_Date_en.get()
    var7 = dec_en.get()
    print(var1,var2,var3,var4,var5,var6,var7)
    if var1 == "":
         print("please enter all values")
         tkinter.messagebox.showinfo("WARNING","Please Fill All Field")
    if var2=="" :
         print("please enter all values")
         tkinter.messagebox.showinfo("WARNING","Please Fill All Field")
    if var4 =="":
         print("please enter all values")
         tkinter.messagebox.showinfo("WARNING","Please Fill All Field")

    else:
        sql1="SELECT * FROM Employee_reg WHERE ID LIKE ?"
        execute1 = c.execute(sql1, (var3,))

        for i in execute1:
            ID = i[0]
            D_name = i[1]
        
            command="create table if not exists Booking_App(Patients_Name integer,Patients_Gender text,Doctor_ID integer,App_No integer,App_Time text,App_Date text,Description text) "
            conn.execute(command)

            command="insert into Booking_App(Patients_Name ,Patients_Gender,Doctor_ID ,App_No ,App_Time ,App_Date,Description)values(?,?,?,?,?,?,?)"
            conn.execute(command, ( var1,var2, var3, var4, var5, var6,var7))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Appoitement of " + var2 + " has been saved ")
            print("Insert New Data :")

            if var1 != "":
                print(f"P_ID:{var1}")
        
            if var2 != "":
                print(f"D_ID:{var2}")
            if var3 != "":
                print(f"APP_NO:{var3}")
            if var4 != "":
                print(f"APP_TIME:{var4}")
            if var5 != "":
                print(f"APP_DATE:{var5}")
            if var6 != "":
                print(f"DESCRIPTION:{var6}")


P_Name=Label(bottomframe,text="Patient's Name :",font=("arial",10,"bold"),fg="white",activebackground="RED",background="purple")
P_Name.place(x=25,y=20)
P_Name_en=Entry(bottomframe,font=("arial",10,"bold"))
P_Name_en.place(x=10,y=50)

p_gender=Label(bottomframe,text="Patient's Gender  :",font=("arial",10,"bold"),fg="white",activebackground="RED",background="purple")
p_gender.place(x=25,y=80)
L=['Male','Female']
p_gender_en=Listbox(bottomframe, width=22, height=1, selectmode='SINGLE', exportselection=0)
for i in L:
    p_gender_en.insert(END, i)
p_gender_en.place(x=10,y=110)

D_ID=Label(bottomframe,text="Doctor ID :",font=("arial",10,"bold"),fg="white",activebackground="RED",background="purple")
D_ID.place(x=25,y=140)
D_ID_en = Entry(bottomframe ,font=("arial", 10, "bold"))
D_ID_en.place(x=10,y=170)

App_no=Label(bottomframe,text="Appoitement No  :",font=("arial",10,"bold"),fg="white",activebackground="RED",background="purple")
App_no.place(x=25,y=200)
L=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50']
App_no_en=Listbox(bottomframe, width=15, height=1, selectmode='SINGLE', exportselection=0)
for j in L:
    App_no_en.insert(END, j)
App_no_en.place(x=10,y=230)
scrollbar = Scrollbar(bottomframe,orient=HORIZONTAL)
scrollbar.place(x=115, y=230)
App_no_en.config(yscrollcommand=scrollbar.set)
scrollbar.configure(command=App_no_en.yview)

App_Time=Label(bottomframe,text="Appoitement Time :",font=("arial",10,"bold"),fg="white",activebackground="RED",background="purple")
App_Time.place(x=25,y=260)
App_Time_en = Entry(bottomframe, font=("arial", 10, "bold"))
App_Time_en.place(x=10,y=290)

App_Date=Label(bottomframe,text="Appoitement Date :",font=("arial",10,"bold"),fg="white",activebackground="RED",background="purple")
App_Date.place(x=25,y=320)
App_Date_en = Entry(bottomframe, font=("arial", 10, "bold"))
App_Date_en.place(x=10,y=350)

dec=Label(bottomframe,text="Descripition :",font=("arial",10,"bold"),fg="white",activebackground="RED",background="purple")
dec.place(x=25,y=380)
dec_en = Entry(bottomframe, font=("arial", 10, "bold"))
dec_en.place(x=10,y=410)

b1=Button(bottomframe,text="+++Add Appoitement+++",bg="red",font=("arial",11,"bold"),command=add_Employee,fg="white", highlightbackground="YELLOW",highlightcolor="RED")
b1.place(x=10,y=450)


b1=Button(master,text=">>BACK<<",bg="red",font=("arial",13,"bold"),command=back,fg="white", highlightbackground="YELLOW",highlightcolor="RED")
b1.place(x=60,y=640)


L1=Label(TableMargin1,text="Doctor Data",font=("arial",20,"bold"),fg="red",)
L1.pack()

scrollbarx = Scrollbar(TableMargin1, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin1, orient=VERTICAL)
tree = ttk.Treeview(TableMargin1, columns=("ID", "Name",), height=50, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

tree.heading('ID', text="ID", anchor=W)
tree.heading('Name', text="Name", anchor=W)

tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=50,)

tree.pack()

c.execute("SELECT * FROM Employee_reg ")
fetch = c.fetchall()
for data in fetch:
    tree.insert('', 'end', values=(data))
    print(data)


L1=Label(TableMargin2,text="Appoitement Data",font=("arial",20,"bold"),fg="red",)
L1.pack()

scrollbarx = Scrollbar(TableMargin2, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin2, orient=VERTICAL)
tree = ttk.Treeview(TableMargin2, columns=("P_Name", "P_Gender","Doctor_ID","App_No","App_Time","App_Date","Disc"), height=50, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

tree.heading('P_Name', text="P_Name", anchor=W)
tree.heading('Doctor_ID', text="Doctor_ID", anchor=W)
tree.heading('P_Gender', text="P_Gender", anchor=W)
tree.heading('App_No', text="App_No", anchor=W)
tree.heading('App_Time', text="App_Time", anchor=W)
tree.heading('App_Date', text="App_Date", anchor=W)
tree.heading('Disc', text="Discription  ", anchor=W)


tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80,)
tree.column('#2', stretch=NO, minwidth=0, width=80,)
tree.column('#3', stretch=NO, minwidth=0, width=80,)
tree.column('#4', stretch=NO, minwidth=0, width=90,)
tree.column('#5', stretch=NO, minwidth=0, width=90,)
tree.column('#6', stretch=NO, minwidth=0, width=90,)


tree.bind('<Double-Button-1>', OnSelected)

tree.pack()

c.execute("SELECT * FROM Booking_App")
fetch = c.fetchall()
for data in fetch:
    tree.insert('', 'end', values=(data))
    print(data)


master.mainloop()
