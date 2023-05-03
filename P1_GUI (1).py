from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import ttl
import serial
from PIL import Image, ImageTk

Ample = 0
Num = 0
freqV = 0
Peri = 0


def clicked():
    global Num, Peri, freqV, Tren
    Ok = True

    # try:
    #
    #     Ample = float(ampleE.get())
    # except ValueError:
    #     messagebox.showinfo('ValueError','Ample del pols:\nEntrada invàlida per a nombres enters amb base 10')
    #     Ok = False

    try:
        Num = int(numE.get())
    except ValueError:
        messagebox.showerror('Value Error', 'Nombre de polsos:\nEntrada invàlida per a nombres enters amb base 10')
        Ok = False

    try:
        Freq = float(freqE.get())
        Peri = 1 / Freq
    except ValueError:
        try:
            Peri = float(periE.get())
            Freq = 1 / Peri
        except ValueError:
            messagebox.showerror('Value Error',
                                 'Freqüència o Període:\nEntrada invàlida per a nombres enters amb base 10')
            Ok = False

    try:
        Port = puerto.get().split(" -")
    except ValueError:
        messagebox.showerror('Value Error', 'Port:\nEntrada invàlida per al nom del port')
        Ok = False

    if var.get() == 1:
        try:
            Tren = int(trenE.get())
        except ValueError:
            messagebox.showerror('Value Error', 'Tren de polsos:\nEntrada invàlida per a nombres enters amb base 10')
            Ok = False

    if Ok:
        # print("Ample del pols: " + str(Ample) + "\nNombre de polsos: " + str(Num) + "\nFreqüència: " + str(Freq) +
        # "\nPeríode: " + str(Peri) + "\n\n\n")
        # texto = "\nNombre de polsos: " + str(Num) + "\nFreqüència: " + str(Freq) + "\nPeríode: " + str(
        #    Peri) + "\nPort: " + Port[0] + "\n\n\n"
        messagebox.showinfo('Pols enviat correctament',
                            "\nNombre de polsos: " + str(Num) + "\nFreqüència: " + str(Freq) + "\nPeríode: " + str(
                                round(Peri, 2)) + "\nPort: " + Port[0] + "\n\n\n")
        ttl.comunicacion(Port[0], Peri, Num)

def freq():
    freqE.delete(first=0, last=22)
    freqE.configure(state="abled")
    periE.delete(first=0, last=22)
    periE.configure(state="disabled")


def peri():
    freqE.delete(first=0, last=22)
    freqE.configure(state="disabled")
    periE.delete(first=0, last=22)
    periE.configure(state="abled")


def about():
    window2 = Toplevel(window)
    window2.title("Sobre nosaltres")
    window2.geometry("544x218")

    img1 = Image.open("3.png")
    img2 = img1.resize((544, 218), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img2)

    about_label = Label(window2, image=img3)
    about_label.pack()

    window2.mainloop()

def tren():
    trenE.delete(first=0, last=22)
    if var.get() == 0:
        trenE.configure(state="disabled")
    else:
        trenE.configure(state="abled")

window = Tk()
window.title("Configuració del pols")
window.geometry('420x400')
icon = PhotoImage(file='1r.png')
window.call('wm', 'iconphoto', window.w, icon)

menu = Menu(window)
window.config(menu=menu)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Ajuda', menu=helpmenu)

helpmenu.add_command(label='Sobre nosaltres', command=about)

# lbl1 = Label(window, text="Ample del pols [ms]")
# lbl1.grid(column=2, row=0)
# ampleE = Entry(window,width=10)
# ampleE.grid(column=2, row=1)
# ampleE.focus()
#
# b2 = Label(window, text="")
# b2.grid(column=2, row=2)


lblnombre = Label(window, text="Nombre de polsos")
lblnombre.grid(column=2, row=3)
numE = Entry(window, width=10)
numE.grid(column=2, row=4)

b5 = Label(window, text="")
b5.grid(column=2, row=5)

lbl3 = Label(window, text="Freqüència [Hz] / Període [ms]")
lbl3.grid(column=2, row=6)
freq = Radiobutton(window, text='Freqüència', value=1, command=freq)
peri = Radiobutton(window, text='Període', value=2, command=peri)
freq.grid(column=1, row=7)
peri.grid(column=3, row=7)
freqE = Entry(window, width=10, state='disabled')
freqE.grid(column=1, row=8)
periE = Entry(window, width=10, state='disabled')
periE.grid(column=3, row=8)

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

var = IntVar()
trenCh = Checkbutton(text="Tren de polsos", command=tren, variable=var, onvalue=1, offvalue=0)
var.set(0)
trenCh.grid(column=2, row=15)
trenE = Entry(window, width=10, state='disabled')
trenE.grid(column=2, row=16)


b17 = Label(window, text="")
b17.grid(column=2, row=17)
b18 = Label(window, text="")
b18.grid(column=2, row=18)

btn = Button(window, text="Enviar pols", command=clicked)
btn.grid(column=2, row=19)

window.mainloop()
