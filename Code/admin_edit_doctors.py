import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from app_main import HMS
import mysql.connector
from tkinter import font



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

            query = "UPDATE doc_details SET name=%s, age=%s, gender=%s, email=%s, phone=%s, specialization=%s, password=%s WHERE username=%s"
            values = (name, age, gender, email, phone, specialization, password, username)
            mycursor.execute(query, values)
            mydb.commit()

            # Clear the entry boxes
            self.clear_entry_boxes()

            # Refresh the treeview with updated data
            self.treeview.delete(*self.treeview.get_children())
            self.import_data()

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
        from admin_main import Admin_Main
        self.withdraw()
        back = Admin_Main(username, password)
        back.mainloop()