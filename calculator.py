from tkinter import * 
import tkinter as tk

equation = 0
interface = tk.Tk()

interface.title("Calculator")
interface.geometry("315x400")

expression_field = Entry(interface, textvariable=equation)
expression_field.grid(row=1, columnspan=4, ipadx=100, ipady=25)

equation = StringVar()

button0=tk.Button(interface, text="0", width=10, height=5)
button0.grid(row=5,column=1)
button1=tk.Button(interface, text="1", width=10, height=5)
button1.grid(row=4,column=0)
button2=tk.Button(interface, text="2", width=10, height=5)
button2.grid(row=4,column=1)
button3=tk.Button(interface, text="3", width=10, height=5)
button3.grid(row=4,column=2)
button4=tk.Button(interface, text="4", width=10, height=5)
button4.grid(row=3,column=0)
button5=tk.Button(interface, text="5", width=10, height=5)
button5.grid(row=3,column=1)
button6=tk.Button(interface, text="6", width=10, height=5)
button6.grid(row=3,column=2)
button7=tk.Button(interface, text="7", width=10, height=5)
button7.grid(row=2,column=0)
button8=tk.Button(interface, text="8", width=10, height=5)
button8.grid(row=2,column=1)
button9=tk.Button(interface, text="9", width=10, height=5)
button9.grid(row=2,column=2)
btnadd=tk.Button(interface, text="+", width=10, height=5)
btnadd.grid(row=2,column=3)
btnsub=tk.Button(interface, text="-", width=10, height=5)
btnsub.grid(row=3,column=3)
btnmult=tk.Button(interface, text="*", width=10, height=5)
btnmult.grid(row=4,column=3)
btndiv=tk.Button(interface, text="/", width=10, height=5)
btndiv.grid(row=5,column=3)

def add(): 
    print ("add")

def sub():
    print ("sub")

def mult():
    print ("mult")

def div():
    print ("div")

interface.mainloop()