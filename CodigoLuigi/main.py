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
mMotorUltrassom = Motor(Port.B)
motorDireito = Motor(Port.D)
motorEsquerdo = Motor(Port.C)

ultrassom = UltrasonicSensor(Port.S1)
giroscopio = GyroSensor(Port.S2)
luzEsquerda = LightSensor(Port.S3)
luzDireita = LightSensor(Port.S4)

rodaDireita = Motor(Port.D)
rodaEsquerda = Motor(Port.C)
rodas = DriveBase(rodaEsquerda, rodaDireita, wheel_diameter= 40, axle_track=110)

# Write your program here.

rodas = DriveBase(rodaEsquerda, rodaDireita, wheel_diameter= 40, axle_track=110)
rodas.settings(100, 300)


def sobre_empilhadera():
    run_time(30, 1000)

def abaixa_empilhadeira():
    pass
def pega_cano():
    pass

def inicio():
    run_time(30, 1000)

inicio()