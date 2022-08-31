from pybricks.hubs import EV3Brick
from pybricks.ev3devices import *
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import *
from pybricks.nxtdevices import LightSensor

# Motores e Sensores
ev3 = EV3Brick()
UltrassomDireita = UltrasonicSensor(Port.S1)
UltrassomEsquerda = UltrasonicSensor(Port.S2)
LuzDireita = LightSensor(Port.S3)
LuzEsquerda = LightSensor(Port.S4)

# Variáveis
tempo_empilhadeira = 1600

