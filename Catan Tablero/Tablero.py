from tkinter import *
import tkinter as tk
import random
from Clase_Grafo import *
from functools import partial        

#Super Hello world

#Inicializacion de la ventana
window = Tk()

window.title("Settlers of Catan")
Ftablero = Canvas(window, width=800,height=720,bg="BLUE")
window.geometry("800x720+640+0")
Ftablero.place(x=0,y=0)

#Desclarar imagenes y resampleos
Bosque = PhotoImage(file="Bosque.png")
BosqueSub = Bosque.subsample(6,6)
Colinas = PhotoImage(file="Colinas.png")
ColinasSub = Colinas.subsample(6,6)
Montañas = PhotoImage(file="Montañas.png")
MontañasSub = Montañas.subsample(6,6)
Prados = PhotoImage(file="Prados.png")
PradosSub = Prados.subsample(6,6)
Cultivos = PhotoImage(file="Cultivos.png")
CultivosSub = Cultivos.subsample(6,6)
Desierto = PhotoImage(file="Desierto.png")
DesiertoSub = Desierto.subsample(6,6)

#Eventos de click

#Coordenadas X
C_X = [368, 431, 272, 336, 464, 528, 179, 243, 367, 432, 560, 621, 148, 272, 337, 463, 528, 653, 176, 241, 366, 433, 558, 623, 147, 273, 337, 461, 526, 656, 178, 240, 368, 432, 559, 624, 146, 274, 336, 463, 527, 654, 177, 241, 369, 431, 559, 622, 273, 336, 464, 527, 369, 432]
#Coordenadas Y
C_Y = [83, 81, 138, 136, 136, 136, 194, 192, 191, 191, 190, 192, 249, 247, 247, 247, 245, 244, 302, 302, 301, 303, 302, 300, 357, 354, 356, 357, 357, 357, 412, 411, 411, 413, 410, 412, 467, 467, 465, 467, 467, 467, 522, 522, 520, 521, 523, 522, 577, 576, 576, 578, 631, 631]

#Dic de bot.
botones = {}

#Eventos de click

def key(event):
    print ("pressed"), repr(event.char)

def callback(event):
    Ftablero.focus_set()
    print ("Click en: ", event.x, event.y)


Ftablero.bind("<Key>", key)
Ftablero.bind("<Button-1>", callback)


