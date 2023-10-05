import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from app_main import HMS



class Admin_Main(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("ADMIN-DASHBOARD")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/Admin_Main.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')


#----------------------------------------------------Buttons-----------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/Admin_profile_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/Admin_doctors_button.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("Images/Admin_add_doctors_button.png"))
        self.photo3 = ImageTk.PhotoImage(Image.open("Images/Admin_edit_doctors_button.png"))
        self.photo4 = ImageTk.PhotoImage(Image.open("Images/Admin_equipments_button.png"))
        self.photo5 = ImageTk.PhotoImage(Image.open("Images/Admin_feedback_button.png"))
        self.photo6 = ImageTk.PhotoImage(Image.open("Images/Admin_logout_button.png"))


        self.adm_profile_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: self.profile(username, password))
        self.adm_profile_button.place(width=350,height=170,x=119,y=274)

        self.adm_doctors_button = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.doctors(username, password))
        self.adm_doctors_button.place(width=350,height=170,x=572,y=274)

        self.adm_add_doctor_button = Button(self,image=self.photo2,borderwidth=0,highlightthickness=0,command=lambda: self.add_doctors(username, password))
        self.adm_add_doctor_button.place(width=350,height=170,x=1025,y=274)

        self.adm_edit_doctor_button = Button(self,image=self.photo3,borderwidth=0,highlightthickness=0,command=lambda: self.edit_doctors(username, password))
        self.adm_edit_doctor_button.place(width=350,height=170,x=119,y=513)

        self.adm_feedback_button = Button(self,image=self.photo5,borderwidth=0,highlightthickness=0,command=lambda: self.feedback(username, password))
        self.adm_feedback_button.place(width=350,height=170,x=572,y=513)

        self.adm_logout_button = Button(self,image=self.photo6,borderwidth=0,highlightthickness=0,command=self.logout)
        self.adm_logout_button.place(width=350,height=170,x=1025,y=513)


# -------------------------------------------------------------- Functions ------------------------------------------------------------------

    def logout(self):
        if messagebox.askyesno("Alert","Are You sure you want to Logout?"):
           from admin import Admin
           self.withdraw()
           logout = Admin()
           logout.mainloop()

    def profile(self,username,password):
        from admin_profile import Admin_Profile
        self.withdraw()
        profile = Admin_Profile(username,password)
        profile.mainloop()

    def doctors(self,username,password):
        from admin_doctors import Admin_doctors
        self.withdraw()
        doctors = Admin_doctors(username,password)
        doctors.mainloop()

    def add_doctors(self,username,password):
        from admin_add_doctors import Admin_add_doctors
        self.withdraw()
        add_doctors = Admin_add_doctors(username,password)
        add_doctors.mainloop()

    def edit_doctors(self,username,password):
        from admin_edit_doctors import Admin_edit_doctors
        self.withdraw()
        edit_doctors = Admin_edit_doctors(username,password)
        edit_doctors.mainloop()

    def feedback(self,username,password):
        from admin_feedback import Admin_feedback
        self.withdraw()
        feedback = Admin_feedback(username,password)
        feedback.mainloop()