from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import *
import time
#from pybricks.nxtdevices import *

ev3 = EV3Brick()

SensorCorDireita = ColorSensor(Port.S1)
SensorCorEsquerda = ColorSensor(Port.S2)
#Giroscopio = GyroSensor(Port.S3)
UltrassomEsquerda = UltrasonicSensor(Port.S3)
UltrassomFrente = UltrasonicSensor(Port.S4)
RodaEsquerda = Motor(Port.D)
RodaDireita = Motor(Port.A)
MotorEmpilhadeira = Motor(Port.C)
MotorGarra = Motor(Port.B)
robot = DriveBase(RodaEsquerda, RodaDireita, wheel_diameter=41, axle_track=109.4) #axle_track antigo -> 118
watch = StopWatch()
watch2 = StopWatch()
watch_virada = StopWatch()

FIM_DO_PROGRAMA = False
TUBO_ENTREGUE = False




robot.settings(130,372,150,361)        #Usei 50 vel ang   # O padrão é (93,372,90,361) - (VELOCIDADE RETO, ACELERAÇÃO RETO, VELOCIDADE GIRANDO, ACELERAÇÃO GIRANDO)
ev3.speaker.set_volume(100)
ev3.speaker.say('Poggers poggers poggers poggers')
ev3.speaker.set_speech_options('pt-br', 'f4')
ev3.speaker.set_volume(100)
#ev3.speaker.say('Oi saudades, eu sou o Mário e eu falooo')
robot.stop()
RodaEsquerda.stop()
RodaDireita.stop()
#print(RodaEsquerda.control.limits(800,1600,300))          # O padrão é (800, 1600, 100)
#print(RodaDireita.control.limits(800,1600,300))