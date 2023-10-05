import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from app_main import HMS


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
        from emp import Employee
        self.withdraw()
        back = Employee()
        back.mainloop()

    def create_button(self):
        from emp import Employee
        self.withdraw()
        back = Employee()
        back.mainloop()

