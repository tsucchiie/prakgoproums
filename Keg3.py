from tkinter import *
from tkinter import messagebox

apl = Tk()

apl.title("Kalkulator")

L = Label(apl, text="Bangun Geometri", font=("Arial", 20))
L.grid(row=0, column=0)
L1 = Label(apl, text="Parameter 1 sebagai jari jari:")
L1.grid(row=1, column=0, sticky="W")
par1 = StringVar()
E1 = Entry(apl, textvariable=par1)
E1.grid(row=1, column=1)

L2 =Label(apl, text="parameter 2 sebagai tinggi:")
L2.grid(row=2, column=0, sticky="W")
par2 = StringVar()
E2 = Entry(apl, textvariable=par2)
E2.grid(row=2, column=1)

pi=3.14
def hitung():
    x = float(par1.get())
    y = float(par2.get())
    z = 2 * pi * x * y
    E4.config(text = z)



L4 = Button(apl, text="Hasil", command=hitung)
L4.grid(row=4, column=0, sticky="W")
a4 = StringVar()
E4 = Label(apl, text="")
E4.grid(row=4, column=1)
apl.mainloop()
