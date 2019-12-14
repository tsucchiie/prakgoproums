from tkinter import *
from tkinter import messagebox

apl = Tk()

apl.title("Data diri")

L = Label(apl, text="Data diri", font=("Arial", 20))
L.grid(row=0, column=0)
L1 = Label(apl, text="Nama Mahasiswa")
L1.grid(row=1, column=0, sticky="W")
nama = StringVar()
E1 = Entry(apl, textvariable=nama)
E1.grid(row=1, column=1)

L2 =Label(apl, text="NIM")
L2.grid(row=2, column=0, sticky="W")
nim = StringVar()
E2 = Entry(apl, textvariable=nim)
E2.grid(row=2, column=1)

L3 =Label(apl, text="Buku favorit")
L3.grid(row=3, column=0, sticky="W")
buku = StringVar()
E3 = Entry(apl, textvariable=buku)
E3.grid(row=3, column=1)

L4 =Label(apl, text="Idola di kalangan sahabat")
L4.grid(row=4, column=0, sticky="W")
idola = StringVar()
E4 = Entry(apl, textvariable=idola)
E4.grid(row=4, column=1)

L5 =Label(apl, text="Motto")
L5.grid(row=5, column=0, sticky="W")
motto = StringVar()
E5 = Entry(apl, textvariable=motto)
E5.grid(row=5, column=1)

def hello():
    messagebox.showinfo("Pesan", "Hallo!"+ "\n" +
                        'Nama: '+nama.get() + "\n" +
                        'NIM: '+nim.get() + "\n" +
                        'Buku: '+buku.get() + "\n" +
                        'Idola: '+idola.get() + "\n" +
                        'Motto: '+motto.get() 
                        )

B1 = Button(apl, text="Hello", command=hello)
B1.grid(row=6, column=0)
B2 = Button(apl, text="Tutup", command=apl.destroy)
B2.grid(row=6, column=1)
apl.mainloop()

