from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox 
import tkinter.messagebox 
import mysql.connector 
 
class HospitalManagementSystem: 
     def __init__(self,root): 
          self.root=root 
          self.root.title("Hospital Management System") 
          self.root.geometry("1550x800+0+0") 
  #==========variable========= 
         self.NameofTablets_var=StringVar() 
         self.Referenceno_var=StringVar() 
         self.dose_var=StringVar() 
    self.nooftablets_var=StringVar() 
         self.issuedate_var=StringVar() 
         self.expirydate_var=StringVar() 
         self.dailydose_var=StringVar() 
         self.sideeffect_var=StringVar() 
         self.bloodpressure_var=StringVar() 
         self.storagedevice_var=StringVar() 
         self.medication_var=StringVar() 
self.patientid_var=StringVar() 
self.nameofpatient_var=StringVar() 
self.dob_var=StringVar() 
self.patientaddress_var=StringVar() 
lbltitle=Label(self.root,text="HOSPITAL MANAGEMENT 
SYSTEM",bg="blue",fg="white",bd=20,relief=RIDGE,font=("times new 
roman",50,"bold"),padx=2,pady=6) 
lbltitle.pack(side=TOP,fill=X) 
Dataframe=Frame(self.root,bd=20,relief=RIDGE,padx=20,bg="pink") 
Dataframe.place(x=0,y=130,width=1440,height=400) 
#===========DataFrameLeft========== 
DataFrameLeft=LabelFrame(Dataframe,text="PATIENT 
INFORMATION",bg="pink",fg="black",bd=12,relief=RIDGE,font=("times new 
roman",12,"bold")) 
DataFrameLeft.place(x=0,y=5,width=850,height=350) 
lblNameofTablets=Label(DataFrameLeft,bg="pink",text="Name of 
Tablets:",font=("arial",12,"bold"),padx=2,pady=6) 
lblNameofTablets.grid(row=0,column=0,sticky=W) 
txtNameofTablets=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29) 
txtNameofTablets.grid(row=1,column=1) 
comNameofTablet=ttk.Combobox(DataFrameLeft,textvariable=self.NameofTablets_var,font
 =("arial",12,"bold"),width=27,state="readonly") 
comNameofTablet["value"]=("Nice","Corona 
Vacacine","Acetaninophen","Adderall","Ativan","Anlodipine") 
comNameofTablet.current(0) 
comNameofTablet.grid(row=0,column=1) 
lblref=Label(DataFrameLeft,bg="pink",text="Reference 
No:",font=("arial",12,"bold"),padx=2,pady=6) 

lblref.grid(row=1,column=0,sticky=W) 
txtref=Entry(DataFrameLeft,textvariable=self.Referenceno_var,font=("arial",12,"bold"),widt
 h=29) 
txtref.grid(row=1,column=1) 
lblDose=Label(DataFrameLeft,bg="pink",text="Dose:",font=("arial",12,"bold"),padx=2,pady=
 6) 
lblDose.grid(row=2,column=0,sticky=W) 
txtDose=Entry(DataFrameLeft,textvariable=self.dose_var,font=("arial",12,"bold"),width=29) 
txtDose.grid(row=2,column=1) 
lblNoofTablets=Label(DataFrameLeft,bg="pink",text="No of 
Tablets:",font=("arial",12,"bold"),padx=2,pady=6) 
lblNoofTablets.grid(row=3,column=0,sticky=W) 
txtNoofTablets=Entry(DataFrameLeft,textvariable=self.nooftablets_var,font=("arial",12,"bo
 ld"),width=29)txtNoofTablets.grid(row=3,column=1)lblIssueDate=Label(DataFrameLeft,bg="
 pink",text="Issue Date:",font=("arial",12,"bold"),padx=2,pady=6) 
lblIssueDate.grid(row=4,column=0,sticky=W)txtIssueDate=Entry(DataFrameLeft,textvariable
 =self.issuedate_var,font=("arial",12,"bold"),width=29) 
txtIssueDate.grid(row=4,column=1) 
lblExpiryDate=Label(DataFrameLeft,bg="pink",text="Expiry 
Date:",font=("arial",12,"bold"),padx=2,pady=6) 
lblExpiryDate.grid(row=5,column=0,sticky=W) 
txtExpiryDate=Entry(DataFrameLeft,textvariable=self.expirydate_var,font=("arial",12,"bold"
 ),width=29) 
txtExpiryDate.grid(row=5,column=1) 
lblDailyDose=Label(DataFrameLeft,bg="pink",text="Daily 
Dose:",font=("arial",12,"bold"),padx=2,pady=6) 
lblDailyDose.grid(row=6,column=0,sticky=W) 
txtDailyDose=Entry(DataFrameLeft,textvariable=self.dailydose_var,font=("arial",12,"bo
 ld"),width=29) 

 
          txtDailyDose.grid(row=6,column=1) 
          lblSideeffect=Label(DataFrameLeft,bg="pink",text="Side 
Effect:",font=("arial",12,"bold"),padx=2,pady=6) 
          lblSideeffect.grid(row=7,column=0,sticky=W) 
          txtSideeffect=Entry(DataFrameLeft,textvariable=self.sideeffect_var,font=("arial",12,"b
 old"),width=29) 
          txtSideeffect.grid(row=7,column=1) 
          lblBloodPressure=Label(DataFrameLeft,bg="pink",text="Blood 
Pressure:",font=("arial",12,"bold"),padx=2,pady=6) 
          lblBloodPressure.grid(row=8,column=0,sticky=W) 
          txtBloodPressure=Entry(DataFrameLeft,textvariable=self.bloodpressure_var,font=("ari
 al",12,"bold"),width=29) 
          txtBloodPressure.grid(row=8,column=1) 
          lblStorageDevice=Label(DataFrameLeft,bg="pink",text="Storage 
Device:",font=("arial",12,"bold"),padx=2,pady=6) 
          lblStorageDevice.grid(row=0,column=2,sticky=W) 
          txtStorageDevice=Entry(DataFrameLeft,textvariable=self.storagedevice_var,font
 =("arial",12,"bold"),width=29) 
          txtStorageDevice.grid(row=0,column=3) 
          lblMedication=Label(DataFrameLeft,bg="pink",text="Medication:",font=("arial",12,"bo
 ld"),padx=2,pady=6) 
          lblMedication.grid(row=1,column=2,sticky=W) 
          txtMedication=Entry(DataFrameLeft,textvariable=self.medication_var,font=("arial",12,
 "bold"),width=29) 
          txtMedication.grid(row=1,column=3) 
          lblPatientid=Label(DataFrameLeft,bg="pink",text="Patient 
Id:",font=("arial",12,"bold"),padx=2,pady=6) 
          lblPatientid.grid(row=2,column=2,sticky=W) 

 
          txtPatientid=Entry(DataFrameLeft,textvariable=self.patientid_var,font=("arial",12,"bol
 d"),width=29) 
          txtPatientid.grid(row=2,column=3) 
          lblNameofPatient=Label(DataFrameLeft,bg="pink",text="Name of 
Patient:",font=("arial",12,"bold"),padx=2,pady=6) 
          lblNameofPatient.grid(row=3,column=2,sticky=W) 
          txtNameofPatient=Entry(DataFrameLeft,textvariable=self.nameofpatient_var,fo
 nt=("arial",12,"bold"),width=29) 
          txtNameofPatient.grid(row=3,column=3) 
          lblDob=Label(DataFrameLeft,bg="pink",text="DOB:",font=("arial",12,"bold"),padx=2,p
 ady=6) 
          lblDob.grid(row=4,column=2,sticky=W) 
          txtDob=Entry(DataFrameLeft,textvariable=self.dob_var,font=("arial",12,"bold"),width=
 29) 
          txtDob.grid(row=4,column=3) 
          lblPatientaddress=Label(DataFrameLeft,bg="pink",text="Patient 
Address:",font=("arial",12,"bold"),padx=2,pady=6) 
          lblPatientaddress.grid(row=5,column=2,sticky=W) 
          txtPatientaddress=Entry(DataFrameLeft,textvariable=self.patientaddress_var,font=("ar
 ial",12,"bold"),width=29) 
          txtPatientaddress.grid(row=5,column=3) 
          
 
          #==========DataFrameRight=========== 
          DataFrameRight=LabelFrame(Dataframe,text="PRESCRIPTION",bg="pink",fg="black",b
 d=12,relief=RIDGE,font=("times new roman",12,"bold")) 
          DataFrameRight.place(x=850,y=5,width=520,height=350) 

 
          self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),width=54,height=16,
 padx=1,pady=4,bg="pink") 
          self.txtPrescription.grid(row=0,column=0) 
 
          
          # ============Buttons frame============= 
          Framebutton=Frame(self.root,bd=20,relief=RIDGE,bg="powder blue") 
          Framebutton.place(x=0,y=530,width=1440,height=70) 
          btnPrescription=Button(Framebutton,command=self.iPresciptionData,text="Prescripti
 on",font=("arial",12,"bold"),width=23,bg="green",fg="white") 
          btnPrescription.grid(row=0,column=0) 
          btnPrescriptiondata=Button(Framebutton,command=self.iPrescription,text="Prescripti
 on Data",font=("arial",12,"bold"),width=23,bg="green",fg="white") 
          btnPrescriptiondata.grid(row=0,column=1) 
          btnupdate=Button(Framebutton,command=self.update,text="Update",font=("arial",12
 ,"bold"),width=23,bg="green",fg="white") 
          btnupdate.grid(row=0,column=2) 
          btndelete=Button(Framebutton,command=self.delete,text="Delete",font=("aria
 l",12,"bold"),width=23,bg="green",fg="white") 
          btndelete.grid(row=0,column=3) 
          btnclear=Button(Framebutton,command=self.clear,text="Clear",font=("arial",12,"bold
 "),width=23,bg="green",fg="white") 
          btnclear.grid(row=0,column=4) 
          btnexit=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),
 width=23,bg="green",fg="white") 
          btnexit.grid(row=0,column=5) 
          # ============Information Frame============= 

 
          Detailsframe=Frame(self.root,bd=20,relief=RIDGE,bg="powder blue") 
          Detailsframe.place(x=0,y=600,width=1440,height=290) 
 
          Table_frame=Frame(Detailsframe,bd=6,relief=RIDGE,bg="powder blue") 
          Table_frame.place(x=0,y=2,width=1460,height=260) 
          xscroll=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL) 
          yscroll=ttk.Scrollbar(Detailsframe,orient=VERTICAL) 
           
          self.hospital1_table=ttk.Treeview(Detailsframe,column=("NameofTablets","Reference
 no","dose","nooftablets","issuedate","expirydate","dailydose","sideeffect","bloodpressure",
 "storagedevice","medication","patientid","nameofpatient","dob","patientaddress"),xscrollc
 ommand=xscroll.set,yscrollcommand=yscroll.set) 
          xscroll.pack(side=BOTTOM,fill=X) 
          yscroll.pack(side=RIGHT,fill=Y) 
          xscroll.config(command=self.hospital1_table.xview) 
          yscroll.config(command=self.hospital1_table.yview) 
          
          self.hospital1_table.heading("NameofTablets",text="Name of Tablets") 
          self.hospital1_table.heading("Referenceno",text="Reference No") 
          self.hospital1_table.heading("dose",text="Dose") 
          self.hospital1_table.heading("nooftablets",text="No of Tablets") 
          self.hospital1_table.heading("issuedate",text="Issue Date") 
          self.hospital1_table.heading("expirydate",text="Expiry Date") 
          self.hospital1_table.heading("dailydose",text="Daily Dose") 
          self.hospital1_table.heading("sideeffect",text="Side Effect") 
          self.hospital1_table.heading("bloodpressure",text="Blood Pressure") 

 
          self.hospital1_table.heading("storagedevice",text="Storage Device") 
          self.hospital1_table.heading("medication",text="Medication") 
          self.hospital1_table.heading("patientid",text="Patient Id") 
          self.hospital1_table.heading("nameofpatient",text="Name of Patient") 
          self.hospital1_table.heading("dob",text="DOB") 
          self.hospital1_table.heading("patientaddress",text="Patient Address") 
 
          self.hospital1_table["show"]="headings" 
          self.hospital1_table.pack(fill=BOTH,expand=1) 
          self.hospital1_table.column("NameofTablets",width=100) 
          self.hospital1_table.column("Referenceno",width=100) 
          self.hospital1_table.column("dose",width=100) 
          self.hospital1_table.column("nooftablets",width=100) 
          self.hospital1_table.column("issuedate",width=100) 
          self.hospital1_table.column("expirydate",width=100) 
          self.hospital1_table.column("dailydose",width=100) 
          self.hospital1_table.column(“sideeffect”,width=100) 
          self.hospital1_table.column(“bloodpressure”,width=100) 
           self.hospital1_table.column("storagedevice",width=100) 
          self.hospital1_table.column("medication",width=100) 
          self.hospital1_table.column("patientid",width=100) 
          self.hospital1_table.column("nameofpatient",width=100) 
          self.hospital1_table.column("dob",width=100) 
          self.hospital1_table.column("patientaddress",width=100)  
 
 
 
      
          self.fetch_data() 
          self.hospital1_table.bind("<ButtonRelease-1>",self.get_cursor) 
  #------------------------------------------functionality declaration--------------------------------------------- 
     def iPresciptionData(self): 
conn=mysql.connector.connect(host="localhost",username="root",password="geetha123",
 database="mydata1") 
 my_cursor=conn.cursor() 
 my_cursor.execute("insert into hospital1 
values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                       self.NameofTablets_var.get(), 
                                                                                                        self.Referenceno_var.get(), 
                                                                                                        self.dose_var.get(), 
                                                                                                        self.nooftablets_var.get(), 
                                                                                                        self.issuedate_var.get(), 
                                                                                                        self.expirydate_var.get(), 
                                                                                                        self.dailydose_var.get(), 
                                                                                                        self.sideeffect_var.get(), 
                                                                                                        self.bloodpressure_var.get(), 
                                                                                                        self.storagedevice_var.get(), 
                                                                                                        self.medication_var.get(), 
                                                                                                        self.patientid_var.get(), 
                                               self.nameofpatient_var.get(), 
                                                                                                        self.dob_var.get(), 

 
                                                                                                        self.patientaddress_var.get() 
                                                                                                          )) 
            conn.commit() 
            self.fetch_data() 
            conn.close() messagebox.showinfo("Success","Record has been inserted") 
     def update(self): 
conn=mysql.connector.connect(host="localhost",username="root",password="geetha123",
 database="mydata1") 
               my_cursor=conn.cursor() 
               my_cursor.execute("update hospital1 set 
NameofTablets=%s,dose=%s,nooftablets=%s,issuedate=%s,expirydate=%s,dailydose=%s,sid
 eeffect=%s,bloodpressure=%s,storagedevice=%s,medication=%s,patientid=%s,nameofpatie
 nt=%s,dob=%s,patientaddress=%s where Referenceno=%s",( 
                                                                                                                self.NameofTablets_var.get(),                          
                                                                                                                self.dose_var.get(), 
                                                                                                                self.nooftablets_var.get(), 
                                                                                                                 self.issuedate_var.get(), 
                                                                                                                 self.expirydate_var.get(), 
                                                                                                                 self.dailydose_var.get(), 
                                                                                                                 self.sideeffect_var.get(), 
                                                                                                                 self.bloodpressure_var.get(), 
                                                                                                                  self.storagedevice_var.get(), 
                                                                                                                  self.medication_var.get(), 
                                                                                                                  self.patientid_var.get(), 
                                                                                                                 self.nameofpatient_var.get(), 
                                                                                                                 self.dob_var.get(), 

 
                                                                                                                 self.patientaddress_var.get(), 
                                                                                                           self.Referenceno_var.get(),       )) 
               conn.commit() 
               self.fetch_data() 
               conn.close() 
  messagebox.showinfo("Success","Member has been updated”) 
def fetch_data(self): 
 conn=mysql.connector.connect(host="localhost",username="root",password="geetha123",
 database="mydata1") 
 my_cursor=conn.cursor()              
 my_cursor.execute("select * from hospital1") 
  rows=my_cursor.fetchall() 
             if len(rows)!=0: 
                    self.hospital1_table.delete(*self.hospital1_table.get_children()) 
                    for i in rows: 
                         self.hospital1_table.insert("",END,values=i) 
                    conn.commit() 
               conn.close()  
def get_cursor(self,event=""): 
       cursor_column=self.hospital1_table.focus() 
               content=self.hospital1_table.item(cursor_column) 
               column=content['values'] 
              self.NameofTablets_var.set(column[0]) 
               self.Referenceno_var.set(column[1]) 
               self.dose_var.set(column[2]) 

 
               self.nooftablets_var.set(column[3]) 
               self.issuedate_var.set(column[4]) 
               self.expirydate_var.set(column[5]) 
               self.dailydose_var.set(column[6]) 
               self.sideeffect_var.set(column[7]) 
               self.bloodpressure_var.set(column[8]) 
               self.storagedevice_var.set(column[9]) 
               self.medication_var.set(column[10]) 
               self.patientid_var.set(column[11]) 
               self.nameofpatient_var.set(column[12]) 
               self.dob_var.set(column[13]) 
               self.patientaddress_var.set(column[14]) 
                 def iPrescription(self) 
self.txtPrescription.insert(END,"Name of Tablets:\t\t\t"+self.NameofTablets_var.get() +"\n")  
  self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.Referenceno_var.get() +"\n")  
  self.txtPrescription.insert(END,"Dose\t\t\t"+self.dose_var.get() +"\n")  
  self.txtPrescription.insert(END,"No.of Tablets\t\t\t"+self.nooftablets_var.get() +"\n")  
  self.txtPrescription.insert(END,"Issue Date\t\t\t"+self.issuedate_var.get() +"\n")  
  self.txtPrescription.insert(END,"Expiry Date\t\t\t"+self.expirydate_var.get() +"\n")  
  self.txtPrescription.insert(END,"Daily Dose\t\t\t"+self.dailydose_var.get() +"\n")  
  self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideeffect_var.get() +"\n")  
  self.txtPrescription.insert(END,"Blood Pressure\t\t\t"+self.bloodpressure_var.get() +"\n")  
  self.txtPrescription.insert(END,"Storage Device\t\t\t"+self.storagedevice_var.get() +"\n")  
  self.txtPrescription.insert(END,"Medication\t\t\t"+self.medication_var.get() +"\n")  
   self.txtPrescription.insert(END,"Patient Id\t\t\t"+self.patientid_var.get() +"\n")  
self.txtPrescription.insert(END,"Name of Patient\t\t\t"+self.nameofpatient_var.get() +"\n") 
self.txtPrescription.insert(END,"DOB\t\t\t"+self.dob_var.get() +"\n") 
self.txtPrescription.insert(END,"Patient Address\t\t\t"+self.patientaddress_var.get() +"\n") 
def delete(self): 
conn=mysql.connector.connect(host="localhost",username="root",password="geetha123",
 database="mydata1") 
my_cursor=conn.cursor() 
query="delete from  hospital1 where referenceno=%s" 
value=(self.Referenceno_var.get(),) 
my_cursor.execute(query,value) 
conn.commit()  
self.fetch_data() 
conn.close() 
messagebox.showinfo("Success","Member has been deleted") 
def clear(self): 
self.NameofTablets_var.set(""),   
self.Referenceno_var.set(""), 
self.dose_var.set(""), 
self.nooftablets_var.set(""),  
self.issuedate_var.set(""), 
self.expirydate_var.set(""),                    
self.dailydose_var.set(""), 
self.sideeffect_var.set(""),  
self.bloodpressure_var.set(""),                
self.storagedevice_var.set(""),  
self.medication_var.set(""), 

 
self.patientid_var.set(""),  
self.nameofpatient_var.set(""),  
self.dob_var.set(""),  
self.patientaddress_var.set(""),  
self.txtPrescription.delete("1.0",END) 
 
 def iExit(self): 
               iExit= tkinter.messagebox.askyesno("Hospital Management System","Do you want 
to exit")   
               if iExit>0: 
                    self.root.destroy() 
                    return        
if __name__ == "__main__": 
      root=Tk() 
      obj=HospitalManagementSystem(root) 
      root.mainloop()
