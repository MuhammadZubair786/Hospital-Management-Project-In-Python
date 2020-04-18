from tkinter import *
import os
import sqlite3
import time
import pyttsx3
import tkinter.messagebox
conn=sqlite3.connect('database1.db')
c=conn.cursor()

master = Tk()
master.title("Hospital  MANGEMENT SYSTEM")
master.geometry("1180x800+150+0")
master.configure(background="black")

localtime = StringVar()
label0 = Label(master,text="Hospital Mangement System(Patient's Bill)",bg="black",fg="white",font=("Times", 20))
label0.place(x=350,y=3)
label = Label(master,text=" Date : ",bg="black",fg="white",font=("Times", 17))
label.place(x=370,y=50)
a=time.asctime(time.localtime(time.time()))

engine = pyttsx3.init()


# engine1.getProperty('voice' , ru_voice_id)

volume=engine.getProperty('volume')
engine.setProperty('volume',volume-0)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-5000)

voices=engine.getProperty("voices")
# for voice in  voices:
    #engine1.setProperty("voice",voice.id)
engine.say("Patient's Bill")
engine.runAndWait()

ID = StringVar()
DD = StringVar()
TDA = StringVar()
QUN = StringVar()
localtime.set(a)

engine1 = pyttsx3.init()

volume=engine1.getProperty('volume')
engine1.setProperty('volume',volume-0)

rate = engine1.getProperty('rate')


voices = engine1.getProperty("voices")
for voice in voices:
    engine1.setProperty("voice",voice.id)

engine1.runAndWait()

print(a)
e=Entry(master,textvariable=localtime,font=("arial",18,"bold"),width=22,bg="orange")
e.place(x=450,y=50)
bottomframe = Frame(master,width="480",background="black",height="600", highlightbackground="cyan",highlightcolor="cyan", highlightthickness=5)
bottomframe.place( x=350,y=90)


def new():
    ID.set("")
    DD.set("")
    TDA.set("")
    QUN.set("")


def back():
   master.destroy()
   os.system('python menu.py')


global TOTAL_ROOM_PRICE


def generatebill():
    print(t1)
    var1=P_id_en.get()

    var2=P_name_en.get()

    var3=P_age_en.get()

    var4=P_gender_en.get()

    var5=Room_No_en.get()

    var6=Room_Type_en.get()

    var7=P_da_en.get()

    var8=P_dd_en.get()

    var9=Treatment_en.get()

    var10=Medicines_en.get()

    var11=int(tr_Price_en.get())

    print(type(var11))

    var12=int(med_Price_en.get())

    var13=(Price_en.get())

    var14=int(tmp_Price_en.get())

    var15=int(quantity_en.get())
   
    print("**************************************Bill of Patient's*************************************************")

    localtime=time.asctime(time.localtime(time.time()))
    print("Time :",localtime)
    if var1 !="":
      print(f"Patient's Id : {var1} ")
    if var2 !="":
      print(f"Patient's Name : {var2} ")
      engine1.say(f"Patient's Name {var2}")

      engine1.runAndWait()
    if var3 != "":
      print(f"Patient's Age : {var3} ")
    if var4!="":
      print(f"Patient's Gender: {var4} ")
    if var5 !="":
      print(f"Patient's Room No : {var5}")
      engine1.say(f"Patient's Room NUMBER {var5}")
      engine1.runAndWait()
    if( var6!=""):
      print(f"Patient's Room Type : {var6} ")
      engine1.say(f"Patient's Room  Type {var6}")

      engine1.runAndWait()
    if(var7!=""):
      print(f"Patient's Date Addmitted : {var7} ")
      print("The  Total Day Addmit :",sum1)
    if(var8!=""):
      print(f"Patient's Date Dischaged : {var8} ")

    if(var9!=""):
      print(f"Patient's Treatment  : {var9} ")
      engine1.say(f"Patient's Tretment {var9}")

      engine1.runAndWait()
    if(var10!=""):
      print(f"Patient's Medicine  : {var10} ")
      engine1.say(f"Medicine {var10}")

      engine1.runAndWait()
    if(var11!=""):
      print(f"Patient's Total Treatment price  : {var11}  ")
      engine1.say(f"Patient's Total Treatment price {var11}")

      engine1.runAndWait()
    if (var12 != ""):
       print(f"Patient's Medicine Price  : {var12}")

    if(var14!=""):
      print(f"Patient's Total Medicine Price  : {var14} ")
      engine1.say(f"Patient's Total Medicine price {var14}")

      engine1.runAndWait()


    if(var13!=""):
      print(f"Patient's Room price Of one Day  : {var13} ")
      engine1.say(f"Patient's Room Price of one Day: {var13}")

      engine1.runAndWait()
   
    if(var15!=""):
      print(f"Patient's Total Quantity Medicine   : {var15} ")
   
   
    if(t1!=0 or t1==""):
      
      print(f"The Total Room Price :{t1}")
      engine1.say(f"Total Room Price {t1}")

      engine1.runAndWait()


    b=var11+(var14*var15)
    print("Total Patient's Medicine Price:",b)
    total_patient=t1+b
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
   
    print("TOTAL BILL of Patients  :",total_patient)
    engine1.say(f"so  Total Bill Of Patients  {total_patient}")

    engine1.runAndWait()
    engine1.say("Thanks you For you Visit my hospital Please Tell your Are Satisfy or not")
    engine1.runAndWait()


