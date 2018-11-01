from tkinter import *
import tkinter as tk
from Generator import * 
from Clase_Grafo import *
from functools import partial        

#Inicializacion de la ventana
window = Tk()

window.title("Settlers of Catan")
Ftablero = Canvas(window, width=800,height=720,bg="#46eae4")
FGR = Canvas(window, width=480,height=720,bg="#f4c542")
window.geometry("1280x720+0+0")
Ftablero.place(x=0,y=0)
FGR.place(x=800,y=0)

#Desclarar imagenes y resampleos
Boton= PhotoImage(file="Vertice.gif")
Vertice = Boton.subsample(9,9)
fichados = PhotoImage(file="f_dos.png")
fichatres = PhotoImage(file="f_tres.png")
fichacuatro = PhotoImage(file="f_cuatro.png")
fichacinco = PhotoImage(file="f_cinco.png")
fichaseis = PhotoImage(file="f_seis.png")
fichaocho = PhotoImage(file="f_ocho.png")
fichanueve = PhotoImage(file="f_nueve.png")
fichadiez = PhotoImage(file="f_diez.png")
fichaonce = PhotoImage(file="f_once.png")
fichadoce = PhotoImage(file="f_doce.png")
f_dos = fichados.subsample(8,8)
f_tres = fichatres.subsample(8,8)
f_cuatro = fichacuatro.subsample(8,8)
f_cinco = fichacinco.subsample(8,8)
f_seis = fichaseis.subsample(8,8)
f_ocho = fichaocho.subsample(8,8)
f_nueve = fichanueve.subsample(8,8)
f_diez = fichadiez.subsample(8,8)
f_once = fichaonce.subsample(8,8)
f_doce = fichadoce.subsample(8,8)
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

#Centros de fichas
C_F_X = [400, 304, 494, 210, 398, 591, 303, 496, 207, 401, 591, 304, 497, 209, 399, 591, 305, 496, 400]
C_F_Y = [133, 190, 190, 247, 245, 246, 302, 298, 355, 359, 352, 410, 413, 466, 468, 464, 517, 519, 574]

ncx = {'Boton1': 368, 'Boton2': 431, 'Boton3': 272, 'Boton4': 336, 'Boton5': 464, 'Boton6': 528, 'Boton7': 179, 'Boton8': 243, 'Boton9': 367, 'Boton10': 432, 'Boton11': 560, 'Boton12': 621, 'Boton13': 148, 'Boton14': 272, 'Boton15': 337, 'Boton16': 463, 'Boton17': 528, 'Boton18': 653, 'Boton19': 176, 'Boton20': 241, 'Boton21': 366, 'Boton22': 433, 'Boton23': 558, 'Boton24': 623, 'Boton25': 147, 'Boton26': 273, 'Boton27': 337, 'Boton28': 461, 'Boton29': 526, 'Boton30': 656, 'Boton31': 178, 'Boton32': 240, 'Boton33': 368, 'Boton34': 432, 'Boton35': 559, 'Boton36': 624, 'Boton37': 146, 'Boton38': 274, 'Boton39': 336, 'Boton40': 463, 'Boton41': 527, 'Boton42': 654, 'Boton43': 177, 'Boton44': 241, 'Boton45': 369, 'Boton46': 431, 'Boton47': 559, 'Boton48': 622, 'Boton49': 273, 'Boton50': 336, 'Boton51': 464, 'Boton52': 527, 'Boton53': 369, 'Boton54': 432}
ncy = {'Boton1': 83, 'Boton2': 81, 'Boton3': 138, 'Boton4': 136, 'Boton5': 136, 'Boton6': 136, 'Boton7': 194, 'Boton8': 192, 'Boton9': 191, 'Boton10': 191, 'Boton11': 190, 'Boton12': 192, 'Boton13': 249, 'Boton14': 247, 'Boton15': 247, 'Boton16': 247, 'Boton17': 245, 'Boton18': 244, 'Boton19': 302, 'Boton20': 302, 'Boton21': 301, 'Boton22': 303, 'Boton23': 302, 'Boton24': 300, 'Boton25': 357, 'Boton26': 354, 'Boton27': 356, 'Boton28': 357, 'Boton29': 357, 'Boton30': 357, 'Boton31': 412, 'Boton32': 411, 'Boton33': 411, 'Boton34': 413, 'Boton35': 410, 'Boton36': 412, 'Boton37': 467, 'Boton38': 467, 'Boton39': 465, 'Boton40': 467, 'Boton41': 467, 'Boton42': 467, 'Boton43': 522, 'Boton44': 522, 'Boton45': 520, 'Boton46': 521, 'Boton47': 523, 'Boton48': 522, 'Boton49': 577, 'Boton50': 576, 'Boton51': 576, 'Boton52': 578, 'Boton53': 631, 'Boton54': 631}



#Dic de bot.
botones = {}

#Eventos de click

#def key(event):
 #   print ("pressed"), repr(event.char)

#def callback(event):
 #   Ftablero.focus_set()
 #   C_F_X.append(event.x)
  #  print(C_F_X)
   # C_F_Y.append(event.y)
    #print(C_F_Y)
    #print ("Click en: ", event.x, event.y)