def ReorganizarTablero():
    Terrenos = {1: BosqueSub,
                11: BosqueSub,
                21: BosqueSub,
                31: BosqueSub,
                2: PradosSub,
                12: PradosSub,
                22: PradosSub,
                32: PradosSub,
                3: CultivosSub,
                13: CultivosSub,
                23: CultivosSub,
                33: CultivosSub,
                4: MontañasSub,
                14: MontañasSub,
                24: MontañasSub,
                34: MontañasSub,
                5: ColinasSub,
                15: ColinasSub,
                25: ColinasSub,
                35: ColinasSub,
                6: DesiertoSub}

    #Algoritmo de no repeticion

    contador1 = 0
    contador1S = 0
    contador2 = 0
    contador2S = 0
    contador3 = 0
    contador3S = 0
    contador4 = 0
    contador4S = 0
    contador5 = 0
    contador5S = 0
    contador6 = 0
    contadorG = 0
     
    rarray = []
    
    for n in range(19):
    
        while contadorG !=19:
            r = random.randint(1,6)
            
            if r==1 and contador1 !=4:
                contador1+=1
                rarray.append(r+contador1S)
                contador1S+=10
            
            elif r==2 and contador2 !=4:
                contador2+=1
                rarray.append(r+contador2S)
                contador2S+=10
                
            elif r==3 and contador3 !=4:
                contador3+=1
                rarray.append(r+contador3S)
                contador3S+=10
            
            elif r==4 and contador4 !=3:
                contador4+=1
                rarray.append(r+contador4S)
                contador4S+=10
            
            elif r==5 and contador5 !=3:
                contador5+=1
                rarray.append(r+contador5S)
                contador5S+=10

            elif r==6 and contador6 !=1:
                contador6+=1
                rarray.append(r)

        
            contadorG = contador1 + contador2 + contador3 + contador4 + contador5 + contador6

    #Donde hay seis recorrer el numero para dejar sin ficha el desierto
    i=0
    for index in rarray:
         if index != 6:
            i+=1
            print(i)
         else:
            print("Aqui hay un 6")
        
    print(rarray)
    
    


    Ftablero.create_image(400,140,image=Terrenos[rarray[0]])

    Ftablero.create_image(305,195,image=Terrenos[rarray[1]])
    Ftablero.create_image(495,195,image=Terrenos[rarray[2]])

    Ftablero.create_image(210,250,image=Terrenos[rarray[3]])
    Ftablero.create_image(400,250,image=Terrenos[rarray[4]])
    Ftablero.create_image(590,250,image=Terrenos[rarray[5]])
    
    Ftablero.create_image(305,305,image=Terrenos[rarray[6]])
    Ftablero.create_image(495,305,image=Terrenos[rarray[7]])
   
    Ftablero.create_image(210,360,image=Terrenos[rarray[8]])
    Ftablero.create_image(400,360,image=Terrenos[rarray[9]])
    Ftablero.create_image(590,360,image=Terrenos[rarray[10]])
    
    Ftablero.create_image(305,415,image=Terrenos[rarray[11]])
    Ftablero.create_image(495,415,image=Terrenos[rarray[12]])

    Ftablero.create_image(210,470,image=Terrenos[rarray[13]])
    Ftablero.create_image(400,470,image=Terrenos[rarray[14]])
    Ftablero.create_image(590,470,image=Terrenos[rarray[15]])
    
    Ftablero.create_image(305,525,image=Terrenos[rarray[16]])
    Ftablero.create_image(495,525,image=Terrenos[rarray[17]])
   
    Ftablero.create_image(400,580,image=Terrenos[rarray[18]])

    #Grafo de los terrenos

    GT = Grafo() 


    #Conexion vertices y terrenos

    GT.conecta(rarray[0],"1")
    GT.conecta(rarray[0],"2")


    GT.conecta(rarray[1],"3")

    GT.conecta(rarray[0],"4")
    GT.conecta(rarray[1],"4")

    GT.conecta(rarray[0],"5")
    GT.conecta(rarray[2],"5")

    GT.conecta(rarray[2],"6")

    GT.conecta(rarray[3],"7")

    GT.conecta(rarray[1],"8")
    GT.conecta(rarray[3],"8")

    GT.conecta(rarray[0],"9")
    GT.conecta(rarray[1],"9")
    GT.conecta(rarray[4],"9")

    GT.conecta(rarray[0],"10")
    GT.conecta(rarray[2],"10")
    GT.conecta(rarray[4],"10")

    GT.conecta(rarray[2],"11")
    GT.conecta(rarray[5],"11")

    GT.conecta(rarray[5],"12")

    GT.conecta(rarray[3],"13")

    GT.conecta(rarray[1],"14")
    GT.conecta(rarray[3],"14")
    GT.conecta(rarray[6],"14")

    GT.conecta(rarray[1],"15")
    GT.conecta(rarray[4],"15")
    GT.conecta(rarray[6],"15")

    GT.conecta(rarray[2],"16")
    GT.conecta(rarray[4],"16")
    GT.conecta(rarray[7],"16")

    GT.conecta(rarray[2],"17")
    GT.conecta(rarray[5],"17")
    GT.conecta(rarray[7],"17")

    GT.conecta(rarray[5],"18")

    GT.conecta(rarray[3],"19")
    GT.conecta(rarray[8],"19")

    GT.conecta(rarray[3],"20")
    GT.conecta(rarray[6],"20")
    GT.conecta(rarray[8],"20")

    GT.conecta(rarray[4],"21")
    GT.conecta(rarray[6],"21")
    GT.conecta(rarray[9],"21")

    GT.conecta(rarray[4],"22")
    GT.conecta(rarray[7],"22")
    GT.conecta(rarray[9],"22")

    GT.conecta(rarray[5],"23")
    GT.conecta(rarray[7],"23")
    GT.conecta(rarray[10],"23")

    GT.conecta(rarray[5],"24")
    GT.conecta(rarray[10],"24")

    GT.conecta(rarray[8],"25")

    GT.conecta(rarray[6],"26")
    GT.conecta(rarray[8],"26")
    GT.conecta(rarray[11],"26")

    GT.conecta(rarray[6],"27")
    GT.conecta(rarray[9],"27")
    GT.conecta(rarray[11],"27")

    GT.conecta(rarray[7],"28")
    GT.conecta(rarray[9],"28")
    GT.conecta(rarray[12],"28")

    GT.conecta(rarray[7],"29")
    GT.conecta(rarray[10],"29")
    GT.conecta(rarray[12],"29")

    GT.conecta(rarray[10],"30")

    GT.conecta(rarray[8],"31")
    GT.conecta(rarray[13],"31")

    GT.conecta(rarray[8],"32")
    GT.conecta(rarray[11],"32")
    GT.conecta(rarray[13],"32")

    GT.conecta(rarray[9],"33")
    GT.conecta(rarray[11],"33")
    GT.conecta(rarray[14],"33")

    GT.conecta(rarray[9],"34")
    GT.conecta(rarray[12],"34")
    GT.conecta(rarray[14],"34")

    GT.conecta(rarray[10],"35")
    GT.conecta(rarray[12],"35")
    GT.conecta(rarray[15],"35")

    GT.conecta(rarray[10],"36")
    GT.conecta(rarray[15],"36")

    GT.conecta(rarray[13],"37")

    GT.conecta(rarray[11],"38")
    GT.conecta(rarray[13],"38")
    GT.conecta(rarray[16],"38")

    GT.conecta(rarray[11],"39")
    GT.conecta(rarray[14],"39")
    GT.conecta(rarray[16],"39")

    GT.conecta(rarray[12],"40")
    GT.conecta(rarray[14],"40")
    GT.conecta(rarray[17],"40")

    GT.conecta(rarray[12],"41")
    GT.conecta(rarray[15],"41")
    GT.conecta(rarray[17],"41")

    GT.conecta(rarray[15],"42")

    GT.conecta(rarray[13],"43")

    GT.conecta(rarray[13],"44")
    GT.conecta(rarray[16],"44")

    GT.conecta(rarray[14],"45")
    GT.conecta(rarray[16],"45")
    GT.conecta(rarray[18],"45")

    GT.conecta(rarray[14],"46")
    GT.conecta(rarray[17],"46")
    GT.conecta(rarray[18],"46")

    GT.conecta(rarray[15],"47")
    GT.conecta(rarray[17],"47")

    GT.conecta(rarray[15],"48")

    GT.conecta(rarray[16],"49")

    GT.conecta(rarray[16],"50")
    GT.conecta(rarray[18],"50")

    GT.conecta(rarray[17],"51")
    GT.conecta(rarray[18],"51")

    GT.conecta(rarray[17],"52")

    GT.conecta(rarray[18],"53")

    GT.conecta(rarray[18],"54")

    #Conexiones entre vertices

    

    #Vecinos del boton
    
    def valorB(i,e):
        
        l_terrenos = []
        for x in GT.vecinos[e]:
            if x == 6:
                l_terrenos.append("Desierto")
                botones["Boton{0}".format(e)] = Button(width = 1, height = 1,background = "red",relief = "flat",cursor = "crosshair", command = partial(valorB, "Boton{0}".format(e), str(e)))
                botones["Boton{0}".format(e)].pack()
                botones["Boton{0}".format(e)].place(x=C_X[int(e)-1]-5, y=C_Y[int(e)-1]-10)
            elif x==1 or x==11 or x==21 or x==31:
                l_terrenos.append("Bosques")
            elif x==2 or x==12 or x==22 or x==32:
                l_terrenos.append("Prados")
            elif x==3 or x==13 or x==23 or x==33:
                l_terrenos.append("Cultivos")
            elif x==4 or x==14 or x==24 or x==34:
                l_terrenos.append("Montañas")
            elif x==5 or x==15 or x==25 or x==35:
                l_terrenos.append("Colinas")
                
        print(l_terrenos)
    
    
    #Generar botones automaticamente
    
    def generate_buttons():
        for i in range(len(C_X)):
            botones["Boton{0}".format(i)] = Button(width = 1, height = 1,background = "yellow",relief = "flat",cursor = "crosshair", command = partial(valorB, "Boton{0}".format(i+1), str(i+1))) #Partial declara funcion con argumento sin llamarla
            #Poner imagenes gif mas pequeñas en botones 
        for z in range(len(C_X)):
            botones["Boton{0}".format(z)].pack()
            #Pos. de botones
            botones["Boton{0}".format(z)].place(x=C_X[z]-5, y=C_Y[z]-10)
            
    
    generate_buttons() 
    


    
BotonTablero = Button(text="Reorganizar Tablero", command=ReorganizarTablero)
BotonTablero.pack()











        



    
    


































    
