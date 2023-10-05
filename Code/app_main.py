import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk



class HMS(tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("FITNESS CENTER")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.image = tk.PhotoImage(file='Images/Front_page_1.png')
        self.canvas.create_image(-5, 0, image=self.image, anchor='nw')

        self.protocol("WM_DELETE_WINDOW", self.Exit)
        
        
    

#----------------------------------------Buttons------------------------------------------------------------------------------------
        self.photo = ImageTk.PhotoImage(Image.open("Images/Home.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/About.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("Images/Facility.png"))
        self.photo3 = ImageTk.PhotoImage(Image.open("Images/Contact_us.png"))
        self.photo4 = ImageTk.PhotoImage(Image.open("Images/Feedback.png"))
        self.photo5 = ImageTk.PhotoImage(Image.open("Images/Admin.png"))
        self.photo6 = ImageTk.PhotoImage(Image.open("Images/Doctor.png"))
        self.photo7 = ImageTk.PhotoImage(Image.open("Images/Patient.png"))

        self.homebutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo,command=self.open_home)
        self.homebutton.place(width=312,height=52,x=1,y=186)

        self.aboutbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo1,command=self.about)
        self.aboutbutton.place(width=312,height=52,x=313,y=186)

        self.facilitybutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo2,command=self.facility)
        self.facilitybutton.place(width=312,height=52,x=625,y=186)
        
        self.contact_usbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo3,command=self.contact_us)
        self.contact_usbutton.place(width=312,height=52,x=937,y=186)

        self.feedbackbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo4,command=self.feedback)
        self.feedbackbutton.place(width=312,height=52,x=1249,y=186)
        
        self.adminbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo5,command=self.open_admin)
        self.adminbutton.place(width=392,height=92,x=884,y=421)

        self.empbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo6,command=self.open_emp)
        self.empbutton.place(width=392,height=92,x=884,y=582)

        self.patientbutton = Button(self,borderwidth=0,highlightthickness=0,image=self.photo7,command=self.open_patient)
        self.patientbutton.place(width=392,height=92,x=884,y=743)
        


#-----------------------------------------Functions for Every Buttons---------------------------------------------------------------------------------------

    def Exit(self):
        if messagebox.askyesno("Exit","Are You sure you want to exit?"):
            self.destroy()

    def open_admin(self):
        from admin import Admin
        self.withdraw()
        admin = Admin(self)
        admin.mainloop()

    def open_home(self):
        self.destroy()
        home = HMS()
        home.mainloop()
        
    def open_emp(self):
        from emp import Employee
        self.withdraw()
        emp = Employee()
        emp.mainloop()

    def open_patient(self):
        from patient import Patient
        self.withdraw()
        patient = Patient()
        patient.mainloop()


    def about(self):
        from about import About
        self.withdraw()
        about = About()
        about.mainloop()

    
    def facility(self):
        from facility import facility
        self.withdraw()
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



#---------------------------------------------------------Main App Calling part------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = HMS()
    app.mainloop()



