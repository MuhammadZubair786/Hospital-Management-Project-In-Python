from tkinter import *
import os
import tkinter.ttk as ttk
import sqlite3
import time
import pyttsx3
import tkinter.messagebox

conn = sqlite3.connect('database1.db')
c = conn.cursor()
ids = []


master = Tk()
master.title("HOSPITAL MANAGEMENT SYSTEM")
master.geometry("1370x700+0+0")
master.configure(background="Black")
master.resizable(FALSE,FALSE)
localtime = StringVar()
label0 = Label(master, text="      Hospital MANAGEMENT SYSTEM ", bg="black", fg="white",font=("Times", 30))
label0.place(x=400, y=10)
label = Label(master, text=" Date : ", bg="black", fg="white", font=("Times", 17))
label.place(x=530, y=65)
a=time.asctime(time.localtime(time.time()))
localtime.set(a)
print(a)
e = Entry(master, textvariable=localtime, font=("arial", 20, "bold"), width=22, bg="orange")
e.place(x=615,y=65)

engine = pyttsx3.init()


volume = engine.getProperty('volume')
engine.setProperty('volume',volume-0)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-5000)

voices = engine.getProperty("voices")
engine.say("Room Allocated Registration ")
engine.runAndWait()

TableMargin = Frame(master)
TableMargin.place(x=300,y=110)

TableMargin1 = Frame(master)
TableMargin1.place(x=770,y=110)

gender = IntVar()
location = IntVar()
var4 = IntVar()
Price = StringVar()
RoomType = StringVar()
RoomNo = StringVar()


bottomframe = Frame(master,width="200",background="RED",height="500", highlightbackground="Orange",highlightcolor="Blue", highlightthickness=5)
bottomframe.place(x=30,y=100)


def back():
    master.destroy()
    os.system('python menu.py')


def ok():
    var1 = Id_en.get()
    var2 = R_type_en.get(tkinter.ACTIVE)
    var3 = R_no_en.get(tkinter.ACTIVE)
    
    print(var1, var2, var3)
    if var2 == "SINGLE ROOM: Rs 4500":
        Price.set(4500)
        RoomType.set("SINGLE ROOM")

    if var2 == "TWIN SHARING : Rs2500":
        Price.set(2500)
        RoomType.set("TWIN SHARING")
        
    if var2 == "TRIPLE SHARING: Rs2000":
        Price.set(2000)
        RoomType.set("TRIPLE SHARING")

    RoomNo.set(var3)


def Delete():
    sql2 = "DELETE FROM Room_allocated  WHERE Id LIKE ?"
    c.execute(sql2, (ids,))
    conn.commit()
    tkinter.messagebox.showinfo("DELETE", "SUCCESSFULLY DELETE DATA")
    root.destroy()


def Update():
    a = dE.get()
    print(ids, room_type, room_No, Date_Addmitted, a)
    query = "UPDATE Room_allocated SET Room_Type=?,Room_No=?,Date_ADDMITED=?,Date_DISCHARGED=?,Price=? WHERE Id LIKE?"
    c.execute(query, (room_type, room_No, Date_Addmitted, a, price, ids))
    conn.commit()
    tkinter.messagebox.showinfo("UPDATE", "SUCCESSFULLY UPDATE DATA")
    print("Data Update")
    root.destroy()


def OnSelected(event):
    global ids, room_type, room_No, Date_Addmitted, dE, price, root
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    ids = selecteditem[0]
    room_type = selecteditem[1]
    room_No = selecteditem[2]
    Date_Addmitted = selecteditem[3]
    Date_Discharged = selecteditem[4]
    price = selecteditem[5]

    root = Tk()
    root.config(bg="yellow")
    root.geometry("200x140+780+400")
    l = Label(root, text="Patient's ID ", bg="yellow")
    l.place(x=0, y=0)
    pE = Entry(root, width=10)
    pE.insert(END, str(ids))
    pE.place(x=80, y=0)

    l = Label(root, text="Date Addmitted ", bg="yellow")
    l.place(x=0, y=30)
    aE = Entry(root, width=10)
    aE.insert(END, str(Date_Addmitted))
    aE.place(x=100, y=30)

    l = Label(root, text="Date Discharged ", bg="yellow")
    l.place(x=0, y=60)
    dE = Entry(root, width=10)
    dE.insert(END, str(Date_Discharged))
    dE.place(x=100, y=60)

    b1 = Button(root, text="Update", command=Update, bg="orange", font=("arial", 12, "bold"), fg="blue", activebackground="red")
    b1.place(x=20,y=100)
    b1 = Button(root, text="Delete", command=Delete, bg="orange", font=("arial", 12, "bold"), fg="blue", activebackground="red")
    b1.place(x=100, y=100)
    

