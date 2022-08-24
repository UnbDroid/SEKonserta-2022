#!/usr/bin/env pybricks-micropython 
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

motorEmpilhadeira = Motor(Port.A)
motorUltrassom = Motor(Port.B)
motorDireito = Motor(Port.D)
motorEsquerdo = Motor(Port.C)

ultrassom = UltrasonicSensor(Port.S1)
giroscopio = GyroSensor(Port.S2)
luzEsquerda = ColorSensor(Port.S3)
luzDireita = ColorSensor(Port.S4)

rodaDireita = Motor(Port.D)
rodaEsquerda = Motor(Port.C)
rodas = DriveBase(rodaEsquerda, rodaDireita, wheel_diameter= 40, axle_track=110)
rodas.settings(100, 300)
leitura_ultrassom = ultrassom.distance()

# Write your program here.





def sobe_empilhadeira():
    motorEmpilhadeira.run_time(-300, 2300) #para subir, parâmetro "speed" deve ser negativa
    return True

def desce_empilhadeira():
    motorEmpilhadeira.run_time(300, 2300)

def abre_ultrassom():
    motorUltrassom.run_time(200, 500) #para abrir, parâmetro "speed" deve ser positiva

def fecha_ultrassom():
    motorUltrassom.run_time(-200, 500)
    
def ve_cano():
    leitura_ultrassom = ultrassom.distance()

    if leitura_ultrassom < 60:
        return True

def posicao_cano():
    return True

def pega_cano():
    if ve_cano():
        if posicao_cano():
            rodas.straight(-30)
            abre_ultrassom()
            rodas.straight(150)
            estado_empilhadeira = sobe_empilhadeira()

def inicio():
    while True:
        if ve_cano():
            pega_cano()
        else:
            rodas.drive(80,0)

print(ultrassom.distance())


