from declaracoes import *
from cores import *
from percorregasoduto import *
from movimentacao import *

def inicio():   #INÍCIO DO PROGRAMA -> Acaba quando o Mario chega no gasoduto pela primeira vez
    watch2.reset()
    while True:
        le_sensor_cor()
        if viu_verde_branco():
            ev3.speaker.beep(900)
            robot.stop()
            alinha_verde_branco()
            desce_rampa_comeco_costas()
            chega_no_gasoduto()
            break
        elif viu_preto() or viu_azul() or viu_amarelo() or viu_vermelho():
            watch2.reset()
            ev3.speaker.beep(200)
            robot.stop()
            #alinha_preto()
            robot.straight(-150)
            robot.turn(180)
            watch2.reset()
        elif viu_beirada():
            robot.stop()
            alinha_beirada()
            robot.straight(-150)
            robot.turn(90)
            watch2.reset()
        elif watch2.time() > 5000:  #Se demorar mais que X segundos, virar, pois está indo em direção a uma beirada
            robot.stop()
            robot.turn(90)
            watch2.reset()
        else:
            robot.drive(100,0)

def desce_rampa_comeco(): #DESCER RAMPA NO COMEÇO DO CODIGO DE FRENTE
    while not (viu_azul()):
        le_sensor_cor()
        if viu_beirada():
            robot.stop()
        else:
            robot.drive(50,0)
    alinha_azul()
    robot.straight(100)
    robot.turn(-90)
    return

def desce_rampa_comeco_costas(): #Descer rampa no começo do programa de costas, considerando ele alinhado com a rampa de frente
    global eq
    global dr
    robot.straight(-100)
    robot.turn(180)
    while not (viu_azul()):
        le_sensor_cor()
        robot.drive(-120,0)
    while not (viu_verde_azul()):
        le_sensor_cor()
        robot.drive(80,0)
    alinha_verde_azul()
    robot.straight(-100)
    robot.turn(90)
    return


def chega_no_gasoduto(): # Função para chegar no gasoduto após descer a rampa e virar

    while not (viu_beirada()):   #Após descer a rampa e virar para a esquerda, andar reto até encontrar a beirada
        le_sensor_cor()
        # if viu_verde_azul():
        #     robot.drive(20, 40)
        # else:
        #     robot.drive(100,0)
        segue_verde_azul_eq()
    robot.stop()
    alinha_beirada()
    robot.straight(-100)
    robot.turn(90)
    DistanciaUltrassomFrente = UltrassomFrente.distance()
    while DistanciaUltrassomFrente > 160:
        DistanciaUltrassomFrente = UltrassomFrente.distance()
        le_sensor_cor()
        segue_azul_beirada_eq()
    robot.stop()
    watch.reset()
    while watch.time()<1400:
        robot.drive(23.5, 60)
    robot.stop()
    return