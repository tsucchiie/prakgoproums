from tkinter import *
from tkinter import messagebox

apl = Tk()
apl.title("Apliaksi dengan berbagai widget")


L=Label(apl,text="Data diri",font=('Arial',18))
L.grid(row=0,column=0)

L1=Label(apl,text="Nama")
L1.grid(row=1,column=0,sticky="W")
E1=Label(apl,text="hastaka juan jaya saputra")
E1.grid(row=1, column=1)

L2=Label(apl,text="NIM")
L2.grid(row=2,column=0,sticky="W")
E2=Label(apl,text="L200190015")
E2.grid(row=2, column=1)

L3=Label(apl,text="Buku favorite")
L3.grid(row=3,column=0,sticky="W")
E3=Label(apl,text="dilan 1991")
E3.grid(row=3, column=1)

L4=Label(apl,text="idola")
L4.grid(row=4,column=0,sticky="W")
E4=Label(apl,text="Mia Khalifa")
E4.grid(row=4, column=1)

L5=Label(apl,text="Motto")
L5.grid(row=5,column=0,sticky="W")
E5=Label(apl,text="Dont be Afraid")
E5.grid(row=5, column=1)


B1 = Button(text="Tutup", command=quit)
B1.grid(row=6, column=1)

apl.mainloop()
