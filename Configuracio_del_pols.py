import time, serial, serial.tools.list_ports, random, os, sys
from ctypes import Array
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import Tk, Label, Button, Radiobutton, IntVar
from PIL import Image, ImageTk


def clicked():
    global numV, temps0V, temps1V, periV, freqV, portV, trenV, temps2V, temps3V
    Ok = True

    try:
        freqV = float(freqE.get())
        periV = 1000 / freqV
    except ValueError:
        try:
            periV = float(periE.get())
            freqV = 1000 / periV
        except ValueError:
            messagebox.showerror('Value Error', "Freqüència o Període:"
                                                "\nEntrada invàlida per a nombres enters amb base 10")
            Ok = False

    try:
        temps1V = float(temps1E.get())
        temps0V = periV - temps1V
        if temps0V <= 0:
            messagebox.showwarning('Value Error', "Error de concordança entre el període i la durada del pols")
            Ok = False

    except ValueError:
        messagebox.showerror('Value Error', "Durada del pols :"
                                            "\nEntrada invàlida per a nombres enters amb base 10")
        Ok = False

    try:
        numV = int(numE.get())
    except ValueError:
        messagebox.showerror('Value Error', "Nombre de polsos:"
                                            "\nEntrada invàlida per a nombres naturals amb base 10")
        Ok = False

    try:
        portV = portC.get().split(" -")
    except ValueError:
        messagebox.showerror('Value Error', "Port:"
                                            "\nEntrada invàlida per al nom del port")
        Ok = False

    if trenVar.get() == 1:
        try:
            trenV = int(trenE.get())
        except ValueError:
            messagebox.showerror('Value Error', 'Tren de polsos:'
                                                '\nEntrada invàlida per a nombres naturals amb base 10')
            Ok = False
        try:
            temps2V = float(temps2E.get())
            temps3V = temps2V - periV * numV
            if temps3V < 0:
                messagebox.showerror('Value Error', 'Durada del tren:'
                                                    '\nError de concordança entre la durada del tren i la durada del '
                                                    'pols')
                Ok = False
        except ValueError:
            messagebox.showerror('Value Error', 'Durada del tren:'
                                                '\nEntrada invàlida per a nombres enters amb base 10')
            Ok = False

    if Ok:
        if trenVar.get() == 0:
            resposta = messagebox.askokcancel('Informació del pols a enviar',
                                "\nNombre de polsos: " + str(numV) + "\nDurada del pols: " + str(temps1V) + " ms" +
                                "\nTemps entre polsos: " + str(temps0V) + " ms" + "\n\nFreqüència: " +
                                str(round(freqV, 3)) + " Hz" + "\nPeríode: " + str(round(periV, 3)) + " ms" +
                                "\n\nPort: " + portV[0] + "\n\n\n")
            if resposta: 
                comunicacion(portV[0], temps0V, temps1V, numV)
        else:
            resposta = messagebox.askokcancel('Informació del pols a enviar',
                                "\nNombre de polsos: " + str(numV) + "\nDurada del pols: " + str(temps1V) + " ms" +
                                "\nTemps entre polsos: " + str(temps0V) + " ms" + "\n\nFreqüència: " +
                                str(round(freqV, 3)) + " Hz" + "\nPeríode: " + str(round(periV, 3)) + " ms" +
                                "\n\nPort: " + portV[0] + "\n\nNombre de repeticions: " + str(trenV) +
                                "\nDurada tren de polsos: " + str(temps2V) + " ms" + "\nTemps entre repeticions: " +
                                str(round(temps3V,3)) + " ms" + "\n\n\n")
            if resposta: 
                comunicacion(portV[0], temps0V, temps1V, numV, trenV, temps3V )


def lecturaports():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)

def inici(port):
    global ser
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = port
    ser.open()
    ser.setRTS(True)
    ser.setRTS(False)

