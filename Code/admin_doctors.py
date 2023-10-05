import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from app_main import HMS
import mysql.connector
from tkinter import font



class Admin_doctors(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("ADMIN-DOCTORS")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/Admin_Doctors.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

        inter_font = font.Font(family="Inter")
        
#--------------------------------------- BUTTON/ Labels ------------------------------------------------------------

        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))


        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=55,height=40,x=30,y=30)




#---------------------------------MY SQL / TREE VIEW and Data labels --------------------------------------------------
        self.treeview = ttk.Treeview(self,columns=("Username","Name","Age","Email","Gender","Phone No.","Specialization","Password"))

        self.treeview.heading("Username",text="Username")
        self.treeview.heading("Name",text="Name")
        self.treeview.heading("Age",text="Age")
        self.treeview.heading("Email",text="Email")
        self.treeview.heading("Gender",text="Gender")
        self.treeview.heading("Phone No.",text="Phone No.")
        self.treeview.heading("Specialization",text="Specialization")
        self.treeview.heading("Password",text="Password")

        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("Username",anchor="center",width=150)
        self.treeview.column("Name",anchor="center",width=150)
        self.treeview.column("Age",anchor="center",width=150)
        self.treeview.column("Email",anchor="center",width=150)
        self.treeview.column("Gender",anchor="center",width=150)
        self.treeview.column("Phone No.",anchor="center",width=150)
        self.treeview.column("Specialization",anchor="center",width=150)
        self.treeview.column("Password",anchor="center",width=150)

        self.import_data()

        self.treeview.place(x=100,y=88,width=1360,height=837)


            

#---------------------------------------------------FUNCTIONS-----------------------------------------------------------------------
    def import_data(self):
        
        mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
        mycursor = mydb.cursor()

        query = "SELECT username, name, age, email, gender, phone, specialization, password FROM doc_details"
        mycursor.execute(query)

        rows = mycursor.fetchall()

        for row in rows:
            self.treeview.insert("","end",values=row)

        mycursor.close()
        mydb.close()



    def back_button(self,username, password):
        from admin_main import Admin_Main
        self.withdraw()
        back = Admin_Main(username, password)
        back.mainloop()