def UPDATE():
   
   print("well")
   ID =Id_en.get()
   Date_Discharged =dd_en.get()
   
   conn.execute("UPDATE Room_allocated  SET Date_DISCHARGED=? where Id=?", (Date_Discharged,ID ,))
   conn.commit()
   tkinter.messagebox.showinfo("MEDANTA DATABASE SYSTEM", "DISCHARGE DATE UPDATED")
   
   
def Check():
    global P_id_en,P_name_en,P_age_en,P_gender_en,Room_No_en,Room_Type_en,P_da_en,P_dd_en,Treatment_en,Medicines_en,tr_Price_en,med_Price_en,R_Price_en,tmp_Price_en,Price_en
    global t1,sum1,P_id,P_name,P_age,P_gender,Room_No,Room_Type,P_da,P_dd,Treatment,Medicines,tr_Price,med_Price,R_Price,tmp_Price
    t1 = 0
    print("work")
    P_ID = Id_en.get()
    DD = dd_en.get()
    Treat = treat_en.get(tkinter.ACTIVE)
    Medicine = medicine_en.get(tkinter.ACTIVE)
    Quantity = quantity_en.get()
    Total_Day = tda_en.get()
    if Quantity == "" :
          print("please enter all values And Then Click Ok")
          tkinter.messagebox.showinfo("WARNING","Please Fill All Field And Then Click Ok")

    elif Total_Day == "" :
          print("please enter all values And Then Click Ok")
          tkinter.messagebox.showinfo("WARNING","Please Fill All Field And Then Click Ok")

    else:
        print(P_ID,DD,Treat,Medicine,(Quantity))
        engine1.say("Please Wait For Generate Your Bill")

        engine1.runAndWait()

        P_id = Label(bottomframe,text="Patient's ID:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
        P_id.place(x=0,y=270)
        P_id_en = Entry(bottomframe,font=("arial",9,"bold"),width=15)
        P_id_en.place(x=110,y=270)

        P_name = Label(bottomframe,text="Patient's Name:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
        P_name.place(x=240,y=270)
        P_name_en = Entry(bottomframe,font=("arial",9,"bold"),width=15)
        P_name_en.place(x=350,y=270)
        P_age = Label(bottomframe,text="Patient's Age:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
        P_age.place(x=0,y=310)
        P_age_en = Entry(bottomframe,font=("arial",9,"bold"),width=15)
        P_age_en.place(x=110,y=310)

        P_gender=Label(bottomframe,text="Patient's Gender:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
        P_gender.place(x=240,y=310)
        P_gender_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
        P_gender_en.place(x=350,y=310)

        Room_No=Label(bottomframe,text="Room No:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
        Room_No.place(x=0,y=350)
        Room_No_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
        Room_No_en.place(x=110,y=350)

        Room_Type = Label(bottomframe,text="Room Type:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
        Room_Type.place(x=240,y=350)
        Room_Type_en = Entry(bottomframe,font=("arial",9,"bold"),width=15)
        Room_Type_en.place(x=350,y=350)

        P_da = Label(bottomframe,text="Date Addmitted:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
        P_da.place(x=0,y=390)
        P_da_en = Entry(bottomframe,font=("arial",9,"bold"),width=15)
        P_da_en.place(x=110,y=390)

        P_dd = Label(bottomframe,text="Date Discharged:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
        P_dd.place(x=240,y=390)
        P_dd_en = Entry(bottomframe,font=("arial",9,"bold"),width=15)
        P_dd_en.place(x=350,y=390)

        Treatment = Label(bottomframe,text="Treatment:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
        Treatment.place(x=0,y=430)
        Treatment_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
        Treatment_en.place(x=110,y=430)
        Treatment_en.insert(END,str(Treat))

        Medicines=Label(bottomframe,text="Medicine :",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
        Medicines.place(x=240,y=430)
        Medicines_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
        Medicines_en.place(x=350,y=430)
        Medicines_en.insert(END,str(Medicine))

        tr_Price=Label(bottomframe,text="Treatment Price :",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
        tr_Price.place(x=0,y=470)
        tr_Price_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
        tr_Price_en.place(x=110,y=470)

        med_Price=Label(bottomframe,text="Medicine Price :",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
        med_Price.place(x=240,y=470)
        med_Price_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
        med_Price_en.place(x=350,y=470)

        Price=Label(bottomframe,text="Room Price :",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
        Price.place(x=0,y=510)
        Price_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
        Price_en.place(x=110,y=510)

        tmp_Price=Label(bottomframe,text="Total Medicine Price:",font=("arial",8,"bold"),fg="blue",activebackground="cyan",background="cyan")
        tmp_Price.place(x=230,y=510)
        tmp_Price_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
        tmp_Price_en.place(x=350,y=510)

        sql = "SELECT * FROM Patients_reg WHERE ID LIKE ?"
        execute = c.execute(sql, (P_ID,))
      
        for i in execute:
            print(i)
            ID = i[0]
            name = i[1]
            age = i[2]
            gender = i[3]
          
            P_id =Label(bottomframe,text="Patient's ID:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
            P_id.place(x=0,y=270)
            P_id_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
            P_id_en.place(x=110,y=270)
            P_id_en.insert(END,str(ID))

            P_name=Label(bottomframe,text="Patient's Name:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
            P_name.place(x=240,y=270)
            P_name_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
            P_name_en.place(x=350,y=270)
            P_name_en.insert(END,str(name))

            P_age=Label(bottomframe,text="Patient's Age:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
            P_age.place(x=0,y=310)
            P_age_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
            P_age_en.place(x=110,y=310)
            P_age_en.insert(END,str(age))

            P_gender=Label(bottomframe,text="Patient's Gender:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
            P_gender.place(x=240,y=310)
            P_gender_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
            P_gender_en.place(x=350,y=310)
            P_gender_en.insert(END,str(gender))

        sql1 = "SELECT * FROM  Room_allocated WHERE ID LIKE ?"
        execute = c.execute(sql1, (P_ID,))
        for i in execute:
          print(i)
          ID = i[0]
          r_type= i[1]
          r_no = i[2]
          Date_Addmitted = i[3]
          Date_Discharged = i[4]
          Room_price= i[5]

          Room_No=Label(bottomframe,text="Room No:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
          Room_No.place(x=0,y=350)
          Room_No_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
          Room_No_en.place(x=110,y=350)
          Room_No_en.insert(END,str(r_no))

          Room_Type=Label(bottomframe,text="Room Type:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
          Room_Type.place(x=240,y=350)
          Room_Type_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
          Room_Type_en.place(x=350,y=350)
          Room_Type_en.insert(END,str(r_type)) 

          P_da=Label(bottomframe,text="Date Addmitted:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
          P_da.place(x=0,y=390)
          P_da_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
          P_da_en.place(x=110,y=390)
          P_da_en.insert(END,str(Date_Addmitted))

          P_dd=Label(bottomframe,text="Date Discharged:",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
          P_dd.place(x=240,y=390)
          P_dd_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
          P_dd_en.place(x=350,y=390)
          P_dd_en.insert(END,str(Date_Discharged))

          if Room_price != "":
             Price = Label(bottomframe,text="Room Price :",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
             Price.place(x=0,y=510)
             Price_en = Entry(bottomframe,font=("arial",9,"bold"),width=15)
             Price_en.place(x=110,y=510)
             Price_en.insert(END,str(Room_price))
             print(Room_price)
             a=int(Room_price)
             print(Total_Day)
             sum1=int(Total_Day)
        
             print(sum1)
           
             t1=a*sum1
             print(f"TOTAL ROOM PRICE :{t1} ")
          if t1 != "":
           print("ok")
        if( t1==""):
          t1=0

        sql1 = "SELECT * FROM Treatment_reg  WHERE treat  LIKE  ?"
        execute = c.execute(sql1, (Treat,))
        for i in execute:
           treat_id = i[0]
           treat_price= i[1]
           print(i)
           tr_Price = Label(bottomframe,text="Treatment Price :",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
           tr_Price.place(x=0,y=470)
           tr_Price_en = Entry(bottomframe,font=("arial",9,"bold"),width=15)
           tr_Price_en.place(x=110,y=470)
           tr_Price_en.insert(END,str(treat_price))
        sql1 = "SELECT * FROM Medicine_reg  WHERE Select_Medicine  LIKE  ?"
        execute = c.execute(sql1, (Medicine,))
        for i in execute:
            med_id = i[0]
            Med_price= i[1]
            print(i)
            med_Price=Label(bottomframe,text="Medicine Price :",font=("arial",9,"bold"),fg="blue",activebackground="cyan",background="cyan")
            med_Price.place(x=240,y=470)
            med_Price_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
            med_Price_en.place(x=350,y=470)
            med_Price_en.insert(END,int(Med_price))
            a=Quantity
            (Total)=int(Quantity)*int(Med_price)
            print(int(Total))
            tmp_Price=Label(bottomframe,text="Total Medicine Price:",font=("arial",8,"bold"),fg="blue",activebackground="cyan",background="cyan")
            tmp_Price.place(x=230,y=510)
            tmp_Price_en=Entry(bottomframe,font=("arial",9,"bold"),width=15)
            tmp_Price_en.place(x=350,y=510)
            tmp_Price_en.insert(END,(Total))

        Totalprice=Button(bottomframe,text="Generate Bill :",font=("arial",14,"bold"),command=generatebill,activebackground="cyan",background="cyan",fg="blue")
        Totalprice.place(x=250,y=540)


Id=Label(bottomframe,text="Patient's ID      :",font=("arial",10,"bold"),fg="blue",activebackground="cyan",background="cyan")
Id.place(x=5,y=20)
Id_en=Entry(bottomframe,font=("arial",10,"bold"),textvariable=ID)
Id_en.place(x=180,y=20)

dd=Label(bottomframe,text="Date Discharged   :",font=("arial",10,"bold"),fg="blue",activebackground="cyan",background="cyan")
dd.place(x=5,y=60)
dd_en=Entry(bottomframe,font=("arial",10,"bold"),textvariable=DD)
dd_en.place(x=180,y=60)
button=Button(bottomframe,text="UPDATE",font=("arial",8,"bold"),command=UPDATE)
button.place(x=330,y=60)

tda=Label(bottomframe,text="Total Day Addmitted   :",font=("arial",10,"bold"),fg="blue",activebackground="cyan",background="cyan")
tda.place(x=5,y=100)
tda_en=Entry(bottomframe,font=("arial",10,"bold"),textvariable=TDA)
tda_en.place(x=180,y=100)


treat=Label(bottomframe,text="Select Treatment       :",font=("arial",10,"bold"),fg="blue",activebackground="cyan",background="cyan")
treat.place(x=5,y=140)
L=['NONE','SURGERY','LAB TEST ','CONSULATION']

treat_en=tkinter.Listbox(bottomframe,font=("arial",10,"bold"),width=15, height=1, selectmode='SINGLE', exportselection=0)
for select in L:
  treat_en.insert(tkinter.END, select)
   

treat_en.place(x=180,y=140)

# location_en.place(x=54,y=380)

medicine=Label(bottomframe,text="Select Medicine       :",font=("arial",10,"bold"),fg="blue",activebackground="cyan",background="cyan")
medicine.place(x=5,y=190)
L=['NONE','NEURAL','FANEKPLUS','DISPRRIN','PANADOL','CALPOAL','PONSTAN']

medicine_en=tkinter.Listbox(bottomframe,font=("arial",10,"bold"),width=15, height=1, selectmode='SINGLE', exportselection=0)
for select in L:
   medicine_en.insert(tkinter.END, select)
   

medicine_en.place(x=150,y=190)


quantity=Label(bottomframe,text="Quantity :",font=("arial",10,"bold"),activebackground="cyan",background="cyan",fg="blue")
quantity.place(x=280,y=190)
quantity_en=Entry(bottomframe,font=("arial",10,"bold"),width=8,textvariable=QUN)
quantity_en.place(x=350,y=190)


b1=Button(bottomframe,text="CHECK PRICE",bg="RED",font=("arial",10,"bold"),command=Check, highlightbackground="YELLOW",highlightcolor="RED",fg="white")
b1.place(x=150,y=230)


b1=Button(bottomframe,text=">>>BACK<<<",bg="RED",font=("arial",10,"bold"),command=back, highlightbackground="YELLOW",highlightcolor="RED",fg="white")
b1.place(x=20,y=230)

b1=Button(bottomframe,text=">>>NEW<<<",bg="RED",font=("arial",10,"bold"),command=new, highlightbackground="YELLOW",highlightcolor="RED",fg="white")
b1.place(x=300,y=230)

master.mainloop()
