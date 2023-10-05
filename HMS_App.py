import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from tkinter import font


class HMS(tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("HEALTH CENTER")

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
        self.withdraw()
        admin = Admin(self)
        admin.mainloop()

    def open_home(self):
        self.destroy()
        home = HMS()
        home.mainloop()
        
    def open_emp(self):
        self.withdraw()
        emp = Employee()
        emp.mainloop()

    def open_patient(self):
        self.withdraw()
        patient = Patient()
        patient.mainloop()


    def about(self):
        self.withdraw()
        about = About()
        about.mainloop()

    
    def facility(self):
        self.withdraw()
        fac = facility()
        fac.mainloop()


    def contact_us(self):
        self.withdraw()
        contact = contact_us()
        contact.mainloop()
        

    def feedback(self):
        self.withdraw()
        feed = feedback()
        feed.mainloop()


#=========================================================================about.py================================================================================

class About(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("HEALTH CENTER")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.image = tk.PhotoImage(file='Images/about_page.png')
        self.canvas.create_image(-5, 0, image=self.image, anchor='nw')

        self.protocol("WM_DELETE_WINDOW", self.Exit)
        
        
    

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
        self.destroy()
        about = About()
        about.mainloop()

    
    def facility(self):
        self.withdraw()
        fac = facility()
        fac.mainloop()


    def contact_us(self):
        self.withdraw()
        contact = contact_us()
        contact.mainloop()


    def feedback(self):
        self.withdraw()
        feed = feedback()
        feed.mainloop()


#=======================================================================facility.py===============================================================================

class facility(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("HEALTH CENTER")

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
        self.withdraw()
        about = About()
        about.mainloop()

    
    def facility(self):
        self.destroy()
        fac = facility()
        fac.mainloop()


    def contact_us(self):
        self.withdraw()
        contact = contact_us()
        contact.mainloop()


    def feedback(self):
        self.withdraw()
        feed = feedback()
        feed.mainloop()


#=======================================================================contact_us.py============================================================================

class contact_us(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)


        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("HEALTH CENTER")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.image = tk.PhotoImage(file='Images/contact_us_page.png')
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
        self.withdraw()
        about = About()
        about.mainloop()

    
    def facility(self):
        self.withdraw()
        fac = facility()
        fac.mainloop()


    def contact_us(self):
        self.destroy()
        contact = contact_us()
        contact.mainloop()


    def feedback(self):
        self.withdraw()
        feed = feedback()
        feed.mainloop()


#========================================================================feedback.py=============================================================================

class feedback(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("HEALTH CENTER")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.image = tk.PhotoImage(file='Images/Feedback_page.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

        self.protocol("WM_DELETE_WINDOW", self.Exit)
        
        
        inter_font = font.Font(family="Inter")

#----------------------------------------Buttons------------------------------------------------------------------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/submit_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))

        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=self.back_button)
        self.backbutton.place(width=55,height=40,x=30,y=30)


        self.name_var = tk.StringVar()
        self.name_entry = Entry(self,textvariable=self.name_var,font=(inter_font,25))
        self.name_entry.place(width=600,height=72,x=668,y=259)

        self.email_var = tk.StringVar()
        email_entry = Entry(self,textvariable=self.email_var,font=(inter_font,25))
        email_entry.place(width=600,height=72,x=668,y=356)

        self.feedback_var = tk.StringVar()
        feedback_entry = Entry(self,textvariable=self.feedback_var,font=(inter_font,25))
        feedback_entry.place(width=600,height=294,x=668,y=453)



        self.submit_button = Button(self,borderwidth=0,highlightthickness=0,image=self.photo,command=self.submit_feedback)
        self.submit_button.place(width=274, height=77, x=643, y=791)




    def submit_feedback(self):
        name = self.name_var.get()
        email = self.email_var.get()
        feedback = self.feedback_var.get()

        if name and email and feedback:
            # Insert the values into the feedback table
            mydb = mysql.connector.connect(host="localhost", user="root", password="Vignesh!2004#", database="hmsdb")
            mycursor = mydb.cursor()

            query = "INSERT INTO feedback (name, email, feedback) VALUES (%s, %s, %s)"
            values = (name, email, feedback)
            mycursor.execute(query, values)

            mydb.commit()
            mycursor.close()
            mydb.close()

            # Clear the entry boxes
            self.name_var.set("")
            self.email_var.set("")
            self.feedback_var.set("")

            messagebox.showinfo("Success", "Feedback submitted successfully!")
        else:
            messagebox.showerror("Error", "Please enter all the values.")




    def Exit(self):
        if messagebox.askyesno("Exit","Are You sure you want to exit?"):
            self.destroy()


    def back_button(self):
        self.master.destroy()
        home = HMS()
        home.mainloop()


#=========================================================================admin.py================================================================================

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
        self.withdraw()
        login = Admin_Main(username,password)
        login.mainloop()


#========================================================================admin_main.py===========================================================================

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
           self.withdraw()
           logout = Admin()
           logout.mainloop()

    def profile(self,username,password):
        self.withdraw()
        profile = Admin_Profile(username,password)
        profile.mainloop()

    def doctors(self,username,password):
        self.withdraw()
        doctors = Admin_doctors(username,password)
        doctors.mainloop()

    def add_doctors(self,username,password):
        self.withdraw()
        add_doctors = Admin_add_doctors(username,password)
        add_doctors.mainloop()

    def edit_doctors(self,username,password):
        self.withdraw()
        edit_doctors = Admin_edit_doctors(username,password)
        edit_doctors.mainloop()

    def feedback(self,username,password):
        self.withdraw()
        feedback = Admin_feedback(username,password)
        feedback.mainloop()


#=======================================================================admin_profile.py=========================================================================

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
        self.withdraw()
        back = Admin_Main(username,password)
        back.mainloop()


    def edit_button(self,username,password):
        self.withdraw()
        edit = Admin_Profile_update(username,password)
        edit.mainloop()


#===================================================================admin_profile_update.py======================================================================

class Admin_Profile_update(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("ADMIN-PROFILE (UPDATE)")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/Admin_Profile_Edit.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')


        inter_font = font.Font(family="Inter")
#-------------------------------------------------------------- Entry box / button ---------------------------------------------------------------

        self.username_var = tk.StringVar()
        username_entry = Entry(self,textvariable=self.username_var,font=(inter_font,25),state="readonly")
        username_entry.place(width=530,height=50,x=677,y=206)

        self.name_var = tk.StringVar()
        name_entry = Entry(self,textvariable=self.name_var,font=(inter_font,25))
        name_entry.place(width=530,height=50,x=677,y=277)

        self.age_var = tk.StringVar()
        age_entry = Entry(self,textvariable=self.age_var,font=(inter_font,25))
        age_entry.place(width=530,height=50,x=677,y=348)

        self.gender_var = tk.StringVar()
        gender_entry = Entry(self,textvariable=self.gender_var,font=(inter_font,25))
        gender_entry.place(width=530,height=50,x=677,y=419)

        self.email_var = tk.StringVar()
        email_entry = Entry(self,textvariable=self.email_var,font=(inter_font,25))
        email_entry.place(width=530,height=50,x=677,y=490)

        self.phone_var = tk.StringVar()
        phone_entry = Entry(self,textvariable=self.phone_var,font=(inter_font,25))
        phone_entry.place(width=530,height=50,x=677,y=561)

        self.passwrd_var = tk.StringVar()
        passwrd_entry = Entry(self,textvariable=self.passwrd_var,font=(inter_font,25))
        passwrd_entry.place(width=530,height=50,x=677,y=632)


        self.photo = ImageTk.PhotoImage(Image.open("Images/adm_pro_Save_details_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))

        self.save_detail_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=self.save_details)
        self.save_detail_button.place(width=230,height=65,x=665,y=843)

        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=55,height=40,x=30,y=30)

#------------------------------------------------------mysql connection----------------------------------------------------------

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

        self.username_var.set(username)
        self.name_var.set(name)
        self.age_var.set(age)
        self.gender_var.set(gender)
        self.email_var.set(email)
        self.phone_var.set(phone)
        self.passwrd_var.set(password)

#-----------------------------------------------------------function define -----------------------------------------------------------------

    def save_details(self):
        username = self.username_var.get()
        name = self.name_var.get()
        age = self.age_var.get()
        gender = self.gender_var.get()
        email = self.email_var.get()
        phone = self.phone_var.get()
        password = self.passwrd_var.get()
            
        if name == "":
            name = None
        if age == "":
            age = None
        if gender == "":
            gender = None
        if email == "":
            email = None
        if phone == "":
            phone = None
        if password == "":
            password = None

        mydb = mysql.connector.connect(host="localhost", user="root", password="Vignesh!2004#", database="hmsdb")
        mycursor = mydb.cursor()

        a = b = 1  
        try:
            query = "UPDATE admin_details SET Name = %s, gender = %s, email = %s, password = %s WHERE username = %s"
            mycursor.execute(query, (name, gender, email, password, username))

            query = "UPDATE admin SET password = %s WHERE username = %s"
            mycursor.execute(query,(password,username))


            mydb.commit()

        except mysql.connector.Error as err:
            print(f"Error inserting mobile number: {err}")
        
        if age.isnumeric() and len(age) < 4:
            try:
                query = "UPDATE admin_details SET age = %s WHERE username = %s"
                mycursor.execute(query, (age,username))

                mydb.commit()

            except mysql.connector.Error as err:
                print(f"Error inserting mobile number: {err}")

        else:
            if age != 'None':
                a = 0
                messagebox.showerror("Error!", "Age is Invalid.")

        if (len(phone) == 10 and phone.isnumeric()):
            try:
                query = "UPDATE admin_details SET phone = %s WHERE username = %s"
                mycursor.execute(query, (phone,username))

                mydb.commit()

            except mysql.connector.Error as err:
                print(f"Error inserting mobile number: {err}")

        else:
            if phone != 'None':
                b = 0
                messagebox.showerror("Error!", "Phone number is Invalid.")

        if (a == 1 and b == 1):
            messagebox.showinfo("Update", "Profile details updated successfully!")
            
        mydb.commit()

        mycursor.close()
        mydb.close()


        self.withdraw()
        save = Admin_Profile(username,password)
        save.mainloop()

    
    def back_button(self,username,password):
        self.withdraw()
        back = Admin_Profile(username,password)
        back.mainloop()


#=======================================================================admin_doctors.py=========================================================================

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
        self.withdraw()
        back = Admin_Main(username, password)
        back.mainloop()


#=====================================================================admin_add_doctors.py=======================================================================

class Admin_add_doctors(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("ADMIN-ADD DOCTORS")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/Admin_add_doctors.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

        inter_font = font.Font(family="Inter")
        
#--------------------------------------- BUTTON/ Labels ------------------------------------------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/admin_add_doctors_Add-details_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))


        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=55,height=40,x=30,y=30)

        self.add_details_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: authenticate(self.name_entry.get(),age_entry.get(),gender_entry.get(),email_entry.get(),phone_entry.get(),specialization_entry.get(),passwrd_entry.get(),username_entry.get()))
        self.add_details_button.place(width=230,height=65,x=1044,y=330)



        self.name_var = tk.StringVar()
        self.name_entry = Entry(self,textvariable=self.name_var,font=(inter_font,25))
        self.name_entry.place(width=336,height=50,x=450,y=93)

        self.age_var = tk.StringVar()
        age_entry = Entry(self,textvariable=self.age_var,font=(inter_font,25))
        age_entry.place(width=336,height=50,x=450,y=170)


        self.gender_var = tk.StringVar()
        gender_entry = Entry(self,textvariable=self.gender_var,font=(inter_font,25))
        gender_entry.place(width=336,height=50,x=450,y=246)

        self.email_var = tk.StringVar()
        email_entry = Entry(self,textvariable=self.email_var,font=(inter_font,25))
        email_entry.place(width=336,height=50,x=450,y=322)

        self.phone_var = tk.StringVar()
        phone_entry = Entry(self,textvariable=self.phone_var,font=(inter_font,25))
        phone_entry.place(width=336,height=50,x=450,y=397)

        self.specialization_var = tk.StringVar()
        specialization_entry = Entry(self,textvariable=self.specialization_var,font=(inter_font,25))
        specialization_entry.place(width=336,height=50,x=1106,y=93)

        self.passwrd_var = tk.StringVar()
        passwrd_entry = Entry(self,textvariable=self.passwrd_var,font=(inter_font,25))
        passwrd_entry.place(width=336,height=50,x=1106,y=170)

        self.username_var = tk.StringVar()
        username_entry = Entry(self,textvariable=self.username_var,font=(inter_font,25))
        username_entry.place(width=336,height=50,x=1106,y=246)



        self.treeview = ttk.Treeview(self,columns=("Username","Name","Age","Gender","Email","Phone No.","Specialization","Password"))

        self.treeview.heading("Username",text="Username")
        self.treeview.heading("Name",text="Name")
        self.treeview.heading("Age",text="Age")
        self.treeview.heading("Gender",text="Gender")
        self.treeview.heading("Email",text="Email")
        self.treeview.heading("Phone No.",text="Phone No.")
        self.treeview.heading("Specialization",text="Specialization")
        self.treeview.heading("Password",text="Password")

        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("Username",anchor="center",width=150)
        self.treeview.column("Name",anchor="center",width=150)
        self.treeview.column("Age",anchor="center",width=150)
        self.treeview.column("Gender",anchor="center",width=150)
        self.treeview.column("Email",anchor="center",width=150)
        self.treeview.column("Phone No.",anchor="center",width=150)
        self.treeview.column("Specialization",anchor="center",width=150)
        self.treeview.column("Password",anchor="center",width=150)


        # self.treeview.bind("<Double-1>", self.populate_entry_boxes)

        self.import_data()

        self.treeview.place(x=141,y=485,width=1300,height=437)



        def authenticate(name,age,gender,email,phone,specialization,password,username):
            if name != "" and age != "" and gender != "" and email != "" and phone != "" and specialization != "" and password != "" and username != "":
                age = int(age)
                mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM doc_details WHERE username = %s", (username,))

                res = mycursor.fetchone()
                if res: 
                    messagebox.showwarning("Error", "Data already exists!")


                else:
                    self.add_details(name,age,gender,email,phone,specialization,password,username)
                    messagebox.showinfo("Info", "Data edited successfully!")
                mycursor.close()
                mydb.close()


            else:
                messagebox.showerror("Error!", "All the Fields are compulsory.")


#----------------------------------------------------------------functions--------------------------------------------------------

    def authenticate(self,name,age,gender,email,phone,specialization,password,username):
        if name != "" and age != "" and gender != "" and email != "" and phone != "" and specialization != "" and password != "" and username != "":
            mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM doc_details WHERE username = %s", (username,))

            res = mycursor.fetchone()
            if res: 
                messagebox.showwarning("Error", "Data already exists!")


            else:
                self.add_details(name,age,gender,email,phone,specialization,password,username)
                messagebox.showinfo("Info", "Data edited successfully!")

                
                
            mycursor.close()
            mydb.close()


        else:
            messagebox.showerror("Error!", "All the Fields are compulsory.")



    def import_data(self):
        
        mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
        mycursor = mydb.cursor()

        query = "SELECT username, name, age, gender, email, phone, specialization, password FROM doc_details"
        mycursor.execute(query)

        rows = mycursor.fetchall()

        for row in rows:
            self.treeview.insert("","end",values=row)

        mycursor.close()
        mydb.close()



    def add_details(self,name,age,gender,email,phone,specialization,password,username):
        if name != "" and age != "" and gender != "" and email != "" and phone != "" and specialization != "" and password != "" and username != "":
            if len(phone) == 10 and phone.isnumeric() or phone == 'None':
                if len(age) < 4 and age.isnumeric() or age == 'None':
                    mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh@2004",database="hmsdb")
                    mycursor = mydb.cursor()

                    query = "INSERT INTO doc_details (username, name, age, gender, email, phone, specialization, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    mycursor.execute(query,(username, name, age, gender, email, phone, specialization, password))
                    mycursor.execute("INSERT INTO employee(emp_name,username,password,mobile_no) VALUES(%s,%s,%s,%s)",(name,username,password,phone))
                    mydb.commit()

                    self.name_var.set('')
                    self.age_var.set('')
                    self.gender_var.set('')
                    self.email_var.set('')
                    self.phone_var.set('')
                    self.specialization_var.set('')
                    self.passwrd_var.set('')
                    self.username_var.set('')
                    self.name_entry.focus_set()

                    self.update_treeview()

                else:
                    messagebox.showerror("Error!", "Invalid Age.")
            else:
                messagebox.showerror("Error!", "Invalid Phone number.")
        else :
            messagebox.showerror("Error!", "All the Fields are compursory.")


    def update_treeview(self):
        self.treeview.delete(*self.treeview.get_children())
        self.import_data()


    def back_button(self,username, password):
        self.withdraw()
        back = Admin_Main(username, password)
        back.mainloop()


#=====================================================================admin_edit_doctors.py=======================================================================

class Admin_edit_doctors(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("ADMIN-ADD DOCTORS")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/Admin_edit_doctors.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

        inter_font = font.Font(family="Inter")
        
#--------------------------------------- BUTTON/ Labels ------------------------------------------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/admin_edit_doctor_update_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/admin_edit_doctor_delete_button.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))


        self.backbutton = Button(self,image=self.photo2,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=55,height=40,x=30,y=30)

        self.update_details_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=self.update_details)
        self.update_details_button.place(width=280,height=65,x=834,y=379)

        self.delete_details_button = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=self.delete_details)
        self.delete_details_button.place(width=280,height=65,x=1162,y=379)



        self.name_var = tk.StringVar()
        self.name_entry = Entry(self,textvariable=self.name_var,font=(inter_font,25))
        self.name_entry.place(width=336,height=50,x=450,y=93)

        self.age_var = tk.StringVar()
        age_entry = Entry(self,textvariable=self.age_var,font=(inter_font,25))
        age_entry.place(width=336,height=50,x=450,y=170)

        self.gender_var = tk.StringVar()
        gender_entry = Entry(self,textvariable=self.gender_var,font=(inter_font,25))
        gender_entry.place(width=336,height=50,x=450,y=246)

        self.email_var = tk.StringVar()
        email_entry = Entry(self,textvariable=self.email_var,font=(inter_font,25))
        email_entry.place(width=336,height=50,x=450,y=322)

        self.phone_var = tk.StringVar()
        phone_entry = Entry(self,textvariable=self.phone_var,font=(inter_font,25))
        phone_entry.place(width=336,height=50,x=450,y=397)

        self.specialization_var = tk.StringVar()
        specialization_entry = Entry(self,textvariable=self.specialization_var,font=(inter_font,25))
        specialization_entry.place(width=336,height=50,x=1106,y=93)

        self.passwrd_var = tk.StringVar()
        passwrd_entry = Entry(self,textvariable=self.passwrd_var,font=(inter_font,25))
        passwrd_entry.place(width=336,height=50,x=1106,y=170)

        self.username_var = tk.StringVar()
        username_entry = Entry(self,textvariable=self.username_var,font=(inter_font,25),state="readonly")
        username_entry.place(width=336,height=50,x=1106,y=246)



        self.treeview = ttk.Treeview(self,columns=("Username","Name","Age","Gender","Email","Phone No.","Specialization","Password"))

        self.treeview.heading("Username",text="Username")
        self.treeview.heading("Name",text="Name")
        self.treeview.heading("Age",text="Age")
        self.treeview.heading("Gender",text="Gender")
        self.treeview.heading("Email",text="Email")
        self.treeview.heading("Phone No.",text="Phone No.")
        self.treeview.heading("Specialization",text="Specialization")
        self.treeview.heading("Password",text="Password")

        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("Username",anchor="center",width=150)
        self.treeview.column("Name",anchor="center",width=150)
        self.treeview.column("Age",anchor="center",width=150)
        self.treeview.column("Gender",anchor="center",width=150)
        self.treeview.column("Email",anchor="center",width=150)
        self.treeview.column("Phone No.",anchor="center",width=150)
        self.treeview.column("Specialization",anchor="center",width=150)
        self.treeview.column("Password",anchor="center",width=150)


        self.treeview.bind("<Double-1>", self.populate_entry_boxes)

        self.import_data()

        self.treeview.place(x=141,y=485,width=1300,height=437)






    def populate_entry_boxes(self, event):
        selected_item = self.treeview.focus()
        if selected_item:
            values = self.treeview.item(selected_item)["values"]
            self.username_var.set(values[0])
            self.name_var.set(values[1])
            self.age_var.set(values[2])
            self.gender_var.set(values[3])
            self.email_var.set(values[4])
            self.phone_var.set(values[5])
            self.specialization_var.set(values[6])
            self.passwrd_var.set(values[7])


    def import_data(self):
        
        mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
        mycursor = mydb.cursor()

        query = "SELECT username, name, age, gender, email, phone, specialization, password FROM doc_details"
        mycursor.execute(query)

        rows = mycursor.fetchall()

        for row in rows:
            self.treeview.insert("","end",values=row)

        mycursor.close()
        mydb.close()


    def update_details(self):
        selected_item = self.treeview.focus()
        if selected_item:
            values = self.treeview.item(selected_item)["values"]
            username = values[0]
            name = self.name_var.get()
            age = self.age_var.get()
            gender = self.gender_var.get()
            email = self.email_var.get()
            phone = self.phone_var.get()
            specialization = self.specialization_var.get()
            password = self.passwrd_var.get()

            mydb = mysql.connector.connect(host="localhost", user="root", password="Vignesh!2004#", database="hmsdb")
            mycursor = mydb.cursor()

            a = b = 1  
            try:
                query = "UPDATE doc_details SET name=%s, gender=%s, email=%s, specialization=%s, password=%s WHERE username=%s"
                values = (name, gender, email, specialization, password, username)
                mycursor.execute(query, values)

                query = "UPDATE admin SET password = %s WHERE username = %s"
                mycursor.execute(query,(password,username))


                mydb.commit()

            except mysql.connector.Error as err:
                print(f"Error inserting mobile number: {err}")
            
            if age.isnumeric() and len(age) < 4:
                try:
                    query = "UPDATE doc_details SET age = %s WHERE username = %s"
                    mycursor.execute(query, (age,username))

                    mydb.commit()

                except mysql.connector.Error as err:
                    print(f"Error inserting mobile number: {err}")

            else:
                if age != 'None':
                    a = 0
                    messagebox.showerror("Error!", "Age is Invalid.")

            if (len(phone) == 10 and phone.isnumeric()):
                try:
                    query = "UPDATE doc_details SET phone = %s WHERE username = %s"
                    mycursor.execute(query, (phone,username))

                    mydb.commit()

                except mysql.connector.Error as err:
                    print(f"Error inserting mobile number: {err}")

            else:
                if phone != 'None':
                    b = 0
                    messagebox.showerror("Error!", "Phone number is Invalid.")

            # Clear the entry boxes
            self.clear_entry_boxes()

            # Refresh the treeview with updated data
            self.treeview.delete(*self.treeview.get_children())
            self.import_data()

            if (a==1 and b==1):
                messagebox.showinfo("Success", "Details updated successfully!")

            mycursor.close()
            mydb.close()
        else:
            messagebox.showerror("Error", "No item selected!")


    def delete_details(self):
        selected_item = self.treeview.focus()
        if selected_item:
            values = self.treeview.item(selected_item)["values"]
            username = values[0]

            mydb = mysql.connector.connect(host="localhost", user="root", password="Vignesh!2004#", database="hmsdb")
            mycursor = mydb.cursor()

            query = "DELETE FROM doc_details WHERE username=%s"
            value = (username,)
            mycursor.execute(query, value)
            query = "DELETE FROM employee WHERE username=%s"
            value = (username,)
            mycursor.execute(query, value)
            mydb.commit()

            self.clear_entry_boxes()

            self.treeview.delete(*self.treeview.get_children())
            self.import_data()

            messagebox.showinfo("Success", "Details deleted successfully!")

            mycursor.close()
            mydb.close()
        else:
            messagebox.showerror("Error", "No item selected!")


    def clear_entry_boxes(self):
        self.username_var.set("")
        self.name_var.set("")
        self.age_var.set("")
        self.gender_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.specialization_var.set("")
        self.passwrd_var.set("")


    def back_button(self,username, password):
        self.withdraw()
        back = Admin_Main(username, password)
        back.mainloop()


#======================================================================admin_feedback.py==========================================================================

class Admin_feedback(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("ADMIN-FEEDBACK")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/Admin_feedback.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

        inter_font = font.Font(family="Inter")
        
#--------------------------------------- BUTTON/ Labels ------------------------------------------------------------

        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))


        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=55,height=40,x=30,y=30)




#---------------------------------MY SQL / TREE VIEW and Data labels --------------------------------------------------
        self.treeview = ttk.Treeview(self,columns=("Name","Email","Feedback"))

        self.treeview.heading("Name",text="Name")
        self.treeview.heading("Email",text="Email")
        self.treeview.heading("Feedback",text="Feedback")

        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("Name",anchor="center",width=150)
        self.treeview.column("Email",anchor="center",width=150)
        self.treeview.column("Feedback",anchor="center",width=150)

        self.import_data()

        self.treeview.place(x=110,y=240,width=1340,height=620)


            

#---------------------------------------------------FUNCTIONS-----------------------------------------------------------------------
    def import_data(self):
        
        mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
        mycursor = mydb.cursor()

        query = "SELECT name, email, feedback FROM feedback"
        mycursor.execute(query)

        rows = mycursor.fetchall()

        for row in rows:
            self.treeview.insert("","end",values=row)

        mycursor.close()
        mydb.close()



    def back_button(self,username, password):
        self.withdraw()
        back = Admin_Main(username, password)
        back.mainloop()


#=============================================================================emp.py==============================================================================

class Employee(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("EMPLOYEE LOGIN")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/Login_page.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')


#-------------------------------Entry Box-----------------------------------------------------------------

        username_var = tk.StringVar()
        username_entry = Entry(self,textvariable=username_var,font=("Roboto",25))
        username_entry.place(width=524,height=78,x=509,y=391)

        passwrd_var = tk.StringVar()
        passwrd_entry = Entry(self,show="*",textvariable=passwrd_var,font=("Roboto",25))
        passwrd_entry.place(width=524,height=78,x=509,y=544)

#----------------------------------------------------Buttons-----------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/adm_login_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/adm_signup_button.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))


        self.loginbutton = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: authenticate(username_entry.get(),passwrd_entry.get()))
        self.loginbutton.place(width=218,height=65,x=661,y=665)

        self.signupbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=self.signup_button)
        self.signupbutton.place(width=218,height=65,x=661,y=795)

        self.backbutton = Button(self,image=self.photo2,borderwidth=0,highlightthickness=0,command=self.back_button)
        self.backbutton.place(width=55,height=40,x=30,y=30)



        def authenticate(username,password):

            mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM employee WHERE username = %s AND password = %s", (username, password))

            res = mycursor.fetchone()
            if res: 
                messagebox.showinfo("Login", "Login successful!")
                mycursor.close()
                mydb.close()
                self.login_button(username,password)


            else:
                messagebox.showwarning("Login", "Invalid username or password!")



    def back_button(self):
        self.destroy()
        self.master.destroy()
        back = HMS()
        back.mainloop()


    def login_button(self,username,password):
        self.withdraw()
        login = Emp_Main(username,password)
        login.mainloop()
        

    def signup_button(self):
        self.destroy()
        signup = Emp_Signup()
        signup.mainloop()


