from tkinter import *
from tkinter import ttk

class student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40,"bold"), bg="blue", fg="red")
        title.pack(side=TOP, fill=X)

        #============manage Frame=============

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=590)

        m_title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman", 20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll Number", bg="crimson", fg="white",font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1,column=0 ,padx=0,pady=10,sticky="w")

        lbl_roll = Entry(Manage_Frame,font=("times new roman", 15, "bold"),bd=5,relief=GROOVE)
        lbl_roll.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="white",font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, padx=0, pady=10, sticky="w")

        lbl_name = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        lbl_name.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, padx=0, pady=10, sticky="w")

        lbl_email = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        lbl_email.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        lbl_Gender = Label(Manage_Frame, text="Gender", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, padx=0, pady=10, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,font=("times new roman",14,"bold"),state="readonly")
        combo_gender["values"]=("Male","Female","Others")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        lbl_contact = Label(Manage_Frame, text="CONTACT", bg="crimson", fg="white",font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, padx=0, pady=10, sticky="w")

        lbl_contact = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        lbl_contact.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        lbl_Date_of_B = Label(Manage_Frame, text="D.O.B", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        lbl_Date_of_B.grid(row=6, column=0, padx=0, pady=10, sticky="w")

        lbl_Date_of_B = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        lbl_Date_of_B.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        lbl_Address= Label(Manage_Frame, text="Address", bg="crimson", fg="white",font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, padx=0, pady=10, sticky="w")

        txt_add=Text(Manage_Frame,bd=5,relief=GROOVE,width=29,height=5,font=("",10))
        txt_add.grid(row=7,column=1,padx=20,pady=10,sticky="w")

        #===========Manage Frame Button==================

        #=============Detail Frame===============
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=830, height=590)

root = Tk()
ob = student(root)
root.mainloop()
