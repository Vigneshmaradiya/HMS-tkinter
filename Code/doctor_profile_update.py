import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from app_main import HMS
from tkinter import font



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

        mydb = mysql.connector.connect(host="localhost", user="root", password="Vignesh!2004#", database="hmsdb")
        mycursor = mydb.cursor()

        try:
            query = "UPDATE doc_details SET name = %s, gender = %s, email = %s, specialization = %s, password = %s WHERE username = %s"
            mycursor.execute(query, (name, gender, email, specialization, password, username))

            messagebox.showinfo("Update", "Profile details updated successfully!")

            query = "UPDATE employee SET password = %s WHERE username = %s"
            mycursor.execute(query,(password,username))

            mydb.commit()

        except mysql.connector.Error as err:
            print(f"Error inserting mobile number: {err}")
        
        if age.isnumeric and len(age) < 4:
            try:
                query = "UPDATE doc_details SET age = %s WHERE username = %s"
                mycursor.execute(query, (age,username))

                messagebox.showinfo("Update", "Profile details updated successfully!")

                mydb.commit()

            except mysql.connector.Error as err:
                print(f"Error inserting mobile number: {err}")

        else:
            messagebox.showerror("Error!", "Age is Invalid.")

        if (len(phone) == 10 and phone.isnumeric()):
            try:
                query = "UPDATE doc_details SET phone = %s WHERE username = %s"
                mycursor.execute(query, (phone,username))

                messagebox.showinfo("Update", "Profile details updated successfully!")

                mydb.commit()

            except mysql.connector.Error as err:
                print(f"Error inserting mobile number: {err}")

        else:
            messagebox.showerror("Error!", "Phone number is Invalid.")

        mydb.commit()

        mycursor.close()
        mydb.close()
        

        from doctor_profile import doctor_Profile
        self.withdraw()
        save = doctor_Profile(username,password)
        save.mainloop()

    
    def back_button(self,username,password):
        from doctor_profile import doctor_Profile
        self.withdraw()
        back = doctor_Profile(username,password)
        back.mainloop()