import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from app_main import HMS


class Emp_pat_hist(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("DOCTOR-DASHBOARD")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/doctor_patient_history.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')


#---------------------------------------------------------------------Button-------------------------------------------------------------------------

        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))

        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=55,height=40,x=30,y=30)



#--------------------------------------------------------------------------Tree view-------------------------------------------------------------------

        self.treeview = ttk.Treeview(self,columns=("Patient","Date","Problem","Medicines"))

        self.treeview.heading("Patient",text="Patient")
        self.treeview.heading("Date",text="Date")
        self.treeview.heading("Problem",text="Problem")
        self.treeview.heading("Medicines",text="Medicines")
        

        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("Patient",anchor="center",width=170)
        self.treeview.column("Date",anchor="center",width=170)
        self.treeview.column("Problem",anchor="center",width=170)
        self.treeview.column("Medicines",anchor="center",width=170)
        

        self.import_data(username)

        self.treeview.place(x=110,y=138,width=1340,height=726)



#-----------------------------------------------------Funtions--------------------------------------------------------------------

    def import_data(self,username):
        
        mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
        mycursor = mydb.cursor()
        

        query = "SELECT p.username, p.pat_name, a.date, a.problem, a.medicines FROM pat_activity a INNER JOIN patient p ON a.username = p.username WHERE a.doctor = %s"
        mycursor.execute(query,(username,))

        rows = mycursor.fetchall()

        for row in rows:
            self.treeview.insert("","end",values=row[1:])

        mycursor.close()
        mydb.close()



    def back_button(self,username,password):
        from emp_main import Emp_Main
        self.withdraw()
        back = Emp_Main(username,password)
        back.mainloop()