#========================================================================emp_signup.py============================================================================

class Emp_Signup(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("SIGN UP - EMPLOYEE")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/SIGN_UP_page.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')


#-------------------------------Entry Box-----------------------------------------------------------------

        name_var = tk.StringVar()
        name_entry = Entry(self,textvariable=name_var,font=("Roboto",25))
        name_entry.place(width=490,height=54,x=525,y=284)

        username_var = tk.StringVar()
        username_entry = Entry(self,textvariable=username_var,font=("Roboto",25))
        username_entry.place(width=490,height=54,x=525,y=392)

        passwrd_var = tk.StringVar()
        passwrd_entry = Entry(self,show="*",textvariable=passwrd_var,font=("Roboto",25))
        passwrd_entry.place(width=490,height=54,x=525,y=504)

        mob_var = tk.StringVar()
        mob_entry = Entry(self,textvariable=mob_var,font=("Roboto",25))
        mob_entry.place(width=490,height=54,x=525,y=612)

#----------------------------------------------------Buttons-----------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/create_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))


        self.createbutton = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: insertion(name_entry.get(),username_entry.get(),passwrd_entry.get(),mob_entry.get()))
        self.createbutton.place(width=331,height=58,x=605,y=749)


        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=self.back_button)
        self.backbutton.place(width=55,height=40,x=30,y=30)


        def insertion(name,username,password,mobile):
            if name != "" and username != "" and password != "" and mobile != "":
                
                mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM employee WHERE username = %s",(username,))
                res = mycursor.fetchone()

                if res:
                    messagebox.showerror("Error!", "Username already exist, please try to login or use other Username.")

                else:
                    if len(mobile) == 10 and mobile.isnumeric():
                        try :
                            mycursor.execute("INSERT INTO employee(emp_name,username,password,mobile_no) VALUES(%s,%s,%s,%s)",(name,username,password,mobile))
                            mycursor.execute("INSERT INTO doc_details(name,username,password,phone) VALUES(%s,%s,%s,%s)",(name,username,password,mobile))
                            mydb.commit()
                            messagebox.showinfo("Info","Account Succesfully created.")
                            mycursor.close()
                            mydb.close()
                            self.create_button()
                        except Exception as e:
                            print(e)
                            mydb.rollback()
                            mydb.close()
                    else:
                        messagebox.showerror("Error!", "Invalid mobile number.")
            else:
                messagebox.showerror("Error!", "All the Fields are compursory.")

    def back_button(self):
        self.withdraw()
        back = Employee()
        back.mainloop()

    def create_button(self):
        self.withdraw()
        back = Employee()
        back.mainloop()