#Ftablero.bind("<Key>", key)
#Ftablero.bind("<Button-1>", callback)


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
    i = 0
    j = 3
    
    for n in range(19):
    
        while contadorG !=19:
            i += 1
            j += 1
            r = Generator(a = i, c = j/2, low = 1, high = 6, rounded = True).throw()
            print(r)
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

    print("Arreglo global de los terrenos del tablero")            
    print(rarray)
    print("")
    


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

    #Donde hay seis recorrer el numero para dejar sin ficha el desierto
    N_F_O = []
    
    #Arreglo de fichas ordenadas
    F_O = [f_once, f_cuatro, f_doce, f_ocho, f_tres, f_nueve, f_once, f_seis, f_diez, f_diez, f_nueve, f_cinco, f_cinco, f_cuatro, f_ocho, f_dos, f_tres, f_seis]

    #Numero de ficha de cada pieza (hexagono)
    F_Temp = {}
    F_T = {}


###################----Encapsulado--###########################
    def evitar_desierto(*args):
        N_F_O.append(*args)
        for i in range(len(N_F_O)):
            Ftablero.create_image(C_F_X[i], C_F_Y[i], image= N_F_O[i])

            switcher = {
                "pyimage13": 2 ,
                "pyimage14": 3 ,
                "pyimage15": 4 ,
                "pyimage16": 5 ,
                "pyimage17": 6 ,
                "pyimage18": 8 ,
                "pyimage19" : 9 ,
                "pyimage20": 10 ,
                "pyimage21": 11 ,
                "pyimage22" : 12 
            }
            F_T[switcher.get("{0}".format(N_F_O[i]))] = rarray[i] 
            

   

   

    for w in range(len(rarray)):
 
        if rarray[w] == 6:
               evitar_desierto(None)
        try: 
            evitar_desierto(F_O[w])
        except IndexError:
            print("")
