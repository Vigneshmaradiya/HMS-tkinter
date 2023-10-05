import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import mysql.connector
from app_main import HMS

class facility(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("FITNESS CENTER")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.image = tk.PhotoImage(file='Images/facilities.png')
        self.canvas.create_image(-5, 0, image=self.image, anchor='nw')

        self.protocol("WM_DELETE_WINDOW", self.Exit)
        
        
        inter_font = font.Font(family="Inter")

#----------------------------------------Buttons------------------------------------------------------------------------------------
        self.photo = ImageTk.PhotoImage(Image.open("Images/Home.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/About.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("Images/Facility.png"))
        self.photo3 = ImageTk.PhotoImage(Image.open("Images/Contact_us.png"))
        self.photo4 = ImageTk.PhotoImage(Image.open("Images/Feedback.png"))




        self.homebutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo,command=self.open_home)
        self.homebutton.place(width=312,height=52,x=1,y=186)

        self.aboutbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo1,command=self.about)
        self.aboutbutton.place(width=312,height=52,x=313,y=186)
    
        self.facilitybutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo2,command=self.facility)
        self.facilitybutton.place(width=312,height=52,x=625,y=186)
        
        self.contact_us_button = Button(self,borderwidth=0,highlightthickness=0,image=self.photo3,command=self.contact_us)
        self.contact_us_button.place(width=312,height=52,x=937,y=186)

        self.feedbackbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo4,command=self.feedback)
        self.feedbackbutton.place(width=312,height=52,x=1249,y=186)




    def Exit(self):
        if messagebox.askyesno("Exit","Are You sure you want to exit?"):
            self.destroy()


    def open_home(self):
        self.destroy()
        self.master.destroy()
        back = HMS()
        back.mainloop()


    def about(self):
        from about import About
        self.withdraw()
        about = About()
        about.mainloop()

    
    def facility(self):
        self.destroy()
        fac = facility()
        fac.mainloop()


    def contact_us(self):
        from contact_us import contact_us
        self.withdraw()
        contact = contact_us()
        contact.mainloop()


    def feedback(self):
        from feedback import feedback
        self.withdraw()
        feed = feedback()
        feed.mainloop()