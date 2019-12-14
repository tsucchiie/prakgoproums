from tkinter import *
from tkinter import messagebox

apl = Tk()

apl.title("Judul Aplikasi")

L1 = Label(apl, text="Nama Mahasiswa")
L1.grid(row=0, column=0, sticky="W")
nama = StringVar()
E1 = Entry(apl, textvariable=nama)
E1.grid(row=0, column=1)

L2 =Label(apl, text="NIM")
L2.grid(row=1, column=0, sticky="W")
nim = StringVar()
E2 = Entry(apl, textvariable=nim)
E2.grid(row=1, column=1)

def hello():
    messagebox.showinfo("Pesan", "Hallo!"+ "\n" + nama.get() + "\n" + nim.get())

B1 = Button(apl, text="Hello", command=hello)
B1.grid(row=2, column=1)
apl.mainloop()
