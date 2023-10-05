import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from app_main import HMS


class Emp_Main(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("DOCTOR-DASHBOARD")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/doctor_main.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')


#-------------------------------------------------------------Buttons-------------------------------------------------------------------------------------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/doctor_main_profile_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/doctor_main_pat-hist_button.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("Images/doctor_main_logout_button.png"))


        self.doc_profile_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: self.profile(username, password))
        self.doc_profile_button.place(width=382,height=170,x=589,y=222)

        self.pat_hist_button = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.pat_history(username, password))
        self.pat_hist_button.place(width=382,height=170,x=589,y=478)

        self.logout_button = Button(self,image=self.photo2,borderwidth=0,highlightthickness=0,command=self.logout)
        self.logout_button.place(width=382,height=170,x=589,y=734)



#-------------------------------------------------------Funtions----------------------------------------------------------------------------------------------------------


    def logout(self):
        if messagebox.askyesno("Alert","Are You sure you want to Logout?"):
           from emp import Employee
           self.withdraw()
           logout = Employee()
           logout.mainloop()


    def profile(self,username,password):
        from doctor_profile import doctor_Profile
        self.withdraw()
        profile = doctor_Profile(username,password)
        profile.mainloop()


    def pat_history(self,username,password):
        from doctor_pat_hist import Emp_pat_hist
        self.withdraw()
        pat_history = Emp_pat_hist(username,password)
        pat_history.mainloop()