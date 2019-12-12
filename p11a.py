
# meng-import Tkinter
from tkinter import *


def exit():
    print('close')
    quit()

# Membuat Object Tkinter
TkObject = Tk()

# Membuat Frame Pertama
TopFrame = Frame(TkObject)
TopFrame.pack(side=TOP, fill=X)

# Membuat Frame Pertama
BottomFrame = Frame(TkObject)
BottomFrame.pack(side=LEFT, fill=X)

# Membuat Label dan menempatkannya pada Top Frame
label1 = Label(TopFrame, text="DATA DIRI",font=('Arial,24'))
label1.pack(side=TOP)

# Membuat Label dan menempatkannya pada Bottom Frame
spacing= Label(BottomFrame,text='')
label2 = Label(BottomFrame, text="Nama:            Arindra Hning Adhepta")
label3 = Label(BottomFrame, text="NIM:               L200190065                 ")
label4 = Label(BottomFrame, text="Alamat:         Solo                              ")
label5 = Label(BottomFrame, text="Moto:             Chill Santuy                  ")
label6 = Label(BottomFrame, text="Pekerjaan:     Mahasiswa                    ")
butt=Button(TkObject, text="TUTUP", command=exit)

spacing.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()
label6.pack()
butt.pack(side=BOTTOM)


# Menampilkan Window
TkObject.mainloop()


