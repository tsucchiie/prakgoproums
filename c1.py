from tkinter import *
from tkinter import messagebox

apl = Tk()
apl.title("Apliaksi dengan berbagai widget")

L1 = Label(apl, text="Nama Mahasiswa")
L1.grid(row=0, column=0)

nama = StringVar()
E1 = Entry(apl, textvariable=nama)
E1.grid(row=0, column=1)

def hello():
    messagebox.showinfo("Title, :Hello", nama.get())

B1 = Button(apl, text="Hello", command=hello)
B1.grid(row=1, column=1)

apl.mainloop()
