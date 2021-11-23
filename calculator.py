from tkinter import * 
import tkinter as tk

#Variables 
equation = 0
tempvar = 0
function = ""

#Functions
def add(): 
    print ("add")

def sub():
    print ("sub")

def mult():
    print ("mult")

def div():
    print ("div")

def clear():
    print("Hello")

def submit():
    print("Submit")

def display():
    x = 0

#Design GUI
interface = tk.Tk()
interface.resizable(width=False, height=False)

interface.title("Calculator")
interface.geometry("315x400")

expression_field = Entry(interface, textvariable=equation)
expression_field.grid(row=1, columnspan=4, ipadx=100, ipady=25)

equation = StringVar()

btn0=tk.Button(interface, text="0", width=10, height=5)
btn0.grid(row=5,column=1)

btn1=tk.Button(interface, text="1", width=10, height=5)
btn1.grid(row=4,column=0)

btn2=tk.Button(interface, text="2", width=10, height=5)
btn2.grid(row=4,column=1)

btn3=tk.Button(interface, text="3", width=10, height=5)
btn3.grid(row=4,column=2)

btn4=tk.Button(interface, text="4", width=10, height=5)
btn4.grid(row=3,column=0)

btn5=tk.Button(interface, text="5", width=10, height=5)
btn5.grid(row=3,column=1)

btn6=tk.Button(interface, text="6", width=10, height=5)
btn6.grid(row=3,column=2)

btn7=tk.Button(interface, text="7", width=10, height=5)
btn7.grid(row=2,column=0)

btn8=tk.Button(interface, text="8", width=10, height=5)
btn8.grid(row=2,column=1)

btn9=tk.Button(interface, text="9", width=10, height=5)
btn9.grid(row=2,column=2)

btnadd=tk.Button(interface, text="+", width=10, height=5, command=add)
btnadd.grid(row=2,column=3)

btnsub=tk.Button(interface, text="-", width=10, height=5, command=sub)
btnsub.grid(row=3,column=3)

btnmult=tk.Button(interface, text="*", width=10, height=5, command=mult)
btnmult.grid(row=4,column=3)

btndiv=tk.Button(interface, text="/", width=10, height=5, command=div)
btndiv.grid(row=5,column=3)

btnsubmit=tk.Button(interface, text="=", width=10, height=5, command=submit)
btnsubmit.grid(row=5,column=2)

btnclear=tk.Button(interface, text="Clear", width=10, height=5, command=clear)
btnclear.grid(row=5,column=0)

interface.mainloop()
display()