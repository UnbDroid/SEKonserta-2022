from declaracoes import *
from cores import *
from percorregasoduto import *

def inicio():
    watch2.reset()
    while True:
        le_sensor_cor()
        if viu_verde_branco():
            ev3.speaker.beep(900)
            robot.stop()
            alinha_verde_branco()
            desce_rampa_comeco()
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

def desce_rampa_comeco():
    while not (viu_azul()):
        le_sensor_cor()
        if viu_beirada():
            robot.stop()
        else:
            robot.drive(50,0)
    robot.straight(100)
    robot.turn(-90)
    return

def chega_no_gasoduto():
    while not (viu_beirada()):   #Após descer a rampa e virar para a esquerda, andar reto até encontrar a beirada
        le_sensor_cor()
        if viu_verde_azul():
            robot.drive(20, 40)
        else:
            robot.drive(100,0)
    alinha_beirada()
    robot.straight(-100)
    robot.turn(90)
    DistanciaUltrassomFrente = UltrassomFrente.distance()
    while DistanciaUltrassomFrente > 160:
        DistanciaUltrassomFrente = UltrassomFrente.distance()
        le_sensor_cor()
        if viu_beirada():
            robot.drive(20,40)
        else:
            robot.drive(70,0)
    robot.stop()
    watch.reset()
    while watch.time()<2650:
        robot.drive(8, 29)
    robot.stop()
    percorre_gasoduto_esquerda()
    return