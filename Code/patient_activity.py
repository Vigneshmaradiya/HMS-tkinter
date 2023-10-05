import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from app_main import HMS
from tkinter import font
from patient import Patient



class patient_activity(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("PATIENT-ACTIVITY")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/patient_main_activity.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

        inter_font = font.Font(family="Inter")
#-------------------------------------------------------label / buttons----------------------------------------------------------------------------------------




        self.date_var = tk.StringVar()
        self.date_entry = Entry(self,textvariable=self.date_var,font=(inter_font,25))
        self.date_entry.place(width=350,height=50,x=397,y=139)

        self.problem_var = tk.StringVar()
        problem_entry = Entry(self,textvariable=self.problem_var,font=(inter_font,25))
        problem_entry.place(width=350,height=50,x=397,y=233)

        self.medicines_var = tk.StringVar()
        medicines_entry = Entry(self,textvariable=self.medicines_var,font=(inter_font,25))
        medicines_entry.place(width=350,height=50,x=1079,y=139)

        # self.doctor_var = tk.StringVar()
        # doctor_entry = Entry(self,textvariable=self.doctor_var,font=(inter_font,25))
        # doctor_entry.place(width=350,height=50,x=1079,y=233)

        self.doctor_var = tk.StringVar()
        self.doctor_combobox = ttk.Combobox(self, textvariable=self.doctor_var, font=(inter_font, 25))
        self.doctor_combobox.place(width=350, height=50, x=1079, y=233)
        
        # Populate the doctor_combobox with doctor names
        self.populate_doctor_combobox()

        



        self.photo = ImageTk.PhotoImage(Image.open("Images/patient_activity_submit_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))

        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=55,height=40,x=30,y=30)

        self.submit_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: self.submit(self.date_var.get(),self.problem_var.get(),self.medicines_var.get(),self.doctor_var.get(),username))
        self.submit_button.place(width=218,height=68,x=671,y=338)




#-----------------------------------------------------------Tree view-------------------------------------------------------------------------------------------

        self.treeview = ttk.Treeview(self,columns=("Date","Problem","Medicines","Doctor"))

        self.treeview.heading("Date",text="Date")
        self.treeview.heading("Problem",text="Problem")
        self.treeview.heading("Medicines",text="Medicines")
        self.treeview.heading("Doctor",text="Doctor")
        

        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("Date",anchor="center",width=170)
        self.treeview.column("Problem",anchor="center",width=170)
        self.treeview.column("Medicines",anchor="center",width=170)
        self.treeview.column("Doctor",anchor="center",width=170)
        

        self.import_data()

        self.treeview.place(x=86,y=448,width=1380,height=426)


    def populate_doctor_combobox(self):
        mydb = mysql.connector.connect(host="localhost", user="root", password="Vignesh!2004#", database="hmsdb")
        mycursor = mydb.cursor()
        
        query = "SELECT username FROM doc_details"
        mycursor.execute(query)
        
        doctors = mycursor.fetchall()
        
        # Extract doctor names from the result and populate the combobox
        doctor_names = [doctor[0] for doctor in doctors]
        self.doctor_combobox['values'] = doctor_names
        
        mycursor.close()
        mydb.close()


    def import_data(self):
        
        mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
        mycursor = mydb.cursor()

        query = "SELECT date, problem, medicines, doctor FROM pat_activity"
        mycursor.execute(query)

        rows = mycursor.fetchall()

        for row in rows:
            self.treeview.insert("","end",values=row)

        mycursor.close()
        mydb.close()



    def submit(self,date, problem, medicines, doctor,username):
        if date != "" and problem != "" and medicines != "" and doctor != "":
            mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
            mycursor = mydb.cursor()

            query = "INSERT INTO pat_activity (username, date, problem, medicines, doctor) VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(query,(username, date, problem, medicines, doctor))
            mydb.commit()

            self.date_var.set('')
            self.problem_var.set('')
            self.medicines_var.set('')
            self.doctor_var.set('')
            self.date_entry.focus_set()

            self.update_treeview()


        else :
            messagebox.showerror("Error!", "All the Fields are compursory.")



    def update_treeview(self):
        self.treeview.delete(*self.treeview.get_children())
        self.import_data()



    def back_button(self,username,password):
        from patient_main import pat_Main
        self.withdraw()
        back = pat_Main(username,password)
        back.mainloop()