def comunicacion(port, temps0, temps1, nombrePols, repeticio=1, temps3=0):
    # ser = serial.Serial()
    # ser.baudrate = 9600
    if ser.port != port:
        ser.port = port
    # ser.open()
    # ser.setRTS(True)
    # ser.setRTS(False)
    # time.sleep(0.5)

    for i in range(repeticio):
        for j in range(nombrePols):
            
            t = time.time()
            ser.setRTS(True)
            while time.time() - t < temps1/1000:
                pass

            t = time.time()
            ser.setRTS(False)
            while time.time() - t < temps0/1000:
                pass

        t = time.time()
        while time.time() - t < temps3/1000:
            pass

    # ser.close()

def freqRF():
    freqE.delete(first=0, last=22)
    freqE.configure(state="abled")
    periE.delete(first=0, last=22)
    periE.configure(state="disabled")


def periRF():
    freqE.delete(first=0, last=22)
    freqE.configure(state="disabled")
    periE.delete(first=0, last=22)
    periE.configure(state="abled")


def about():
    window2 = Toplevel(window)
    window2.title("Sobre nosaltres")
    window2.geometry("560x230")

    img = Image.open(resource_path("2.png"))
    img = img.resize((544, 218), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    about_label = Button(window2, image=img, command=modesuprem)
    about_label.pack()

    window2.mainloop()


def modesuprem():
    frases = ["Wake up and make your dreams come true",
              "Never forget to make people happier every day",
              "Don’t look back in order to focus on the future",
              "Hello! It’s your best friend, your dog",
              "¡Sal ahí fuera y brilla!",
              "Todo lo bueno empieza hoy",
              "Sueña a lo grande",
              "Sueños, planes y mil historias que cumplir",
              "Soy una auténtica joya, así que cuídame bien",
              "La felicidad se lleva dentro",
              "Soy la creme de la creme",
              "El verano es la repera debajo de una palmera",
              "Las mejores aventuras son las que vivimos juntos",
              "Let me take you on an adventure",
              "Prepare for summer",
              "Cada vez que viajo, ¡doy botes de alegría!",
              "Soy la mar de salada",
              "Mamá, tu sonrisa lo vale todo",
              "La vida es un bonito viaje",
              "Abuelo eres genial, como tus abrazos no hay nada igual",
              "En esta familia nos damos besos, achuchones y mimitos a montones",
              "Necesito más espacio",
              "¡Sonríe! Hoy puede ser tu día",
              "La vida está hecha para vivir aventuras",
              "Voy a vivir un millón de aventuras",
              "Déjame que te bese, y nos levantaremos con la cama hecha un trece",
              "Rumbo a mi nuevo lugar favorito",
              "You look wonderful today",
              "Hoy estoy radiante",
              "Sois unos padres que valen su peso en oro",
              "Tienes el guapo subido",
              "No hay mal que 100 años dure ni nada que este botiquín no cure",
              "Si puedes soñarlo, puedes hacerlo",
              "Hoy es un buen día para sonreír",
              "Ser feliz a tu lado es fácil",
              "Un café con leche con doble de alegría y buen rollo por la mañana",
              "Las cosas buenas pasan a quienes las esperan",
              "Las mejores cosas pasan a los que van a por ellas",
              "Si no tardas mucho te espero toda la vida",
              "No se trata de dónde estés sino de dónde quieres llegar",
              "Lo único imposible es aquello que no intentas",
              "Haz lo que te dé la real gana, pero que te haga feliz",
              "Que tus sueños sean más grandes que tus miedos",
              "Todo saldrá bien porque tú eres la leche",
              "Cambia tu forma de ver las cosas y las cosas cambiarán",
              "No te creas más que nadie, ni te creas menos que alguien",
              "Traza la meta, hoy es tu día para conseguirlo",
              "No esperes que nadie haga por ti lo que tú puedes conseguir",
              "Llora. Tienes sentimientos",
              "Enamórate de tus ideas",
              "Ríe, sé positivo, todo saldrá bien",
              "Los tiempos son malos, malísimos, pero la pasión y buenas ideas triunfan",
              "¿Tomas algo para ser feliz? Sí, decisiones",
              "Cosas no aburridas para ser la mar de feliz",
              "Para alcanzar algo que no has tenido, tendrás que hacer algo que no hiciste",
              "Si no metes la pata, no conseguirás nada. ¡Equivocate sin miedo!",
              "¡Esta panda se va de parranda!",
              "Con sólo mirarte me erizo",
              "Tú siempre con la misma historia",
              "Contigo me parto",
              "365 días para llegar hasta donde te propongas",
              "Bienvenidos los días frescos para las chaquetas gustosas",
              "Hoy estoy tan feliz que sonríen hasta los dedos de mis pies",
              "Por ti estoy que ardo",
              "Mejor dragón majete, que príncipe zoquete",
              "Hoy me pongo las pilas",
              "La vida empieza cada cinco minutos",
              "Encontrarás significado en la vida si lo creas",
              "Donde una puerta se cierra, otra se abre",
              "Fueron semillas mis errores",
              "Si la vida te da un limón, haz limonada",
              "La felicidad no es algo hecho. Proviene de tus propias acciones",
              "La gente positiva cambia el mundo, mientras que la negativa lo mantiene como está",
              "Una actitud fuertemente positiva creará más milagros que cualquier droga",
              "Todo puede tener belleza, aún lo más horrible",
              "Nadie que haya dado lo mejor de sí mismo lo ha lamentado",
              "Enamórate de tu existencia",
              "Toda persona tiene capacidad para cambiarse a sí misma",
              "Hay una fuerza motriz más poderosa que el vapor, la electricidad y la energía atómica: la voluntad",
              "Nunca eres demasiado viejo para tener otra meta u otro sueño",
              "Seamos realistas y hagamos lo imposible",
              "El triunfo del verdadero hombre surge de las cenizas del error",
              "No llores porque se acabó, sonríe porque sucedió",
              "El optimismo es la fe que conduce al logro; nada puede realizarse sin esperanza",
              "La paciencia es amarga, pero su fruto es dulce",
              "Cada problema tiene en sus manos un regalo para ti",
              "Incluso la noche más oscura terminará con la salida del Sol",
              "Si miras al Sol, no verás las sombras",
              "La felicidad suele colarse por una puerta que no sabías que habías dejado abierta",
              "El aprendizaje es un regalo. Incluso cuando el dolor es tu maestro",
              "Los únicos interesados en cambiar el mundo son los pesimistas, porque los optimistas están encantados "
              "con lo que hay",
              "Soy optimista. No parece muy útil ser cualquier otra cosa",
              "Todos piensan en cambiar el mundo, pero nadie piensa en cambiarse a sí mismo",
              "Las personas cambian cuando se dan cuenta del potencial que tienen para cambiar la realidad",
              "Cada día me miro en el espejo y me pregunto: 'Si hoy fuese el último día de mi vida, ¿querría hacer lo "
              "que voy a hacer hoy?'. Si la respuesta es 'No' durante demasiados días consecutivos, sé que debo "
              "cambiar algo",
              "Ríete todos los días y no habrás desperdiciado ni un solo momento de tu vida",
              "Si exagerásemos nuestras alegrías, como hacemos con nuestras penas, nuestros problemas perderían "
              "importancia",
              "Bueno es tener la alegría en casa y no haber de buscarla fuera",
              "Cuando brotan esperanzas, el corazón se aprovecha y empieza a actuar por su cuenta",
              "Los verdaderos grandes son los de ánimo grande",
              "Lo que no te mata te hace más fuerte",
              "La sabiduría más verdadera es una resuelta determinación",
              "El fracaso es una buena oportunidad para empezar de nuevo con más inteligencia",
              "Todos nuestros sueños se pueden volver realidad si tenemos la valentía de perseguirlos",
              "La mejor manera de predecir el futuro es creándolo",
              "Poseer menos llaves permite abrir más puertas",
              "Una actitud sana es contagiosa. Deja que otros se impregnen de ella",
              "El optimismo perpetuo es un multiplicador de fuerzas",
              "La mejor manera de olvidar las malas cosas de la vida es aprender a recordar las cosas buenas",
              "Cuando una puerta se cierra, muchas más se abren",
              "Siempre parece imposible hasta que se hace",
              "La corrección hace mucho, pero la valentía hace más",
              "Cree que la vida merece ser vivida y la creencia ayudará a crear el hecho",
              "Si puedes soñarlo, puedes hacerlo",
              "Estoy agradecido a todos los que me dijeron no. Gracias a ellos lo estoy haciendo por mí mismo",
              " El entusiasmo mueve el mundo",
              "El poder de la imaginación nos vuelve infinitos ",
              "Sin lluvia no habría arcoiris",
              "Dentro de la dificultad yace la oportunidad",
              "Una vez has elegido la opción de la esperanza, cualquier cosa es posible",
              "De una pequeña semilla puede nacer un poderoso árbol",
              "En la vida hay tantas ocasiones especiales como veces elegimos celebrarlas",
              "La vida no tiene más limitaciones que las que uno se ponga a sí mismo",
              "Quien es feliz hará a otros felices",
              "De nuestras dificultades nacen milagros",
              "Ganar no lo es todo, pero querer ganar sí",
              "Cree que puedes y ya habrás hecho medio camino",
              "Nunca es tarde para ser quien podrías haber sido",
              "No importa cuán lento camines mientras camines",
              "Soñar es una manera de hacer planes",
              "Aprender es un regalo. Incluso el dolor es un maestro",
              "Si puedes cambiar tu mente, puedes cambiar el mundo",
              "La diferencia entre ganar y perder suele ser no dándose por vencido",
              "No importa la situacón, recuérdate esta idea: 'tengo opciones'",
              "La vida no te está sucediendo. La vida te está respondiendo",
              "Cuando el camino parezca imposible, enciende el motor",
              "La única discapacidad en la vida es la mala actitud",
              "Haz que tu optimismo se vuelva realidad",
              "Aprende a sonreir en cualquier situación. Tómatelo como una oportunidad para expresar tu fortaleza",
              "No podemos controlar el viento, pero sí ajustar las velas",
              "Mi optimismo lleva botas pesadas y es ruidoso",
              "El pesimismo lleva a la debilidad y el optimismo al poder",
              "La vida cambia muy rápidamente, y de un modo positivo, si la dejas",
              "La única diferencia entre un día malo y uno bueno es tu actitud",
              "El pensamiento positivo te dejará usar las habilidades que tienes, y eso es fantástico",
              "Tener una actitud positiva es preguntarse cómo puede hacerse algo, más que decir que no puede hacerse",
              "Cuando piensas en positivo, las cosas ocurren",
              "No importa a quién conozcas a lo largo de tu vida, tomarás algo de ellos, ya sea positivo o negativo",
              "Mantén una mente positiva y ríete de todo",
              "Tu corazón está lleno de semillas esperando germinar",
              "Rodéate de gente positiva",
              "No llores porque se ha terminado, sonríe porque ha ocurrido",
              "Lo negativo es tan importante como lo positivo",
              "Vuelve a intentarlo. Fracasa de nuevo. Fracasa mejor.",
              "Escribe en tu corazón que cada día es el mejor día de tu vida",
              "La felicidad no es la ausencia de problemas sino la capacidad de lidiar con ellos",
              "Todas las cosas son difíciles hasta que son fáciles",
              "La vida no tiene mando a distancia. Levántate y cámbiala por tus propios medios",
              "Un mundo mejor no es solo posible, sino que está llegando",
              "El mejor tipo de felicidad es el hábito que te apasiona",
              "Aspira a ser la persona a la que más admires",
              "Somos dioses en una crisálida",
              "Mira hacia atrás y sonríe ante los peligros pasados",
              "El amor es ese micro-momento de calidez y conexión que compartimos con otro ser vivo",
              "La buena vida es un proceso, no un estado",
              "No hay fracaso, tan solo éxito inacabado",
              "Amarse a uno mismo es el comienzo de un romance de por vida",
              "Ando lentamente, pero nunca camino hacia atrás",
              "Una buena risa cura muchas heridas",
              "No importa la edad, siempre hay algo bueno que superar",
              "La victoria siempre es posible para quien se niega a rendirse",
              "La música es la poesía del aire",
              "Las verdaderas historias de amor nunca terminan",
              "Un amigo es alguien con quien te atreves a ser tú mismo",
              "Si nunca has fallado, nunca has vivido",
              "De las dificultades nacen milagros",
              "La vida es como el jazz... mejor si es improvisada",
              "Si das luz, la oscuridad se irá por sí misma",
              "El mundo está lleno de magia que espera pacientemente a que nuestro ingenio se afine",
              "El hombre nunca ha hecho un material tan resistente como el alma resiliente",
              "¡Alumbra el mañana con el hoy!",
              "Vivimos unos 30.000 días, y en cada uno de ellos decidimos cambiar nuestra realidad... o bien dejarnos "
              "llevar",
              "El pensamiento está sobrevalorado. Hay que pensar menos y sentir más",
              "Vivimos unos 30.000 días, y en cada uno de ellos decidimos cambiar nuestra realidad... o bien dejarnos "
              "llevar",
              "El duelo es necesario en ciertos momentos de la vida. Igual de necesario que saber devolverle a "
              "nuestra existencia ciertos objetivos que nos impulsen a continuar",
              "Lo más importante es mantenerse positivo"]

    messagebox.showinfo("Mode suprem", '\tBon dia\n\n"' + frases[random.randint(0, len(frases) - 1)] + '"')


def color():
    messagebox.showinfo("Color cables", "CABLE BLANC (+)\nCABLE VERD (-)")


def trenCF():
    trenE.delete(first=0, last=22)
    temps2E.delete(first=0, last=22)
    if trenVar.get() == 0:
        trenE.configure(state="disabled")
        temps2E.configure(state="disabled")
    else:
        trenE.configure(state="abled")
        temps2E.configure(state="abled")


def polssimple():
    global freqV, periV, portV
    Ok = True

    try:
        freqV = float(freqE.get())
        periV = 1 / freqV
    except ValueError:
        try:
            periV = float(periE.get())
            freqV = 1 / periV
        except ValueError:
            messagebox.showerror('Value Error', "Freqüència o Període:"
                                                "\nEntrada invàlida per a nombres enters amb base 10")
            Ok = False

    try:
        portV = portC.get().split(" -")
    except ValueError:
        messagebox.showerror('Value Error', "Port:"
                                            "\nEntrada invàlida per al nom del port")
        Ok = False

    if Ok:
        resposta = messagebox.askokcancel('Informació del pols a enviar',
                            "\nNombre de polsos: 1\nDurada del pols: " + str(periV/2) + " ms" +
                            "\nTemps entre polsos: " + str(periV/2) + " ms" + "\n\nFreqüència: " +
                            str(round(freqV, 3)) + " Hz" + "\nPeríode: " + str(round(periV, 3)) + " ms" +
                            "\n\nPort: " + portV[0] + "\n\n\n")
        if resposta: 
                comunicacion(portV[0], periV/2, periV/2, 1)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def refrescar(port=0):
    global portC
    portC = Combobox(window, width=40, values=list(serial.tools.list_ports.comports()))

    try:
        portC.current(port)
    except TclError:
        messagebox.showerror('Port Error', 'No hi ha cap port conectat')

    portC.grid(column=2, row=13)

def refrescar2(port=0):
    portC2 = Combobox(ask, width=40, values=list(serial.tools.list_ports.comports()))
    try:
        portC2.current(port)
    except TclError:
        messagebox.showerror('Port Error', 'No hi ha cap port conectat')
    portC2.grid(column=0, row=3)

def ask_multiple_choice_question(prompt, options):
    global portC2, ask
    ask = Toplevel(window)
    ask.title("Configuració del pols - Selecció de port")

    if prompt:
        Label(ask, text=prompt).grid(column=0, row=0)
    
    Label(ask, text="").grid(column=0, row=2)
    
    portC2 = Combobox(ask, width=40, values=options)
    try:
        portC2.current(0)
    except TclError:
        messagebox.showerror('Port Error', 'No hi ha cap port conectat')
    portC2.grid(column=0, row=3)
    
    Label(ask, text="").grid(column=0, row=4)
    Button(ask, text="Refrescar", command=refrescar2).grid(column=0, row=5) 
    Label(ask, text="").grid(column=0, row=6)
    Button(ask, text="Acceptar", command=clicked2).grid(column=0, row=7) 
    Label(ask, text="").grid(column=0, row=8)
    ask.mainloop()

    # if v.get() == 0: 
    #     return None

    # refrescar(v.get())
    # return options[v.get()]

def clicked2():
    global portV2
    Ok = True

    try:
        portV2 = portC2.get().split(" -")
    except ValueError:
        messagebox.showerror('Value Error', "Port:"
                                            "\nEntrada invàlida per al nom del port")
        Ok = False
    
    if Ok:
        inici(portV2[0])
        refrescar(portC2.current())
        ask.destroy()
        messagebox.showinfo('Configuració inicial', 'Configuració finalitzada, ja pot connectar la màquina')



window = Tk()
window.title("Configuració del pols")
window.geometry('450x560')
icon = PhotoImage(file=resource_path('1r.png'))
window.call('wm', 'iconphoto', window, icon)

menu = Menu(window)
window.config(menu=menu)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Ajuda', menu=helpmenu)
helpmenu.add_command(label='Color cables', command=color)
helpmenu.add_command(label='Sobre nosaltres', command=about)

optionmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Opcions', menu=optionmenu)
optionmenu.add_command(label='Pols simple', command=polssimple)
optionmenu.add_command(label='Refrescar llistat de ports series', command=refrescar)


numVar = IntVar()
temps1Var = IntVar()
numVar.set(0)
temps1Var.set(0)

temps1L = Label(window, text="Durada del pols [ms]")
temps1L.grid(column=2, row=1)
temps1E = Entry(window, width=10)
temps1E.grid(column=2, row=2)

b3 = Label(window, text="")
b3.grid(column=2, row=3)

numL = Label(window, text="Nombre de polsos")
numL.grid(column=2, row=4)
numE = Entry(window, width=10)
numE.grid(column=2, row=5)

b6 = Label(window, text="")
b6.grid(column=2, row=6)

freqperiL = Label(window, text="Freqüència [Hz] / Període [ms]")
freqperiL.grid(column=2, row=7)
freqR = Radiobutton(window, text='Freqüència', value=1, command=freqRF)
periR = Radiobutton(window, text='Període', value=2, command=periRF)
freqR.grid(column=1, row=8)
periR.grid(column=3, row=8)
freqE = Entry(window, width=10, state='disabled')
freqE.grid(column=1, row=9)
periE = Entry(window, width=10, state='disabled')
periE.grid(column=3, row=9)

b10 = Label(window, text="")
b10.grid(column=2, row=10)
b11 = Label(window, text="")
b11.grid(column=2, row=11)

portL = Label(window, text="Port COM")
portL.grid(column=2, row=12)

# portC = Combobox(window, width=40, values=list(serial.tools.list_ports.comports()))
# try:
#     portC.current(1)
# except TclError:
#     messagebox.showerror('Port Error', 'No hi ha cap port conectat')
# portC.grid(column=2, row=13)

b14 = Label(window, text="")
b14.grid(column=2, row=14)
b15 = Label(window, text="")
b15.grid(column=2, row=15)

trenVar = IntVar()
trenCh = Checkbutton(text="Tren de polsos", command=trenCF, variable=trenVar, onvalue=1, offvalue=0)
trenVar.set(0)
trenCh.grid(column=2, row=16)

b16 = Label(window, text="")
b16.grid(column=2, row=17)

trenL = Label(window, text="Nombre de repeticions")
trenL.grid(column=2, row=18)
trenE = Entry(window, width=10, state='disabled')
trenE.grid(column=2, row=19)

b20 = Label(window, text="")
b20.grid(column=2, row=20)

temps2L = Label(window, text="Durada del tren [ms]")
temps2L.grid(column=2, row=21)
temps2E = Entry(window, width=10, state='disabled')
temps2E.grid(column=2, row=22)

b23 = Label(window, text="")
b23.grid(column=2, row=23)
b24 = Label(window, text="")
b24.grid(column=2, row=24)

btn = Button(window, text="Enviar pols", command=clicked)
btn.grid(column=2, row=25)


messagebox.showwarning("Configuració inicial", "Desconnecti la màquina abans de continuar")
ask_multiple_choice_question("En quin port està connectat el TTL?", list(serial.tools.list_ports.comports()))

window.mainloop()