def Room_Allocated():
        
    var1 = Id_en.get()
    var2 = RoomType.get()
    var3 = RoomNo.get()
    var4 =dadmitted_en.get()
    var5 =ddischarged_en.get()
    var6=Price.get()

    if var1 == "":
        print("please enter Patients ID")
        tkinter.messagebox.showinfo("WARNING","Please enter Patients ID")   

    elif var2 == "":
        print("please enter all values And Then Click Ok")
        tkinter.messagebox.showinfo("WARNING","Please Fill All Field And Then Click Ok")
         
    elif var3 == "":
        print("please enter all values And Then Click Ok")
        tkinter.messagebox.showinfo("WARNING","Please Fill All Field And Then Click Ok")

    elif var4 == "":
        print("please enter all values And Then Click Ok")
        tkinter.messagebox.showinfo("WARNING","Please Fill All Field And Then Click Ok")

    elif var6 == "":
        print("please enter all values And Then Click Ok")
        tkinter.messagebox.showinfo("WARNING","Please Fill All Field And Then Click Ok")

    else:
        ##ADD DATA INTO THE DATABASE SQLLITE3

        sql = "SELECT * FROM Patients_reg WHERE ID LIKE ?"
        execute = c.execute(sql, (var1,))
    
        for j in execute:
            ID = j[0]
            name = j[1]
            print(j)
          
            '''command="create table Room_allocated(Id text,Room_Type text,Room_No text,Date_ADDMITED text,Price text) "
            conn.execute(command) '''
            command="create table if not exists Room_allocated(Id text,Room_Type text,Room_No text,Date_ADDMITED text,Date_DISCHARGED text,Price integer) "
            conn.execute(command)
           
             
            command="insert into Room_allocated(Id,Room_Type,Room_No,Date_ADDMITED,Date_DISCHARGED,Price)values(?,?,?,?,?,?)"
            conn.execute(command, (var1, var2, var3, var4, var5,var6))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Room Allocatted for  patients id " + str(var1) + " has been created ")

            print("Insert New Data :")

            if var1 != "":
                print(f"Pa_ID:{var1}")

            if var2 != "":
                print(f"Room_Type:{var2}")
            
            if var3 != "":
                print(f"Room_No{var3}")

            if var4 != "":
                print(f"date _addmited:{var4}")

            if var5 != "":
                print(f"Date_Discharged:{var5}")

            if var6 != "":
                print(f"Room_Price:{var6}")
                    
                  
Id = Label(bottomframe,text="Patient's ID      :",font=("arial",10,"bold"),fg="white",activebackground="RED",background="RED")
Id.place(x=25,y=10)
Id_en = Entry(bottomframe,font=("arial",10,"bold"))
Id_en.place(x=10,y=30)


R_type = Label(bottomframe,text="Room Type     :",font=("arial",10,"bold"),fg="white",activebackground="RED",background="RED")
R_type.place(x=25,y=60)
L = ['SINGLE ROOM: Rs 4500','TWIN SHARING : Rs2500','TRIPLE SHARING: Rs2000']
R_type_en=tkinter.Listbox(bottomframe,font=("arial",10,"bold"),width=23, height=3, selectmode='SINGLE', exportselection=0)
for jjj in L:
    R_type_en.insert(tkinter.END, jjj)

R_type_en.place(x=10,y=80)

R_no = Label(bottomframe,text="Room NO       :",font=("arial",10,"bold"),fg="white",activebackground="RED",background="RED")
R_no.place(x=25,y=140)
L = ['101','102-AA','102-BB','103','104-AA','104-BB','105','206-AAA','206-BBB','206-CCC','207','208-AAA','208-BBB','208-CCC','210','211','302','304-AA','304-BB']

R_no_en=tkinter.Listbox(bottomframe,font=("arial",10,"bold"), height=1, selectmode='SINGLE', exportselection=0)
for select in L:
    R_no_en.insert(tkinter.END, select)
   
   
