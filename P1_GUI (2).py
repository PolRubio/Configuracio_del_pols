from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import ttl
import serial
import math

Ample = 0; Num = 0; TempsPols = 0; freqV = 0; Peri = 0;

def clicked():

    Ok = True

    # try:
    #
    #     Ample = float(ampleE.get())
    # except ValueError:
    #     messagebox.showinfo('ValueError','Ample del pols:\nEntrada invàlida per a nombres enters amb base 10')
    #     Ok = False


    try:
        Num = int(NumE.get())
    except ValueError:
        messagebox.showinfo('ValueError','Nombre de polsos:\nEntrada invàlida per a nombres enters amb base 10')
        Ok = False
    try:
        TempsPols = int(TempsPolsE.get())
        
    except ValueError:
        messagebox.showinfo('ValueError','Temps de durada del pols:\nEntrada invàlida per a nombres enters amb base 10')
        Ok = False

    try:
        Freq = float(freqE.get())
        Peri = 1/Freq
    except ValueError:
        try:
            Peri = float(periE.get())
            Freq = 1/Peri
        except ValueError:
            messagebox.showinfo('ValueError','Freqüència o Període:\nEntrada invàlida per a nombres enters amb base 10')
            Ok = False

    try:
        Port = puerto.get().split(" -")

    except ValueError:
        messagebox.showinfo('ValueError','Nombre de polsos:\nEntrada invàlida per a nombres enters amb base 10')
        Ok = False

    if(Ok):
        # print("Ample del pols: " + str(Ample) + "\nNombre de polsos: " + str(Num) + "\nFreqüència: " + str(Freq) + "\nPeríode: " + str(Peri) + "\n\n\n")
        texto = "\nNombre de polsos: " + str(Num) + "\nFreqüència: " + str(Freq) + "\nPeríode: " + str(Peri) + "\nPort: " + Port[0] + "\n\n\n"

        ttl.comunicacion(Port[0],Peri,Num,TempsPols)
        messagebox.showinfo('Pols enviat correctament',"\nNombre de polsos: " + str(Num) + "\nFreqüència: " + str(Freq) + "\nPeríode: " + str(round(Peri,2)) + "\nPort: " + Port[0]+"\nDurada: " + tempsTren + "\n\n\n")


def freq():
    freqE.delete(first=0,last=22)
    freqE.configure(state = "abled")
    periE.delete(first=0,last=22)
    periE.configure(state = "disabled")


def peri():
    freqE.delete(first=0,last=22)
    freqE.configure(state = "disabled")
    periE.delete(first=0,last=22)
    periE.configure(state = "abled")

def nombrePolsos ():

    NumE.delete(first=0,last=22)
    NumE.configure (state = "abled")
    TempsPolsE.delete (first = 0, last = 22)
    TempsPolsE.configure (state = "disabled")

def tempsTren ():

    NumE.delete(first=0,last=22)
    NumE.configure (state = "disabled")
    TempsPolsE.delete (first = 0, last = 22)
    TempsPolsE.configure (state = "abled")




window = Tk()
window.title("Configuració del pols")
window.geometry('520x400')


menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='About')
menu.add_cascade(label='Help', menu=new_item)
window.config(menu=menu)

# lbl1 = Label(window, text="Ample del pols [ms]")
# lbl1.grid(column=2, row=0)
# ampleE = Entry(window,width=10)
# ampleE.grid(column=2, row=1)
# ampleE.focus()
#
# b2 = Label(window, text="")
# b2.grid(column=2, row=2)

var1 = StringVar()
var2 = StringVar()
var1.set(0)
var2.set(0)

b5 = Label(window, text="")
b5.grid(column=2, row=5)


lbl3 = Label(window, text="Freqüència [Hz] / Període [ms]")
lbl3.grid(column=2, row=6)
freq = Radiobutton(window,text='Freqüència',variable = var1, value=1, command=freq)
peri = Radiobutton(window,text='Període',variable = var1, value=2, command=peri)
freq.grid(column=1, row=7)
peri.grid(column=3, row=7)
freqE = Entry(window,width=10, state='disabled')
freqE.grid(column=1, row=8)
periE = Entry(window,width=10, state='disabled')
periE.grid(column=3, row=8)

b62 = Label(window, text="")
b62.grid(column=2, row=5)

lbl41 = Label(window, text="Nombre de polsos / Durada del tren de polsos (s)")
lbl41.grid(column=2, row=3)

nombrePolsos = Radiobutton(window,text='Nombre de polsos',variable = var2, value= 1, command=nombrePolsos)
tempsTren = Radiobutton(window,text='Temps del tren',variable = var2, value= 2, command=tempsTren)
nombrePolsos.grid(column=1, row=4)
tempsTren.grid(column=3, row=4)
NumE = Entry(window,width=10, state='disabled')
NumE.grid(column=1, row=5)
TempsPolsE = Entry(window,width=10, state='disabled')
TempsPolsE.grid(column=3, row=5)

#lblnombre = Label(window, text="Nombre de polsos")
#lblnombre.grid(column=2, row=3)
#numE = Entry(window,width=10)
#numE.grid(column=2, row=4)


b9 = Label(window, text="")
b9.grid(column=2, row=9)
b10 = Label(window, text="")
b10.grid(column=2, row=10)

lbl4 = Label(window, text="Port COM")
lbl4.grid(column=2, row=11)
puerto = Combobox(window, width=40)


puerto['values'] = list(serial.tools.list_ports.comports())
try:
    puerto.current(0)
except TclError:
    messagebox.showerror('Port Error', 'No hi ha cap port conectat')
puerto.grid(column=2, row=12)
puerto.grid(column=2, row=12)

b13 = Label(window, text="")
b13.grid(column=2, row=13)
b14 = Label(window, text="")
b14.grid(column=2, row=14)


btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=15)
window.mainloop()
# image = PhotoImage(file="1.png")
# image = Label(window,image=image)
# image.grid(column=2, row=16)
#

# ttl.comunicacion('COM3',Freq,0)

