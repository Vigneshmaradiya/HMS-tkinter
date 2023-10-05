import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from app_main import HMS


class Admin(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("ADMIN LOGIN")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/Admin_Login_page.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

        



#-------------------------------Entry Box-------------------------------------------------------------------------------------------------------------------------------------

        username_var = tk.StringVar()
        username_entry = Entry(self,textvariable=username_var,font=("Roboto",25))
        username_entry.place(width=524,height=78,x=509,y=391)

        passwrd_var = tk.StringVar()
        passwrd_entry = Entry(self,show="*",textvariable=passwrd_var,font=("Roboto",25))
        passwrd_entry.place(width=524,height=78,x=509,y=544)

#----------------------------------------------------Buttons---------------------------------------------------------------------------------------------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/adm_login_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))


        self.loginbutton = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: authenticate(username_entry.get(),passwrd_entry.get()))
        self.loginbutton.place(width=218,height=65,x=661,y=730)

        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=self.back_button)
        self.backbutton.place(width=55,height=40,x=30,y=30)
        
        global username
        username = username_entry.get()
        global password
        password = passwrd_entry.get()
#----------------------------------------------------SQL DATABASE CONNECTION--------------------------------------------------------------------------------------------------------
        

        def authenticate(username,password):

            mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM admin WHERE username = %s AND password = %s", (username, password))

            res = mycursor.fetchone()
            if res: 
                messagebox.showinfo("Login", "Login successful!")
                mycursor.close()
                mydb.close()
                self.login_button(username,password)


            else:
                messagebox.showwarning("Login", "Invalid username or password!")

#-------------------------------------------------------------defined functions-------------------------------------------------------------------------------------------------




    def back_button(self):
        self.destroy()
        self.master.destroy()
        back = HMS()
        back.mainloop()

    def login_button(self,username,password):
        from admin_main import Admin_Main
        self.withdraw()
        login = Admin_Main(username,password)
        login.mainloop()
        