from tkinter import *
from tkinter import messagebox

apl = Tk()

apl.title("Kalkulator")

L = Label(apl, text="Kalkulator", font=("Arial", 20))
L.grid(row=0, column=0)
L1 = Label(apl, text="Angka 1")
L1.grid(row=1, column=0, sticky="W", columnspan=2)
a1 = StringVar()
E1 = Entry(apl, textvariable=a1)
E1.grid(row=1, column=1)

L2 =Label(apl, text="Angka 2")
L2.grid(row=2, column=0, sticky="W", columnspan=2)
a2 = StringVar()
E2 = Entry(apl, textvariable=a2)
E2.grid(row=2, column=1)

def tambah():
    x = float(a1.get())
    y = float(a2.get())
    z = x + y
    E4.config(text = z)
def kurang():
    x = float(a1.get())
    y = float(a2.get())
    z = x - y
    E4.config(text = z)
def kali():
    x = float(a1.get())
    y = float(a2.get())
    z = x * y
    E4.config(text = z)
def bagi():
    x = float(a1.get())
    y = float(a2.get())
    z = x / y
    E4.config(text = z)
    
B1 = Button(apl, text="+", command=tambah, width=6)
B1.grid(row=3, column=0, sticky="W")
B2 = Button(apl, text="-", command=kurang, width=6)
B2.grid(row=3, column=1)
B3 = Button(apl, text="x", command=kali, width=6)
B3.grid(row=3, column=2)
B4 = Button(apl, text=":", command=bagi, width=6)
B4.grid(row=3, column=3)


L4 =Label(apl, text="Hasil")
L4.grid(row=4, column=0, sticky="W")
a4 = StringVar()
E4 = Label(apl, text="")
E4.grid(row=4, column=1)
apl.mainloop()
