from tkinter import *
from tkinter import messagebox, filedialog,Frame, Tk, BOTH, Text, Menu, END
from tkinter.filedialog import askopenfilename

root=Tk()
root.title('Tsuchie app')

def open_dialog():
        global proses
        target = [('Python files', '*.py'), ('All files', '*')]
        bukaFile = filedialog.Open(filetypes=target)
        isiFile = bukaFile.show()
        
        pathname=Label(text="Berkas:").grid(row=3 ,column=0,padx=20,pady=10)
        path=Label(text=isiFile).grid(row=3 ,column=1,padx=20,pady=10)
        proses=isiFile
        
        

def runprocess():

        global proses
        get=open(proses,'r')
        push=open('text.txt','w')
        push.writelines(get.readlines())

        get.close()
        push.close()

        success=Button( text='Berhasil Dibuat', bg='green')\
        .grid(row=4,column=1,padx=20,pady=10)
        


class autorun:

    def __init__ (self,master):
        self.master=master

        self.H1=Label(self.master, text='Proses Berkas',font=('Arial',15))\
        .grid(row=0,column=0,padx=20,pady=10)

        self.H2=Label(self.master, text='ScriptBy Arindra065',font=('Arial',8))\
        .grid(row=0,column=1,padx=20,pady=10)

        self.submit=Button(self.master, text='Pilih Berkas',command=open_dialog)\
        .grid(row=4,column=0,padx=20,pady=10)

        self.submit=Button(self.master, text='Proses Berkas',command=runprocess)\
        .grid(row=4,column=1,padx=20,pady=10)

    

autorun(root)

