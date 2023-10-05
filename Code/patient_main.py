import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from app_main import HMS


class pat_Main(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("PATIENT-DASHBOARD")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/patient_main_page.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')


        
#-------------------------------------------------------------Buttons-------------------------------------------------------------------------------------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/patient_main_profile_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/patient_main_activity_button.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("Images/patient_main_logout_button.png"))


        self.pat_profile_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: self.profile(username, password))
        self.pat_profile_button.place(width=382,height=170,x=589,y=222)

        self.activity_button = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.activity(username, password))
        self.activity_button.place(width=382,height=170,x=589,y=480)

        self.logout_button = Button(self,image=self.photo2,borderwidth=0,highlightthickness=0,command=self.logout)
        self.logout_button.place(width=382,height=170,x=589,y=734)



#-------------------------------------------------------Funtions----------------------------------------------------------------------------------------------------------


    def logout(self):
        if messagebox.askyesno("Alert","Are You sure you want to Logout?"):
           from patient import Patient
           self.withdraw()
           logout = Patient()
           logout.mainloop()


    def profile(self,username,password):
        from patient_profile import patient_Profile
        self.withdraw()
        profile = patient_Profile(username,password)
        profile.mainloop()


    def activity(self,username,password):
        from patient_activity import patient_activity
        self.withdraw()
        activity = patient_activity(username,password)
        activity.mainloop()