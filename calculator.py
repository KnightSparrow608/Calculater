import tkinter as tk

interface = tk.Tk()
interface.title("Calculator")
interface.geometry("350x275")

button0=tk.Button(interface, text="0")
button0.grid(row=5,column=1)
button1=tk.Button(interface, text="1")
button1.grid(row=4,column=0)
button2=tk.Button(interface, text="2")
button2.grid(row=4,column=1)
button3=tk.Button(interface, text="3")
button3.grid(row=4,column=2)
button4=tk.Button(interface, text="4")
button4.grid(row=3,column=0)
button5=tk.Button(interface, text="5")
button5.grid(row=3,column=1)
button6=tk.Button(interface, text="6")
button6.grid(row=3,column=2)
button7=tk.Button(interface, text="7")
button7.grid(row=2,column=0)
button8=tk.Button(interface, text="8")
button8.grid(row=2,column=1)
button9=tk.Button(interface, text="9")
button9.grid(row=2,column=2)

def add(): 
    print ("add")

def sub():
    print ("sub")

def mult():
    print ("mult")

def div():
    print ("div")

interface.mainloop()