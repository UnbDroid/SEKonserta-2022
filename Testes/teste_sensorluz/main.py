#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import *
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import *
from pybricks.nxtdevices import LightSensor


watch = StopWatch()

def calibra_sensor_luz():
    contador = 0
    watch.reset()
    somador = 0
    while watch.time() < 10000:
        contador += 1
        ValorLuzEsquerda = LuzEsquerda.reflection()
        somador = ((somador*(contador - 1)) + ValorLuzEsquerda)/contador

    print(somador)



ev3 = EV3Brick()

LuzEsquerda = LightSensor(Port.S4)

while True:
    wait(100)
    ValorLuzEsquerda = LuzEsquerda.reflection()
    print(ValorLuzEsquerda)
    #calibra_sensor_luz()