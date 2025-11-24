import random
import time
import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # <-- ✅ Add this line
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root
    
    
    
        self.root.title("Hospital Management System")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEfect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        
        
        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="blue",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
        
        #=====================DataFrame===================================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0, y=100, width=screen_width, height=390)
        
        
        DataFrameLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                           font=("times new roman", 12, "bold"), text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=900,height=360)
        
        DataFrameRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                           font=("times new roman", 12, "bold"), text="Prescription")
        DataFrameRight.place(x=910, y=5, width=screen_width - 910 - 20, height=360)
        
          #===============================Button Frame========================
          
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE, bg="lightgray")
        Buttonframe.place(x=0, y=500, width=screen_width, height=70)
        
        
        #===========================Frame=====================================
        
        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE)
        table_height = screen_height - 580 - 40  # Adjusted for scrollbar and padding
        DetailsFrame.place(x=0, y=580, width=screen_width, height=table_height)

        
        #==========================DataFrameLeft==============================
        
        lblNameTablet=Label(DataFrameLeft,text="Nameoftablets",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)
        
        comNametablet=ttk.Combobox(DataFrameLeft,textvariable=self.Nameoftablets,state="readonly",font=("times new roman", 12, "bold",),
                                                                                width=33)
        comNametablet.set("Select Medicine")
        comNametablet["values"]=("Panadol","Corona Vaccine","Acetamionaphen","Adderial","AmIiodipine","Ativan")
        comNametablet.grid(row=0,column=1)
        comNametablet.current(0)
        
        lablref=Label(DataFrameLeft,font=("times new roman", 12, "bold"),text="Reference No:",padx=2)
        lablref.grid(row=1,column=0,sticky="w")
        txtref=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)
        
        lblDose=Label(DataFrameLeft,font=("arial",13,"bold"),text="Dose:",padx=2,pady=6)
        lblDose.grid(row=2,column=0,sticky="w")
        txtDose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)
        
        lblNoOftablets=Label(DataFrameLeft,font=("arial",13,"bold"),text="No Of Tablets:",padx=2,pady=5)
        lblNoOftablets.grid(row=3,column=0,sticky="w")
        txtNoOFtablets=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNoOFtablets.grid(row=3,column=1)
        
        lblLot=Label(DataFrameLeft,font=("arial",13,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky="w")
        txtLot=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)
        
        lblIssueDate=Label(DataFrameLeft,font=("arial",13,"bold"),text="issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky="w")
        txtIssueDate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.Issuedate,width=35)
        txtIssueDate.grid(row=5,column=1)
        
        lblExpireDate=Label(DataFrameLeft,font=("arial",13,"bold"),text="Expire Date:",padx=2,pady=6)
        lblExpireDate.grid(row=6,column=0,sticky="w")
        txtExpireDate=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ExpDate,width=35)
        txtExpireDate.grid(row=6,column=1)
        
        lblDailyDose=Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky="w")
        txtDailyDose=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)
        
        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky="w")
        txtSideEffect=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.sideEfect,width=35)
        txtSideEffect.grid(row=8,column=1)
        
        lblFurtherInfo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Further Info:",padx=2)
        lblFurtherInfo.grid(row=0,column=2,sticky="w")
        txtFurtherInfo=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFurtherInfo.grid(row=0,column=3)
        
        lblBloodPressure=Label(DataFrameLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2)
        txtBloodPressure=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtBloodPressure.grid(row=1,column=3)
        
        lblStorage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Storage:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky="w")
        txtStorage=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=2,column=3)
        
        lblMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky="w")
        txtMedicine=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.HowToUseMedication,width=35)
        txtMedicine.grid(row=3,column=3,sticky="w")
        
        lblPatientId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient ID:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky="w")
        txtPatientId=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)
        
        lblNhsNumber=Label(DataFrameLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky="w")
        txtNhsNumber=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)
        
        lblPatientName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky="w")
        txtPatientName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.PatientName,width=35)
        txtPatientName.grid(row=6,column=3)
        
        lblDateOfBirth=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky="w")
        txtDateOfBirth=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DateOfBirth,width=35)
        txtDateOfBirth.grid(row=7,column=3)
        
        lblPatientAddress=Label(DataFrameLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky="w")
        txtPatientAddress=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)
        
        #===============================DATAFrameRight=====================
        self.txtPrescription=Text(DataFrameRight,font=("arial",12,"bold"),width=35,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
        
        #===============================Buttons============================
        

        btnPrescription = Button(Buttonframe, text="Prescription", command=self.show_prescription, bg="royalblue", fg="white", font=("arial", 12, "bold"), width=16, height=0, padx=2, pady=6)
        btnPrescription.grid(row=0,column=0)
        
        btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptionData,text="Prescription Data",bg="royalblue",fg="white",font=("arial",12,"bold"),width=16,height=0,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)
        
        btnUpdate=Button(Buttonframe,command=self.update,text="Update",bg="royalblue",fg="white",font=("arial",12,"bold"),width=16,height=0,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)
        
        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="royalblue",fg="white",font=("arial",12,"bold"),width=16,height=0,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)
        
        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="royalblue",fg="white",font=("arial",12,"bold"),width=16,height=0,padx=2,pady=6)
        btnClear.grid(row=0,column=4)
        
        btnExit=Button(Buttonframe,command=self.iExit,text="Exit",bg="royalblue",fg="white",font=("arial",12,"bold"),width=16,height=0,padx=2,pady=6)
        btnExit.grid(row=0,column=5)
        
        
        #======================================Table=====================================
        #===========================ScrollBar======
        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

        
        self.hospital_table = ttk.Treeview(DetailsFrame, columns=(
                "Nameoftablets", "ref", "dose", "Numberoftablets", "lot", "issuedate",
                    "expdate", "dailydose", "storage", "nhsnumber", "phname", "DOB", "patientaddress"),
                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)
        
        self.hospital_table.heading("Nameoftablets", text="Name of Tablets")
        self.hospital_table.heading("ref",text="Reference No")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("Numberoftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("phname",text="Patient Name")
        self.hospital_table.heading("DOB",text="DOB")
        self.hospital_table.heading("patientaddress",text="Address")
        
        self.hospital_table["show"]="headings"
        
        
        self.hospital_table.column("Nameoftablets",width=80)
        self.hospital_table.column("ref",width=80)
        self.hospital_table.column("dose",width=80)
        self.hospital_table.column("Numberoftablets",width=80)
        self.hospital_table.column("lot",width=80)
        self.hospital_table.column("issuedate",width=80)
        self.hospital_table.column("expdate",width=80)
        self.hospital_table.column("dailydose",width=80)
        self.hospital_table.column("storage",width=80)
        self.hospital_table.column("nhsnumber",width=80)
        self.hospital_table.column("phname",width=80)
        self.hospital_table.column("DOB",width=80)
        self.hospital_table.column("patientaddress",width=80)
        
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()
        #==========================Functionality Declearation=====================
    def iPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:

            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Adeelakhan123@",
                    database="mydata"
                )
                my_cursor = conn.cursor()
                
                
                my_cursor.execute("""INSERT INTO hospital(
                Nameoftablets, ref, dose, Numberoftablets, lot,
                issuedate, expdate, dailydose, storage, nhsnumber,PatientName,
                DOB, patientaddress
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)""", (
                    self.Nameoftablets.get(),
                    self.ref.get(),
                    self.Dose.get(),
                    int(self.NumberofTablets.get()),
                    self.Lot.get(),
                    self.Issuedate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvice.get(),
                    self.nhsNumber.get(),
                    self.PatientName.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get()
                )   
            )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted")
            except Exception as e:
                messagebox.showerror("Database Error", f"Error inserting data:\n{e}")

                
                
    def update(self):
        tablet_name = self.Nameoftablets.get()
        if self.Nameoftablets.get() == "Select Medicine":
            messagebox.showerror("Error", "Please select a valid tablet name.")
            return
        if tablet_name.isdigit():
            messagebox.showerror("Error", "Tablet name cannot be a number.")
            return
        if self.ref.get() == "":
            messagebox.showerror("Error", "Please select a record to update.")
            return
        tablet_name = self.Nameoftablets.get()
        if tablet_name.isdigit():
            messagebox.showerror("Error", "Tablet name cannot be a number.")
            return
        
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Adeelakhan123@", database="mydata")
            my_cursor=conn.cursor()
            update_values = (
                self.Nameoftablets.get(),
                self.Dose.get(),
                int(self.NumberofTablets.get()),  # ✅ Ensure this is cast to int
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get(),
                self.ref.get(),
                
            )
            my_cursor.execute("""UPDATE hospital SET Nameoftablets=%s,dose=%s,Numberoftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,PatientName=%s,DOB=%s,patientaddress=%s WHERE ref=%s""",update_values(
                                                                                                                self.Nameoftablets.get(),
                                                                                                                self.Dose.get(),
                                                                                                                int(self.NumberofTablets.get()),
                                                                                                                self.Lot.get(),
                                                                                                                self.Issuedate.get(),
                                                                                                                self.ExpDate.get(),
                                                                                                                self.DailyDose.get(),
                                                                                                                self.StorageAdvice.get(),
                                                                                                                self.nhsNumber.get(),
                                                                                                                self.PatientName.get(),
                                                                                                                self.DateOfBirth.get(),
                                                                                                                self.PatientAddress.get(),
                                                                                                                self.ref.get(),
                                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            print("Updating:", self.Nameoftablets.get(), "=> Table: hospital")
            messagebox.showinfo("Success", "Record has been updated")
        except Exception as e:
            messagebox.showerror("Database Error", f"Something went wrong:\n{e}")
        print("Updating:", self.Nameoftablets.get(), "=> Table: hospital")

        
                
    def fetch_data(self):
        try:
            conn=mysql.connector.connect(host="localhost",user="root",password="Adeelakhan123@",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT * FROM hospital") 
            rows=my_cursor.fetchall()
        
            if len(rows)!=0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for row in rows:
                    self.hospital_table.insert("",END,values=row)
            conn.commit()
            conn.close()
            print("Fetched rows:", rows)  # ✅ Print only after rows is defined
        except Exception as e:
            messagebox.showerror("Database Error", f"Error fetching data:\n{e}")
        
        
        
        
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        if row:
            self.Nameoftablets.set(row[0])
            self.ref.set(row[1])
            self.Dose.set(row[2])
            self.NumberofTablets.set(row[3])
            self.Lot.set(row[4])
            self.Issuedate.set(row[5])
            self.ExpDate.set(row[6])
            self.DailyDose.set(row[7])
            self.StorageAdvice.set(row[8])
            self.nhsNumber.set(row[9])
            self.PatientName.set(row[10])
            self.DateOfBirth.set(row[11])
            self.PatientAddress.set(row[12])
            print("Row selected:", row)
            
            
    def show_prescription(self):
    # Clear old prescription text
        self.txtPrescription.delete("1.0", END)

    # Insert new prescription
        self.txtPrescription.insert(END, "Nameoftablets:\t\t" + str(self.Nameoftablets.get()) + "\n")
        self.txtPrescription.insert(END, "Ref:\t\t" + str(self.ref.get()) + "\n")
        self.txtPrescription.insert(END, "Dose:\t\t" + str(self.Dose.get()) + "\n")
        self.txtPrescription.insert(END, "Number of Tablets:\t" + str(self.NumberofTablets.get()) + "\n")
        self.txtPrescription.insert(END, "Lot:\t\t" + str(self.Lot.get()) + "\n")
        self.txtPrescription.insert(END, "Issue Date:\t\t" + str(self.Issuedate.get()) + "\n")
        self.txtPrescription.insert(END, "Exp Date:\t\t" + str(self.ExpDate.get()) + "\n")
        self.txtPrescription.insert(END, "Daily Dose:\t\t" + str(self.DailyDose.get()) + "\n")
        self.txtPrescription.insert(END, "Storage Advice:\t\t" + str(self.StorageAdvice.get()) + "\n")
        self.txtPrescription.insert(END, "NHS Number:\t\t" + str(self.nhsNumber.get()) + "\n")
        self.txtPrescription.insert(END, "Patient Name:\t\t" + str(self.PatientName.get()) + "\n")
        self.txtPrescription.insert(END, "Date of Birth:\t\t" + str(self.DateOfBirth.get()) + "\n")
        self.txtPrescription.insert(END, "Patient Address:\t" + str(self.PatientAddress.get()) + "\n")
        
        #=============================Delete Button Functionally=====================================  
    def idelete(self):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]

        if not row:
            messagebox.showerror("Error", "Please select a record to delete.")
            return

        ref_no = row[1]
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?")
        if not confirm:
            return
        try: 
            conn=mysql.connector.connect(host="localhost",user="root",password="Adeelakhan123@",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("DELETE FROM hospital WHERE ref=%s", (ref_no,))
            conn.commit()
            conn.close()
            self.fetch_data()
        
            messagebox.showinfo("Delete","Patient has been deleted successfully")
        except Exception as e:
            messagebox.showerror("Database Error", f"Something went wrong:\n{e}")
            print(f"Ref to delete: '{ref_no}'")  # notice quotes to see spaces
            
            
    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.StorageAdvice.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)
        
        
    def iExit(self):
        iExit=messagebox.askyesno("Hospital Management System","Conform you want to exit")
        if iExit>0:
            root.destroy()
            return

        
        
        
        

        

        
        

    
        

root = Tk()
ob = Hospital(root)
root.mainloop()
