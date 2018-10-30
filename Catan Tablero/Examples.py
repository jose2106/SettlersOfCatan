from tkinter import *

root = Tk()


Bosque = PhotoImage(file="Bosque.png")
BosqueSub = Bosque.subsample(3,3)
BosqueBut = Bosque.subsample(6,6)
Colinas = PhotoImage(file="Colinas.png")
ColinasSub = Colinas.subsample(5,5)
Montañas = PhotoImage(file="Montañas.png")
MontañasSub = Montañas.subsample(5,5)
Prados = PhotoImage(file="Prados.png")

PradosSub = Prados.subsample(5,5)
Cultivos = PhotoImage(file="Cultivos.png")
CultivosSub = Cultivos.subsample(5,5)
Desierto = PhotoImage(file="Desierto.png")
DesiertoSub = Desierto.subsample(5,5)

root.create_image(400,350,image=BosqueSub)


def callback(event):


    print ("clicked at", event.x, event.y)
frame = Frame(root, width=1280, height=720)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
