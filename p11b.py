##import tkinter
##
##inp1= Entry(TkObject)
##inp2= Entry(TkObject)
##
##inp1.grid(row=0,column=0)
##inp2.grid(row=1,column=0)
##
##
##TkObject.mainloop()



# Meng-import module tkinter
from tkinter import *

# Membuat Object Tkinter
TkObject = Tk()

# Membuat widget label header
Header = Label(TkObject, text="KALKULATOR SEDERHANA")
# Memasukan label header kedalam Grid
Header.grid(columnspan=2)

# Membuat widget label serta entry untuk username dan password
label1 = Label(TkObject, text="Angka 1")
label2 = Label(TkObject, text="Angka 2")
Entry1 = Entry(TkObject)
Entry2 = Entry(TkObject)

# Memasukan widget label dan entry dari username dan password ke dalam grid
label1.grid(row=2, column=0, sticky=E)
label2.grid(row=3, column=0, sticky=E)

Entry1.grid(row=2, column=1)
Entry2.grid(row=3, column=1)

num=0
a=Entry1
b=Entry2
def plus():
    num=a+b
    return num

def mins():
    num=a-b
    return num

def kali():
    num=a*b
    return num

def bagi():
    num=a/b
    return num


button0 = Button(TkObject, text="PLUS [+]",command=plus)
button0.grid(row=4, column=0)

button1 = Button(TkObject, text="MINS [-]",command=mins)
button1.grid(row=4, column=1)

button2 = Button(TkObject, text="BAGI [:]",command=bagi)
button2.grid(row=5, column=0)

button3 = Button(TkObject, text="KALI [X]",command=kali)
button3.grid(row=5, column=1)

hasil=Label(TkObject, text="HASIL= {}".format(num), bg='red')

# Menjalankan program
TkObject.mainloop()
