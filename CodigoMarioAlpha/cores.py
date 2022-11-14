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
    # print("Valor na Esquerda é:", ValorCorEsquerda, "E na direita é", ValorCorDireita)
    return

def valor_dr(i = 0):
    global ValorCorDireita
    if i == 0:
        return ValorCorDireita[0]
    elif i == 1:
        return ValorCorDireita[1]
    else:
        return ValorCorDireita[2]

def valor_eq(i = 0):
    global ValorCorEsquerda
    if i == 0:
        return ValorCorEsquerda[0]
    elif i == 1:
        return ValorCorEsquerda[1]
    else:
        return ValorCorEsquerda[2]

def segue_verde_branco_dr():
    threshold = 30
    PROPORTIONAL_GAIN = 1
    DRIVE_SPEED = 111

    leitura_sensor = valor_dr(2)
    #print(leitura_sensor)
    
    deviation =  leitura_sensor - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(DRIVE_SPEED, turn_rate)

def segue_verde_branco_eq():
    global ValorCorDireita
    threshold = 32
    PROPORTIONAL_GAIN = 1
    DRIVE_SPEED = 111

    leitura_sensor = valor_eq(2)
    #print(leitura_sensor)
    
    deviation =  -leitura_sensor + threshold
    if deviation > 0:
        PROPORTIONAL_GAIN = 1
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(DRIVE_SPEED, turn_rate)

def segue_verde_azul_eq():
    global ValorCorDireita
    threshold = 27
    PROPORTIONAL_GAIN = 1.3
    DRIVE_SPEED = 115

    leitura_sensor = valor_eq(1)
    # print(leitura_sensor)
    
    deviation =  leitura_sensor - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(DRIVE_SPEED, turn_rate)

def segue_azul_beirada_eq():
    threshold = 18
    PROPORTIONAL_GAIN = 1
    DRIVE_SPEED = 90

    leitura_sensor = valor_eq(2)
    # print(leitura_sensor)
    
    deviation =  -leitura_sensor + threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(DRIVE_SPEED, turn_rate)

def viu_branco():    # Se está vendo branco com os dois sensores retorna True, else False
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr
    eq_min =[30,40,40] # eq_min = [31,40,40]
    eq_max = [100,100,100]# eq_max = [37,45,43]
    dr_min = [15,25,30]# dr_min = [18,28,38]
    dr_max = [100,100,100] # dr_max = [21,31,42]
    eq = False
    dr = False
    
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True

    return eq or dr

def viu_branco_eq():
    global eq
    return viu_branco() and eq

def viu_branco_dr():
    global dr
    return viu_branco() and dr

def viu_verde_branco():          #Retorna True se Viu verde saindo do branco, em qualquer um dos sensores
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr
    eq_min = [0,15,6]
    eq_max = [7,25,15]
    dr_min = [0,6,2]
    dr_max = [3,15,8]
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
    eq_max = [7,6,3]
    dr_min = [2,2,1]
    dr_max = [5,6,4]
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
    eq_max = [1,1,1]
    dr_min = [0,0,0]
    dr_max = [1,1,1]
    eq = False
    dr = False
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True
    return eq or dr

def viu_beirada_eq():
    global eq
    return viu_beirada() and eq

def viu_beirada_dr():
    global dr
    return viu_beirada() and dr

def viu_azul():          #Viu azul
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr
    eq_min = [4,16,25]
    eq_max = [9,26,37]
    dr_min = [2,10,22]
    dr_max = [5,16,32]
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
    eq_min = [5,30,15]
    eq_max = [12,60,30]
    dr_min = [2,20,10]
    dr_max = [9,50,24]
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
    eq_min = [33,25,4]
    eq_max = [38,30,9]
    dr_min = [17,15,4]
    dr_max = [23,21,8]
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
    eq_max = [30,5,4]
    dr_min = [13,1,0]
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
            robot.drive(100, -42) #36.75 e -15
    elif dr:
        print("Só na direita")
        while not (viu_branco() and eq and dr):
            le_sensor_cor()
            robot.drive(100, 42)
    else:
        print("Wtf, isso tá muito errado")


def alinha_not_branco():
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
    watch_virada.reset()
    while watch_virada.time()<450:
        robot.drive(-200,0)
    le_sensor_cor()
    while not viu_beirada():
        le_sensor_cor()
        robot.drive(40,0)
    alinha_beirada2()

def alinha_beirada2():
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
    le_sensor_cor()
    while True:
        le_sensor_cor()
        if viu_beirada():
            robot.stop()
        else:
            robot.drive(110,0)


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