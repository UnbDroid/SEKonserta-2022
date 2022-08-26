from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import *
import time
from pybricks.nxtdevices import *

ev3 = EV3Brick()

SensorCorDireita = ColorSensor(Port.S1)
SensorCorEsquerda = ColorSensor(Port.S2)
Giroscopio = GyroSensor(Port.S3)
UltrassomFrente = UltrasonicSensor(Port.S4)
RodaEsquerda = Motor(Port.D)
RodaDireita = Motor(Port.A)
MotorEmpilhadeira = Motor(Port.C)
MotorGarra = Motor(Port.B)
robot = DriveBase(RodaEsquerda, RodaDireita, wheel_diameter=40, axle_track=118)

tempo_empilhadeira = 1200
tempo_garra = 500


robot.settings(95,372,50,361)           # O padrão é (93,372,90,361) - (VELOCIDADE RETO, ACELERAÇÃO RETO, VELOCIDADE GIRANDO, ACELERAÇÃO GIRANDO)