#==========================================================================emp_main.py=============================================================================

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
           self.withdraw()
           logout = Employee()
           logout.mainloop()


    def profile(self,username,password):
        self.withdraw()
        profile = doctor_Profile(username,password)
        profile.mainloop()


    def pat_history(self,username,password):
        self.withdraw()
        pat_history = Emp_pat_hist(username,password)
        pat_history.mainloop()


#=======================================================================doctor_profile.py==========================================================================

class doctor_Profile(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("DOCTOR-PROFILE")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/doctor_main_profile.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

        
# ------------------------------------inserting fonts --------------------------------------------------------------------   
    
        inter_font = font.Font(family="Inter")


#----------------------------------------------------------------MySQL connection --------------------------------------------
        
        mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
        mycursor = mydb.cursor()

        query = "SELECT * FROM doc_details WHERE username = %s AND password = %s"
        mycursor.execute(query, (username,password))

        row = mycursor.fetchone()

        if row:
            username = row[0]
            name = row[1]
            age  = row[2]
            gender = row[3]
            email = row[4]
            phone = row[5]
            specialization = row[6]
            password = row[7]

        mycursor.close()
        mydb.close()


#--------------------------------------------- Creating Labels / Buttons --------------------------------------------------------

        username_label = tk.Label(self,text=username,font=(inter_font,36),bg="#E7F7F8")
        username_label.place(x=720,y=156)

        name_label = tk.Label(self,text=name,font=(inter_font,36),bg="#E7F7F8")
        name_label.place(x=720,y=231)

        age_label = tk.Label(self,text=age,font=(inter_font,36),bg="#E7F7F8")
        age_label.place(x=720,y=306)

        gender_label = tk.Label(self,text=gender,font=(inter_font,36),bg="#E7F7F8")
        gender_label.place(x=720,y=381)

        email_label = tk.Label(self,text=email,font=(inter_font,36),bg="#E7F7F8")
        email_label.place(x=720,y=456)

        phone_label = tk.Label(self,text=phone,font=(inter_font,36),bg="#E7F7F8")
        phone_label.place(x=720,y=531)

        specialization_label = tk.Label(self,text=specialization,font=(inter_font,36),bg="#E7F7F8")
        specialization_label.place(x=720,y=606)

        password_label = tk.Label(self,text=password,font=(inter_font,36),bg="#E7F7F8")
        password_label.place(x=720,y=681)



        self.photo = ImageTk.PhotoImage(Image.open("Images/adm_pro_Edit_details_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))

        self.edit_details_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: self.edit_button(username, password))
        self.edit_details_button.place(width=230,height=65,x=665,y=836)

        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=55,height=40,x=30,y=30)

        

#--------------------------------------------------------------------Functions defined -----------------------------------------------------------------------------------

    def back_button(self,username,password):
        self.withdraw()
        back = Emp_Main(username,password)
        back.mainloop()


    def edit_button(self,username,password):
        self.withdraw()
        edit = Emp_Profile_update(username,password)
        edit.mainloop()


#====================================================================doctor_profile_update.py======================================================================

class Emp_Profile_update(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("DOCTOR-PROFILE (UPDATE)")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/doctor_main_profile_edit.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')


        inter_font = font.Font(family="Inter")
#-------------------------------------------------------------- Entry box / button ---------------------------------------------------------------

        self.username_var = tk.StringVar()
        username_entry = Entry(self,textvariable=self.username_var,font=(inter_font,21),state="readonly")
        username_entry.place(width=530,height=50,x=720,y=157)

        self.name_var = tk.StringVar()
        name_entry = Entry(self,textvariable=self.name_var,font=(inter_font,21))
        name_entry.place(width=530,height=50,x=720,y=232)

        self.age_var = tk.StringVar()
        age_entry = Entry(self,textvariable=self.age_var,font=(inter_font,21))
        age_entry.place(width=530,height=50,x=720,y=307)

        self.gender_var = tk.StringVar()
        gender_entry = Entry(self,textvariable=self.gender_var,font=(inter_font,21))
        gender_entry.place(width=530,height=50,x=720,y=382)

        self.email_var = tk.StringVar()
        email_entry = Entry(self,textvariable=self.email_var,font=(inter_font,21))
        email_entry.place(width=530,height=50,x=720,y=457)

        self.phone_var = tk.StringVar()
        phone_entry = Entry(self,textvariable=self.phone_var,font=(inter_font,21))
        phone_entry.place(width=530,height=50,x=720,y=532)

        self.specialization_var = tk.StringVar()
        specialization_entry = Entry(self,textvariable=self.specialization_var,font=(inter_font,21))
        specialization_entry.place(width=530,height=50,x=720,y=607)

        self.passwrd_var = tk.StringVar()
        passwrd_entry = Entry(self,textvariable=self.passwrd_var,font=(inter_font,21))
        passwrd_entry.place(width=530,height=50,x=720,y=682)


        self.photo = ImageTk.PhotoImage(Image.open("Images/adm_pro_Save_details_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))

        self.save_detail_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=self.save_details)
        self.save_detail_button.place(width=230,height=65,x=665,y=843)

        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=55,height=40,x=30,y=30)

#------------------------------------------------------mysql connection----------------------------------------------------------

        mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
        mycursor = mydb.cursor()

        query = "SELECT * FROM doc_details WHERE username = %s"
        mycursor.execute(query, (username,))

        row = mycursor.fetchone()

        if row:
            username = row[0]
            name = row[1]
            age  = row[2]
            gender = row[3]
            email = row[4]
            phone = row[5]
            specialization = row[6]
            password = row[7]

        self.username_var.set(username)
        self.name_var.set(name)
        self.age_var.set(age)
        self.gender_var.set(gender)
        self.email_var.set(email)
        self.phone_var.set(phone)
        self.specialization_var.set(specialization)
        self.passwrd_var.set(password)

#-----------------------------------------------------------function define -----------------------------------------------------------------

    def save_details(self):
        username = self.username_var.get()
        name = self.name_var.get()
        age = self.age_var.get()
        gender = self.gender_var.get()
        email = self.email_var.get()
        phone = self.phone_var.get()
        specialization = self.specialization_var.get()
        password = self.passwrd_var.get()
            
        if name == "":
            name = None
        if age == "":
            age = None
        if gender == "":
            gender = None
        if email == "":
            email = None
        if phone == "":
            phone = None
        if specialization == "":
            specialization = None
        if password == "":
            password = None

        a = b = 1
        mydb = mysql.connector.connect(host="localhost", user="root", password="Vignesh!2004#", database="hmsdb")
        mycursor = mydb.cursor()

        try:
            query = "UPDATE doc_details SET name = %s, gender = %s, email = %s, specialization = %s, password = %s WHERE username = %s"
            mycursor.execute(query, (name, gender, email, specialization, password, username))

            query = "UPDATE employee SET password = %s WHERE username = %s"
            mycursor.execute(query,(password,username))

            mydb.commit()

        except mysql.connector.Error as err:
            print(f"Error inserting mobile number: {err}")
        
        if age.isnumeric and len(age) < 4:
            try:
                query = "UPDATE doc_details SET age = %s WHERE username = %s"
                mycursor.execute(query, (age,username))

                mydb.commit()

            except mysql.connector.Error as err:
                print(f"Error inserting mobile number: {err}")

        else:
            a = 0
            messagebox.showerror("Error!", "Age is Invalid.")

        if (len(phone) == 10 and phone.isnumeric()):
            try:
                query = "UPDATE doc_details SET phone = %s WHERE username = %s"
                mycursor.execute(query, (phone,username))

                mydb.commit()

            except mysql.connector.Error as err:
                print(f"Error inserting mobile number: {err}")

        else:
            b = 0
            messagebox.showerror("Error!", "Phone number is Invalid.")

        if (a==1 and b==1):
            messagebox.showinfo("Update", "Profile details updated successfully!")

        mydb.commit()

        mycursor.close()
        mydb.close()
        

        self.withdraw()
        save = doctor_Profile(username,password)
        save.mainloop()

    
    def back_button(self,username,password):
        self.withdraw()
        back = doctor_Profile(username,password)
        back.mainloop()


#=====================================================================doctor_pat_hist.py===========================================================================

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
        self.withdraw()
        back = Emp_Main(username,password)
        back.mainloop()


#===========================================================================patient.py=============================================================================

class Patient(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("PATIENT LOGIN")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/Login_page.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')


#-------------------------------Entry Box-----------------------------------------------------------------

        username_var = tk.StringVar()
        username_entry = Entry(self,textvariable=username_var,font=("Roboto",25))
        username_entry.place(width=524,height=78,x=509,y=391)

        passwrd_var = tk.StringVar()
        passwrd_entry = Entry(self,show="*",textvariable=passwrd_var,font=("Roboto",25))
        passwrd_entry.place(width=524,height=78,x=509,y=544)

#----------------------------------------------------Buttons-----------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/adm_login_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/adm_signup_button.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))


        self.loginbutton = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: authenticate(username_entry.get(),passwrd_entry.get()))
        self.loginbutton.place(width=218,height=65,x=661,y=665)

        self.signupbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=self.signup_button)
        self.signupbutton.place(width=218,height=65,x=661,y=795)

        self.backbutton = Button(self,image=self.photo2,borderwidth=0,highlightthickness=0,command=self.back_button)
        self.backbutton.place(width=55,height=40,x=30,y=30)


        def authenticate(username,password):

            mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM patient WHERE username = %s AND password = %s", (username, password))

            res = mycursor.fetchone()
            if res: 
                messagebox.showinfo("Login", "Login successful!")
                mycursor.close()
                mydb.close()
                self.login_button(username,password)


            else:
                messagebox.showwarning("Login", "Invalid username or password!")



    def back_button(self):
        self.destroy()
        self.master.destroy()
        back = HMS()
        back.mainloop()


    def login_button(self,username,password):
        self.withdraw()
        login = pat_Main(username,password)
        login.mainloop()
        

    def signup_button(self):
        self.destroy()
        signup = Pat_Signup()
        signup.mainloop()


#=======================================================================patient_signup.py===========================================================================

class Pat_Signup(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("SIGN UP - PATIENT")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/SIGN_UP_page.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')


#-------------------------------Entry Box-----------------------------------------------------------------

        name_var = tk.StringVar()
        name_entry = Entry(self,textvariable=name_var,font=("Roboto",25))
        name_entry.place(width=490,height=54,x=525,y=284)

        username_var = tk.StringVar()
        username_entry = Entry(self,textvariable=username_var,font=("Roboto",25))
        username_entry.place(width=490,height=54,x=525,y=392)

        passwrd_var = tk.StringVar()
        passwrd_entry = Entry(self,show="*",textvariable=passwrd_var,font=("Roboto",25))
        passwrd_entry.place(width=490,height=54,x=525,y=504)

        mob_var = tk.StringVar()
        mob_entry = Entry(self,textvariable=mob_var,font=("Roboto",25))
        mob_entry.place(width=490,height=54,x=525,y=612)

#----------------------------------------------------Buttons-----------------------------

        self.photo = ImageTk.PhotoImage(Image.open("Images/create_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))


        self.createbutton = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: insertion(name_entry.get(),username_entry.get(),passwrd_entry.get(),mob_entry.get()))
        self.createbutton.place(width=331,height=58,x=605,y=749)


        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=self.back_button)
        self.backbutton.place(width=55,height=40,x=30,y=30)


        def insertion(name,username,password,mobile):
            if name != "" and username != "" and password != "" and mobile != "":
                mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM patient WHERE username = %s",(username,))
                res = mycursor.fetchone()

                if res:
                    messagebox.showerror("Error!", "Username already exist, please try to login or use other Username.")

                else:
                    if len(mobile) == 10 and mobile.isnumeric():
                        try :
                            mycursor.execute("INSERT INTO patient(pat_name,username,password,mobile_no) VALUES(%s,%s,%s,%s)",(name,username,password,mobile))
                            mycursor.execute("INSERT INTO pat_details(name,username,password,phone) VALUES(%s,%s,%s,%s)",(name,username,password,mobile))
                            mydb.commit()
                            messagebox.showinfo("Info","Account Succesfully created.")
                            mycursor.close()
                            mydb.close()
                            self.create_button()
                        except Exception as e:
                            print(e)
                            mydb.rollback()
                            mydb.close()
                    else:
                        messagebox.showerror("Error!", "Invalid mobile number.")
            else:
                messagebox.showerror("Error!", "All the Fields are compursory.")


    def back_button(self):
        self.destroy()
        self.master.destroy()
        back = HMS()
        back.mainloop()

    def create_button(self):
        self.withdraw()
        back = Patient()
        back.mainloop()


#========================================================================patient_main.py=========================================================================

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
           self.withdraw()
           logout = Patient()
           logout.mainloop()


    def profile(self,username,password):
        self.withdraw()
        profile = patient_Profile(username,password)
        profile.mainloop()


    def activity(self,username,password):
        self.withdraw()
        activity = patient_activity(username,password)
        activity.mainloop()


#========================================================================patient_profile.py======================================================================

class patient_Profile(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("PATIENT-PROFILE")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/patient_profile.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')

        
# ------------------------------------inserting fonts --------------------------------------------------------------------   
    
        inter_font = font.Font(family="Inter")


#----------------------------------------------------------------MySQL connection --------------------------------------------
        
        mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
        mycursor = mydb.cursor()

        query = "SELECT * FROM pat_details WHERE username = %s AND password = %s"
        mycursor.execute(query, (username,password))

        row = mycursor.fetchone()

        if row:
            username = row[0]
            name = row[1]
            age  = row[2]
            gender = row[3]
            email = row[4]
            phone = row[5]
            blood_grp = row[6]
            password = row[7]

        mycursor.close()
        mydb.close()


#--------------------------------------------- Creating Labels / Buttons --------------------------------------------------------

        username_label = tk.Label(self,text=username,font=(inter_font,36),bg="#E7F7F8")
        username_label.place(x=720,y=156)

        name_label = tk.Label(self,text=name,font=(inter_font,36),bg="#E7F7F8")
        name_label.place(x=720,y=231)

        age_label = tk.Label(self,text=age,font=(inter_font,36),bg="#E7F7F8")
        age_label.place(x=720,y=306)

        gender_label = tk.Label(self,text=gender,font=(inter_font,36),bg="#E7F7F8")
        gender_label.place(x=720,y=381)

        email_label = tk.Label(self,text=email,font=(inter_font,36),bg="#E7F7F8")
        email_label.place(x=720,y=456)

        phone_label = tk.Label(self,text=phone,font=(inter_font,36),bg="#E7F7F8")
        phone_label.place(x=720,y=531)

        blood_grp_label = tk.Label(self,text=blood_grp,font=(inter_font,36),bg="#E7F7F8")
        blood_grp_label.place(x=720,y=606)

        password_label = tk.Label(self,text=password,font=(inter_font,36),bg="#E7F7F8")
        password_label.place(x=720,y=681)



        self.photo = ImageTk.PhotoImage(Image.open("Images/adm_pro_Edit_details_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))

        self.edit_details_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=lambda: self.edit_button(username, password))
        self.edit_details_button.place(width=230,height=65,x=665,y=836)

        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=55,height=40,x=30,y=30)

        

#--------------------------------------------------------------------Functions defined -----------------------------------------------------------------------------------

    def back_button(self,username,password):
        self.withdraw()
        back = pat_Main(username,password)
        back.mainloop()


    def edit_button(self,username,password):
        self.withdraw()
        edit = pat_Profile_update(username,password)
        edit.mainloop()


#=====================================================================patient_profile_update.py==================================================================

class pat_Profile_update(tk.Toplevel):
    def __init__(self,username,password, master=None):
        super().__init__(master)

        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("PATIENT-PROFILE (UPDATE)")

        self.canvas = tk.Canvas(self, width=1560, height=960)
        self.canvas.pack(expand=True, fill='both')

        self.image = tk.PhotoImage(file='Images/patient_main_profile_edit.png')
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')


        inter_font = font.Font(family="Inter")
#-------------------------------------------------------------- Entry box / button ---------------------------------------------------------------

        self.username_var = tk.StringVar()
        username_entry = Entry(self,textvariable=self.username_var,font=(inter_font,21),state="readonly")
        username_entry.place(width=530,height=50,x=720,y=157)

        self.name_var = tk.StringVar()
        name_entry = Entry(self,textvariable=self.name_var,font=(inter_font,21))
        name_entry.place(width=530,height=50,x=720,y=232)

        self.age_var = tk.StringVar()
        age_entry = Entry(self,textvariable=self.age_var,font=(inter_font,21))
        age_entry.place(width=530,height=50,x=720,y=307)

        self.gender_var = tk.StringVar()
        gender_entry = Entry(self,textvariable=self.gender_var,font=(inter_font,21))
        gender_entry.place(width=530,height=50,x=720,y=382)

        self.email_var = tk.StringVar()
        email_entry = Entry(self,textvariable=self.email_var,font=(inter_font,21))
        email_entry.place(width=530,height=50,x=720,y=457)

        self.phone_var = tk.StringVar()
        phone_entry = Entry(self,textvariable=self.phone_var,font=(inter_font,21))
        phone_entry.place(width=530,height=50,x=720,y=532)

        self.blood_grp_var = tk.StringVar()
        blood_grp_entry = Entry(self,textvariable=self.blood_grp_var,font=(inter_font,21))
        blood_grp_entry.place(width=530,height=50,x=720,y=607)

        self.passwrd_var = tk.StringVar()
        passwrd_entry = Entry(self,textvariable=self.passwrd_var,font=(inter_font,21))
        passwrd_entry.place(width=530,height=50,x=720,y=682)


        self.photo = ImageTk.PhotoImage(Image.open("Images/adm_pro_Save_details_button.png"))
        self.photo1 = ImageTk.PhotoImage(Image.open("Images/back_button.png"))

        self.save_detail_button = Button(self,image=self.photo,borderwidth=0,highlightthickness=0,command=self.save_details)
        self.save_detail_button.place(width=230,height=65,x=665,y=843)

        self.backbutton = Button(self,image=self.photo1,borderwidth=0,highlightthickness=0,command=lambda: self.back_button(username, password))
        self.backbutton.place(width=55,height=40,x=30,y=30)

#------------------------------------------------------mysql connection----------------------------------------------------------

        mydb = mysql.connector.connect(host="localhost",user="root",password="Vignesh!2004#",database="hmsdb")
        mycursor = mydb.cursor()

        query = "SELECT * FROM pat_details WHERE username = %s"
        mycursor.execute(query, (username,))

        row = mycursor.fetchone()

        if row:
            username = row[0]
            name = row[1]
            age  = row[2]
            gender = row[3]
            email = row[4]
            phone = row[5]
            blood_grp = row[6]
            password = row[7]

        self.username_var.set(username)
        self.name_var.set(name)
        self.age_var.set(age)
        self.gender_var.set(gender)
        self.email_var.set(email)
        self.phone_var.set(phone)
        self.blood_grp_var.set(blood_grp)
        self.passwrd_var.set(password)

#-----------------------------------------------------------function define -----------------------------------------------------------------

    def save_details(self):
        username = self.username_var.get()
        name = self.name_var.get()
        age = self.age_var.get()
        gender = self.gender_var.get()
        email = self.email_var.get()
        phone = self.phone_var.get()
        blood_grp = self.blood_grp_var.get()
        password = self.passwrd_var.get()
            
        if name == "":
            name = None
        if age == "":
            age = None
        if gender == "":
            gender = None
        if email == "":
            email = None
        if phone == "":
            phone = None
        if blood_grp == "":
            blood_grp = None
        if password == "":
            password = None


        a = b = 1
        mydb = mysql.connector.connect(host="localhost", user="root", password="Vignesh!2004#", database="hmsdb")
        mycursor = mydb.cursor()


        try:
            query = "UPDATE pat_details SET name = %s, gender = %s, email = %s, blood_grp = %s, password = %s WHERE username = %s"
            mycursor.execute(query, (name, gender, email, blood_grp, password, username))

            query = "UPDATE patient SET password = %s WHERE username = %s"
            mycursor.execute(query,(password,username))


            mydb.commit()

        except mysql.connector.Error as err:
            print(f"Error inserting mobile number: {err}")
        
        if age.isnumeric and len(age) < 4:
            try:
                query = "UPDATE pat_details SET age = %s WHERE username = %s"
                mycursor.execute(query, (age,username))

                mydb.commit()

            except mysql.connector.Error as err:
                print(f"Error inserting mobile number: {err}")

        else:
            if age != 'None':
                a = 0
                messagebox.showerror("Error!", "Age is Invalid.")

        if (len(phone) == 10 and phone.isnumeric()):
            try:
                query = "UPDATE pat_details SET phone = %s WHERE username = %s"
                mycursor.execute(query, (phone,username))

                mydb.commit()

            except mysql.connector.Error as err:
                print(f"Error inserting mobile number: {err}")

        else:
            if phone != 'None':
                b = 0
                messagebox.showerror("Error!", "Phone number is Invalid.")

        if (a == 1 and b == 1):
            messagebox.showinfo("Update", "Profile details updated successfully!")

        mydb.commit()

        mycursor.close()
        mydb.close()


        self.withdraw()
        save = patient_Profile(username,password)
        save.mainloop()

    
    def back_button(self,username,password):
        self.withdraw()
        save = patient_Profile(username,password)
        save.mainloop()


#=======================================================================patient_activity.py=====================================================================

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
        self.withdraw()
        back = pat_Main(username,password)
        back.mainloop()



#---------------------------------------------------------Main App Calling part------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app = HMS()
    app.mainloop()



