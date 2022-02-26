
from time import sleep
from tkinter import *


root = Tk()
root.geometry("600x600")


def mainMenu():
    tittle_text = Label(root, text="Mi idea era mil veces mejor pero bueno. Habrá que hacer lo de los tontos")
    tittle_text.config(font=15)
    tittle_text.pack(pady=2)

    main_text = Label(root, text="Introduce el numero de zonas")
    main_text.pack(pady=80)
    main_text.config(font=15)

    s = Spinbox(root, from_=0, to=100000 ,increment=1)
    s.config()
    s.pack(pady=10)

    button = Button(root, text="Next", command= lambda: calculos(s.get()))
    button.pack(pady=10)

    t = Label(root, text="NI SE TE OCURRA PONER CERO YO AVISO. BAJO TU PROPIA RESPONSABILIDAD")
    t.pack(pady= 60)

def calculos(numero):
    numero = int(numero)
    root.destroy()

    if numero == 0:
        hack()
        return 0

    new = Tk()
    new.geometry("600x800")
    

    zones = []

    for i in range(numero):
        string = "Zona " + str(i)
        text = Label(new, text=string)
        text.pack(pady=2)

        largo = Label(new, text="Largo (cm)")
        largo.pack()
        l = Text(new, width=30, height=1)
        l.pack()

        ancho = Label(new, text="Ancho (cm)")
        ancho.pack()
        a = Text(new, width=30, height=1)
        a.pack()

        zones.append((l, a))

    button = Button(new, text="Get Results", command=lambda: showFinal(zones, new))
    button.pack(pady=15)
    
    

def showFinal(zones, window):
    #En cms^2
    velocidad = 3

    if not check(zones):
        window.destroy()
        gili = Tk()
        gili.attributes("-fullscreen", True)
        t = Label(gili, text="Eres completamente subnormal. No sabes meter ni un numero en serio. Tu estupidex te ha llevado a esta siuacion de estar atrapado y no pode hacer nada \n que se seinte pedazo de retradaso. Pues aqui estas, no se, espera digo yo a que pase algo o no")
        t.config(font=25)
        t.pack(pady= 40)
        
        return 0

    superficie = 0

    for zone in zones:
        superficie = superficie + int(zone[0].get("1.0", END)) + int(zone[1].get("1.0", END))


    time = superficie / velocidad

    final = Tk()
    final.geometry("600x300")
    t = Label(final, text="Texto generico gracioso de que el cacharro dice algo sobre lo que tarda y blablabla...")
    t.config(font=20)
    t.pack(pady=30)
    z = Label(final, text=("Tiempo: " + str(time) + " segundos"))
    z.pack()

    end = Button(final, text="Dale aqui y nos vamos todos a casa", command= lambda: close(final, window))
    end.pack(pady=30)

def check(zones):
    for zone in zones:
        try:
            int(zone[0].get("1.0", END))
            int(zone[1].get("1.0", END))
        except:
            return False
    
    return True

def hack():
    for i in range(1000000):
        new = Tk()
        new.geometry("400x400")

def close(final, anterior):
    final.destroy()
    anterior.destroy()


mainMenu()
root.mainloop()