###################################################################

    print("Valor para dados - Terrenos (rarray)")
    print(F_T)
        

    
           
       
            

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

    GT.conecta("Boton1","Boton2")
    GT.conecta("Boton1","Boton4")

    GT.conecta("Boton2","Boton1")
    GT.conecta("Boton2","Boton5")

    GT.conecta("Boton3","Boton4")
    GT.conecta("Boton3","Boton8")

    GT.conecta("Boton4","Boton1")
    GT.conecta("Boton4","Boton3")
    GT.conecta("Boton4","Boton9")

    GT.conecta("Boton5","Boton6")
    GT.conecta("Boton5","Boton2")
    GT.conecta("Boton5","Boton10")

    GT.conecta("Boton6","Boton5")
    GT.conecta("Boton6","Boton11")

    GT.conecta("Boton7","Boton8")
    GT.conecta("Boton7","Boton13")

    GT.conecta("Boton8","Boton7")
    GT.conecta("Boton8","Boton14")

    GT.conecta("Boton9","Boton4")
    GT.conecta("Boton9","Boton10")
    GT.conecta("Boton9","Boton15")

    GT.conecta("Boton10","Boton9")
    GT.conecta("Boton10","Boton5")
    GT.conecta("Boton10","Boton16")

    GT.conecta("Boton11","Boton12")
    GT.conecta("Boton11","Boton6")
    GT.conecta("Boton11","Boton17")

    GT.conecta("Boton12","Boton11")
    GT.conecta("Boton12","Boton18")

    GT.conecta("Boton13","Boton7")
    GT.conecta("Boton13","Boton19")

    GT.conecta("Boton14","Boton15")
    GT.conecta("Boton14","Boton8")
    GT.conecta("Boton14","Boton20")

    GT.conecta("Boton15","Boton14")
    GT.conecta("Boton15","Boton9")
    GT.conecta("Boton15","Boton21")

    GT.conecta("Boton16","Boton22")
    GT.conecta("Boton16","Boton10")
    GT.conecta("Boton16","Boton17")

    GT.conecta("Boton17","Boton16")
    GT.conecta("Boton17","Boton11")
    GT.conecta("Boton17","Boton23")

    GT.conecta("Boton18","Boton24")
    GT.conecta("Boton18","Boton12")

    GT.conecta("Boton19","Boton25")
    GT.conecta("Boton19","Boton13")
    GT.conecta("Boton19","Boton20")

    GT.conecta("Boton20","Boton26")
    GT.conecta("Boton20","Boton14")
    GT.conecta("Boton20","Boton19")

    GT.conecta("Boton21","Boton27")
    GT.conecta("Boton21","Boton15")
    GT.conecta("Boton21","Boton22")

    GT.conecta("Boton22","Boton21")
    GT.conecta("Boton22","Boton28")
    GT.conecta("Boton22","Boton16")
    
    GT.conecta("Boton23","Boton17")
    GT.conecta("Boton23","Boton29")

    GT.conecta("Boton24","Boton23")
    GT.conecta("Boton24","Boton30")
    GT.conecta("Boton24","Boton18")

    GT.conecta("Boton25","Boton31")
    GT.conecta("Boton25","Boton19")

    GT.conecta("Boton26","Boton27")
    GT.conecta("Boton26","Boton32")
    GT.conecta("Boton26","Boton20")

    GT.conecta("Boton27","Boton21")
    GT.conecta("Boton27","Boton33")
    GT.conecta("Boton27","Boton26")

    GT.conecta("Boton28","Boton29")
    GT.conecta("Boton28","Boton34")
    GT.conecta("Boton28","Boton22")

    GT.conecta("Boton29","Boton28")
    GT.conecta("Boton29","Boton23")
    GT.conecta("Boton29","Boton35")

    GT.conecta("Boton30","Boton36")
    GT.conecta("Boton30","Boton24")

    GT.conecta("Boton31","Boton32")
    GT.conecta("Boton31","Boton25")
    GT.conecta("Boton31","Boton37")

    GT.conecta("Boton32","Boton31")
    GT.conecta("Boton32","Boton38")
    GT.conecta("Boton32","Boton26")

    GT.conecta("Boton33","Boton34")
    GT.conecta("Boton33","Boton39")
    GT.conecta("Boton33","Boton27")

    GT.conecta("Boton34","Boton33")
    GT.conecta("Boton34","Boton40")
    GT.conecta("Boton34","Boton28")

    GT.conecta("Boton35","Boton36")
    GT.conecta("Boton35","Boton41")
    GT.conecta("Boton35","Boton29")

    GT.conecta("Boton36","Boton35")
    GT.conecta("Boton36","Boton42")
    GT.conecta("Boton36","Boton30")

    GT.conecta("Boton37","Boton43")
    GT.conecta("Boton37","Boton31")

    GT.conecta("Boton38","Boton39")
    GT.conecta("Boton38","Boton44")
    GT.conecta("Boton38","Boton32")

    GT.conecta("Boton39","Boton38")
    GT.conecta("Boton39","Boton45")
    GT.conecta("Boton39","Boton33")

    GT.conecta("Boton40","Boton41")
    GT.conecta("Boton40","Boton46")
    GT.conecta("Boton40","Boton34")

    GT.conecta("Boton41","Boton40")
    GT.conecta("Boton41","Boton47")
    GT.conecta("Boton41","Boton35")

    GT.conecta("Boton42","Boton48")
    GT.conecta("Boton42","Boton36")

    GT.conecta("Boton43","Boton37")
    GT.conecta("Boton43","Boton44")

    GT.conecta("Boton44","Boton43")
    GT.conecta("Boton44","Boton49")
    GT.conecta("Boton44","Boton38")

    GT.conecta("Boton45","Boton39")
    GT.conecta("Boton45","Boton46")
    GT.conecta("Boton45","Boton50")

    GT.conecta("Boton46","Boton45")
    GT.conecta("Boton46","Boton40")
    GT.conecta("Boton46","Boton51")

    GT.conecta("Boton47","Boton48")
    GT.conecta("Boton47","Boton41")
    GT.conecta("Boton47","Boton52")

    GT.conecta("Boton48","Boton42")
    GT.conecta("Boton48","Boton47")

    GT.conecta("Boton49","Boton50")
    GT.conecta("Boton49","Boton44")

    GT.conecta("Boton50","Boton45")
    GT.conecta("Boton50","Boton49")
    GT.conecta("Boton50","Boton53")

    GT.conecta("Boton51","Boton46")
    GT.conecta("Boton51","Boton52")
    GT.conecta("Boton51","Boton54")

    GT.conecta("Boton52","Boton51")
    GT.conecta("Boton52","Boton47")

    GT.conecta("Boton53","Boton50")
    GT.conecta("Boton53","Boton54")

    GT.conecta("Boton54","Boton53")
    GT.conecta("Boton54","Boton51")
        

    

    #Vecinos del boton
    
    def valorB(i,e):
        print(i)
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
            botones["Boton{0}".format(i)] = Button(width = 9, height = 9,background = "black", image=Vertice, relief = "flat",cursor = "crosshair", command = partial(valorB, "Boton{0}".format(i+1), str(i+1))) #Partial declara funcion con argumento sin llamarla


        #Poner imagenes gif mas pequeñas en botones 
        for z in range(len(C_X)):
            botones["Boton{0}".format(z)].pack()
            #Pos. de botones
            botones["Boton{0}".format(z)].place(x=C_X[z]-6, y=C_Y[z]-5)

    
    def conexionesB(*args):
        return str(args[0])

    def BotonP(bp):
        return str(bp)
            
    

    for i in range(len(C_X)):
        try:
            for x in GT.vecinos["Boton{0}".format(i+1)]:
                print("")
                bp = "Boton{}".format(i+1)
                Ftablero.create_line(ncx[BotonP(bp)],ncy[BotonP(bp)],ncx[conexionesB(x)],ncy[conexionesB(x)], fill="white",width=3)
                
            pass
            
        except KeyError:
            pass



    
    
               





    
            
    
    generate_buttons()

BotonTablero = Button(text="Nuevo Juego", command=ReorganizarTablero, relief = "flat")
BotonTablero.pack()
BotonTablero.place(x=361, y=20)
window.mainloop()

    


    












        



    
    


































    
