import tkinter as tk
from tkinter import messagebox

mainWindow = tk.Tk()
mainWindow.title("CALCULATOR")

HL1=tk.Label(mainWindow, text="First Number")
HL1.pack()

nf1 = tk.Entry(mainWindow)
nf1.pack()

HL2=tk.Label(mainWindow, text="Second Number")
HL2.pack()

nf2=tk.Entry(mainWindow)
nf2.pack()

operations = tk.Label(mainWindow, text="Operations")
operations.pack()

def inp():
    first = nf1.get()
    second = nf2.get()

    try:
        first = int(first)
        second = int(second)

        return first, second
    except ValueError:
        if ((len(nf1.get()) == 0) or (len(nf2.get()) == 0)):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")
        quit(0)

def add():
    n1,n2= inp()
    res=n1+n2
    result_label.config(text="Operation result is: " +
                             str(res))

def sub():
    n1, n2 = inp()
    res=n1-n2
    result_label.config(text="Operation result is: " +
                             str(res))

def mul():
    n1, n2 = inp()
    res=n1*n2
    result_label.config(text="Operation result is: " +
                             str(res))

def div():
    n1, n2 = inp()
    if(n2!=0):
        res=n1/n2
        result_label.config(text="Operation result is: " +
                                 str(res))
    else:
        messagebox.showerror("Error", "Cannot divide the value by 0.")


b1=tk.Button(mainWindow, text="+", command=lambda : add())
b1.pack()
b2=tk.Button(mainWindow, text="-", command=lambda : sub())
b2.pack()
b3=tk.Button(mainWindow, text="*", command=lambda : mul())
b3.pack()
b4=tk.Button(mainWindow, text="/", command=lambda : div())
b4.pack()

result_label = tk.Label(mainWindow, text="Operations result is:")
result_label.pack()

mainWindow.mainloop()