R_no_en.place(x=10,y=160)
# location_en.place(x=54,y=380)

dadmitted = Label(bottomframe,text="Date Admitted:",font=("arial",10,"bold"),fg="white",activebackground="RED",background="RED")
dadmitted .place(x=25,y=190)
dadmitted_en = Entry(bottomframe, font=("arial", 10, "bold"))
dadmitted_en.place(x=10, y=210)

ddischarged = Label(bottomframe,text="Date Discharged:",font=("arial",10,"bold"),fg="white",activebackground="RED",background="RED")
ddischarged.place(x=25,y=240)
ddischarged_en = Entry(bottomframe, font=("arial", 10, "bold"))
ddischarged_en.place(x=10, y=260)

b1 = Button(bottomframe,text="Ok",font=("arial",10,"bold"),command=ok, highlightbackground="YELLOW",highlightcolor="RED")
b1.place(x=30,y=290)

roomtype = Label(bottomframe,text="Room Type  :",font=("arial",10,"bold"),fg="white",activebackground="RED",background="RED")
roomtype.place(x=25,y=330)
roomtype_en = Entry(bottomframe, font=("arial", 10, "bold"),textvariable=RoomType)
roomtype_en.place(x=10, y=350)

roomno = Label(bottomframe,text="Room No       :",font=("arial",10,"bold"),fg="white",activebackground="RED",background="RED")
roomno.place(x=25,y=380)
roomno_en = Entry(bottomframe, font=("arial", 10, "bold"),textvariable=RoomNo)
roomno_en.place(x=10, y=400)


price = Label(bottomframe,text="Price              :",font=("arial",10,"bold"),fg="white",activebackground="RED",background="RED")
price.place(x=25,y=430) 
price_en = Entry(bottomframe, font=("arial", 10, "bold"),textvariable=Price)
price_en.place(x=10, y=450)


b1 = Button(master,text="Room Allocated",font=("arial",12,"bold"),fg="white",activebackground="orange",bg="green",command=Room_Allocated, highlightbackground="YELLOW",highlightcolor="RED")
b1.place(x=15,y=620)

b1 = Button(master,text="Back",font=("arial",12,"bold"),fg="white",activebackground="orange",bg="green",command=back, highlightbackground="YELLOW",highlightcolor="RED")
b1.place(x=170,y=620)


L1 = Label(TableMargin,text="Patients Data",font=("arial",20,"bold"),fg="red",)
L1.pack()

scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("ID", "Patients_ID", "Room_Type"), height=50, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

tree.heading('ID', text="ID", anchor=W)
tree.heading('Patients_ID', text="Patients_Name", anchor=W)
tree.heading('Room_Type', text="Patient_Age", anchor=W)


tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80,)
tree.column('#2', stretch=NO, minwidth=0, width=110)


tree.pack()


c.execute("SELECT * FROM Patients_reg")
fetch = c.fetchall()
for data in fetch:
    tree.insert('', 'end', values=(data))
    print(data)


L1=Label(TableMargin1,text="Room Allocatted Data",font=("arial",20,"bold"),fg="red",)
L1.pack()

scrollbarx = Scrollbar(TableMargin1, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin1, orient=VERTICAL)
tree = ttk.Treeview(TableMargin1, columns=( "Patients_ID", "Room_Type", "Room_No","Date_Addmitted","Date_Discharged","Price"), height=50, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)


tree.heading('Patients_ID', text="Patients_ID", anchor=W)
tree.heading('Room_Type', text="Room_Type", anchor=W)
tree.heading('Room_No', text="Room_No", anchor=W)
tree.heading('Date_Addmitted', text="Date_Addmitted", anchor=W)
tree.heading('Date_Discharged', text="Date_Discharged", anchor=W)
tree.heading('Price', text="Price", anchor=W)


tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=68,)
tree.column('#2', stretch=NO, minwidth=0, width=100)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=100)
tree.column('#5', stretch=NO, minwidth=0, width=100)
tree.column('#6', stretch=NO, minwidth=0, width=60)
tree.bind('<Double-Button-1>', OnSelected)

tree.pack()
c.execute("SELECT * FROM Room_allocated ")
fetch = c.fetchall()
for data in fetch:
    tree.insert('', 'end', values=(data))
    print(data)


master.mainloop()
