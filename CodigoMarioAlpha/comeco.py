from declaracoes import *
from cores import *

def inicio():
    while True:
        le_sensor_cor()
        if viu_verde_branco():
            ev3.speaker.beep(900)
            robot.stop()
            #alinha_verde_branco()
            break
        elif viu_preto():
            ev3.speaker.beep(200)
            robot.stop()
            robot.straight(-150)
            robot.turn(90)
            #alinha_preto()
        elif viu_beirada():
            robot.stop()
            robot.straight(-150)
            robot.turn(90)
            #alinha_beirada()
        else:
            robot.drive(100,0)