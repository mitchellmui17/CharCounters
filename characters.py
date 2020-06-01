import tkinter
from tkinter import *
from tkinter import messagebox

# Window
top = Tk(className='LogIn')
top.geometry("300x300")

# Username Information
user = Label(top, text="User Name:").grid(row=0)
password = Label(top, text="Password:").grid(row=1)
e1 = Entry(top)
e2 = Entry(top)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


def textFile():
    file = open("beautbst.txt", "r")
    print(file.read())
    messagebox.showinfo("Beauty and the Beast", "Printed Successfully!")


def check():
    if e1.get() == "admin" and e2.get() == "123":
        textFile()
    else:
        messagebox.showinfo("Error", "Incorrect user / password")


enter = tkinter.Button(top, text="login", command=check).grid(row=2)
top.mainloop()
