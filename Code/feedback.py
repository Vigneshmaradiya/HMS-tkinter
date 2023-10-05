import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import mysql.connector
from app_main import HMS


class feedback(tk.Toplevel):
    def __init__(self,master=None):
        super().__init__(master)
        self.resizable(0,0)

        self.geometry("1560x960")
        self.title("FITNESS CENTER")

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