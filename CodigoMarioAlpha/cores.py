from declaracoes import *

#Cores em RGB:

#Branco: Esquerdo (31-37, 40-45, 40-43)  Direito (18-21, 28-31, 38-42)
#Verde (Saindo do Branco): Esquerdo (0-2, 5-7, 0-1) Direita (0-1, 4-6, 0-1)
#Preto Esquerdo (3,3,2-3) Direita ()
#Azul Esquerdo (2-3, 3-5, 7-9) Direita (0-1, 2-3, 7-8)
#Verde (Saindo do Azul)  Esquerda (2-4, 9-20, 0-4) Direita (0-4, 6-20,0-4)
#ValorCorEsquerda = 0
#ValorCorDireita = 0

def le_sensor_cor():
    global ValorCorEsquerda
    global ValorCorDireita
    ValorCorEsquerda = SensorCorEsquerda.rgb()
    ValorCorDireita = SensorCorDireita.rgb()
    #print("Valor na Esquerda é:", ValorCorEsquerda, "E na direita é", ValorCorDireita)
    return


def viu_branco():    # Se está vendo branco com os dois sensores retorna True, else False
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr
    eq_min =[20,20,20] # eq_min = [31,40,40]
    eq_max = [100,100,100]# eq_max = [37,45,43]
    dr_min = [15,20,30]# dr_min = [18,28,38]
    dr_max = [100,100,100] # dr_max = [21,31,42]
    eq = False
    dr = False
    
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True
    
    return eq or dr

def viu_verde_branco():          #Retorna True se Viu verde saindo do branco, em qualquer um dos sensores
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr
    eq_min = [0,5,0]
    eq_max = [2,9,2]
    dr_min = [0,4,0]
    dr_max = [1,6,1]
    eq = False
    dr = False
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True
    return eq or dr

def viu_preto():          #Viu verde saindo do branco
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr
    eq_min = [3,3,1]
    eq_max = [4,4,2]
    dr_min = [3,2,1]
    dr_max = [4,7,2]
    eq = False
    dr = False
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True
    return eq or dr

def viu_beirada():          #Viu beirada em algum dos dois sensores
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr
    eq_min = [0,0,0]
    eq_max = [0,0,0]
    dr_min = [0,0,0]
    dr_max = [0,0,0]
    eq = False
    dr = False
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True
    return eq or dr

def viu_azul():          #Viu azul
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr
    eq_min = [1,3,4]
    eq_max = [3,5,9]
    dr_min = [0,2,4]
    dr_max = [1,3,10]
    eq = False
    dr = False
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True
    return eq and dr

def viu_verde_azul():          #Viu verde saindo do azul
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr
    eq_min = [2,9,0]
    eq_max = [4,20,6]
    dr_min = [0,6,0]
    dr_max = [4,20,4]
    eq = False
    dr = False
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True
    return eq or dr

def viu_amarelo():          #Viu amarelo
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr
    eq_min = [35,25,3]
    eq_max = [40,30,6]
    dr_min = [20,16,2]
    dr_max = [23,21,5]
    eq = False
    dr = False
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True
    return eq or dr

def viu_vermelho():          #Viu vermelho
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr
    eq_min = [27,3,0]
    eq_max = [30,5,2]
    dr_min = [14,1,0]
    dr_max = [18,4,2]
    eq = False
    dr = False
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True
    return eq or dr
    
def alinha_verde_branco():
    global eq
    global dr
    if eq and dr:
        print("Os dois")
        return
    elif eq:
        print("Só na esquerda")
        while not (viu_verde_branco() and eq and dr):
            le_sensor_cor()
            robot.drive(26.75, -15)
        robot.stop()
    elif dr:
        print("Só na direita")
        while not (viu_verde_branco() and eq and dr):
            le_sensor_cor()
            robot.drive(26.75, 15)
        robot.stop()
    else:
        print("Wtf, isso tá muito errado")

def alinha_preto():
    global eq
    global dr
    if eq and dr:
        print("Os dois")
        return
    elif eq:
        print("Só na esquerda")
        while not (viu_preto() and eq and dr):
            le_sensor_cor()
            robot.drive(26.75, -15)
    elif dr:
        print("Só na direita")
        while not (viu_preto() and eq and dr):
            le_sensor_cor()
            robot.drive(26.75, 15)
    else:
        print("Wtf, isso tá muito errado")

def alinha_azul():
    global eq
    global dr
    if eq and dr:
        print("Os dois")
        return
    elif eq:
        print("Só na esquerda")
        while not (viu_azul() and eq and dr):
            le_sensor_cor()
            robot.drive(26.75, -15)
    elif dr:
        print("Só na direita")
        while not (viu_azul() and eq and dr):
            le_sensor_cor()
            robot.drive(26.75, 15)
    else:
        print("Wtf, isso tá muito errado")


def alinha_branco():
    global eq
    global dr
    if eq and dr:
        print("Os dois")
        return
    elif eq:
        print("Só na esquerda")
        while not (viu_branco() and eq and dr):
            le_sensor_cor()
            robot.drive(36.75, -15)
    elif dr:
        print("Só na direita")
        while not (viu_branco() and eq and dr):
            le_sensor_cor()
            robot.drive(36.75, 15)
    else:
        print("Wtf, isso tá muito errado")




def alinha_verde_azul():
    global eq
    global dr
    if eq and dr:
        print("Os dois")
        return
    elif eq:
        print("Só na esquerda")
        while not (viu_verde_azul() and eq and dr):
            le_sensor_cor()
            robot.drive(26.75, -15)
        robot.stop()
    elif dr:
        print("Só na direita")
        while not (viu_verde_azul() and eq and dr):
            le_sensor_cor()
            robot.drive(26.75, 15)
        robot.stop()
    else:
        print("Wtf, isso tá muito errado")


def alinha_beirada():
    global eq
    global dr
    if eq and dr:
        print("Os dois")
        return
    elif eq:
        print("Só na esquerda")
        while not (viu_beirada() and eq and dr):
            le_sensor_cor()
            robot.drive(26.75, -15)
    elif dr:
        print("Só na direita")
        while not (viu_beirada() and eq and dr):
            le_sensor_cor()
            robot.drive(26.75, 15)
    else:
        print("Wtf, isso tá muito errado")


def teste2():
    global ValorCorEsquerda
    global ValorCorDireita
    le_sensor_cor()
    while True:
        le_sensor_cor()
        robot.drive(15,0)
    alinha_verde_azul()
    while True:
        robot.drive(120,0)


def teste():
    global ValorCorEsquerda
    global ValorCorDireita
    while True:   
        le_sensor_cor()
        print("Valor na Esquerda é:", ValorCorEsquerda, "E na direita é", ValorCorDireita)
        if ValorCorEsquerda == (0,0,0) or ValorCorDireita == (0,0,0):
            robot.stop()
        elif viu_branco(): 
            robot.drive(70,0)
        else:
            while not (viu_preto() or viu_verde_branco() or viu_beirada()):
                le_sensor_cor()
                print("Valor na Esquerda é:", ValorCorEsquerda, "E na direita é", ValorCorDireita)
                robot.drive(70,0)
            if viu_preto():
                robot.stop()
                ev3.speaker.beep(200)
            elif viu_verde_branco():
                robot.stop()
                ev3.speaker.beep(800)
            elif viu_beirada():
                robot.stop()