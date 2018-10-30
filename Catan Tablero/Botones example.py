from tkinter import *

def Color(event):
    if event !=0:
        if event == lbl1:
            print("AZUL")
        else:
            print("Negro")
        
    

Ventana = Tk()
Ventana.geometry("300x300+20+20")

Boton = PhotoImage(file = "Boton_Rojo.png")
Boton1 = Boton.subsample(6,6)
Button = PhotoImage(file = "Black.png")
Boton2 = Button.subsample(2,2)
lbl1 = Label(Ventana, image = Boton1)
Lugar1 = lbl1.place(x=20,y=20)

lbl2 = Label(Ventana, image = Boton2)
Lugar2 = lbl2.place(x=200,y=200)

lbl1.bind("<Button-1>",Color)
lbl2.bind("<Button-1>",Color)

