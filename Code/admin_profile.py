import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from app_main import HMS
from tkinter import font



class Admin_Profile(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("ADMIN-PROFILE")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/Admin_Profile.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

        
# ------------------------------------inserting fonts --------------------------------------------------------------------   
    
        inter_font = font.Font(family="Inter")


#----------------------------------------------------------------MySQL connection --------------------------------------------
        
        mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
        mycursor = mydb.cursor()

        query = "SELECT * FROM admin_details WHERE username = %s"
        mycursor.execute(query, (username,))

        row = mycursor.fetchone()

        if row:
            username = row[0]
            name = row[1]
            age  = row[2]
            gender = row[3]
            email = row[4]
            phone = row[5]
            password = row[6]

        mycursor.close()
        mydb.close()


#--------------------------------------------- Creating Labels / Buttons --------------------------------------------------------

        username_label = tk.Label(self,text=username,font=(inter_font,36),bg="#E7F7F8")
        username_label.place(x=680,y=199)

        name_label = tk.Label(self,text=name,font=(inter_font,36),bg="#E7F7F8")
        name_label.place(x=680,y=270)

        age_label = tk.Label(self,text=age,font=(inter_font,36),bg="#E7F7F8")
        age_label.place(x=680,y=341)

        gender_label = tk.Label(self,text=gender,font=(inter_font,36),bg="#E7F7F8")
        gender_label.place(x=680,y=412)

        email_label = tk.Label(self,text=email,font=(inter_font,36),bg="#E7F7F8")
        email_label.place(x=680,y=483)

        phone_label = tk.Label(self,text=phone,font=(inter_font,36),bg="#E7F7F8")
        phone_label.place(x=680,y=554)

        password_label = tk.Label(self,text=password,font=(inter_font,36),bg="#E7F7F8")
        password_label.place(x=680,y=625)



        self.photo = ImageTk.PhotoImage(Image.open("Images/adm_pro_Edit_details_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))

        self.edit_details_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: self.edit_button(username, password))
        self.edit_details_button.place(width=230,height=65,x=665,y=836)

        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=55,height=40,x=30,y=30)

        

#--------------------------------------------------------------------Functions defined -----------------------------------------------------------------------------------

    def back_button(self,username,password):
        from admin_main import Admin_Main
        self.withdraw()
        back = Admin_Main(username,password)
        back.mainloop()


    def edit_button(self,username,password):
        from admin_profile_update import Admin_Profile_update
        self.withdraw()
        edit = Admin_Profile_update(username,password)
        edit.mainloop()

