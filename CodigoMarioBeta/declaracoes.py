from pybricks.hubs import EV3Brick
from pybricks.ev3devices import *
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import *
from pybricks.nxtdevices import LightSensor
from pybricks.nxtdevices import UltrasonicSensor as us

# Motores e Sensores
ev3 = EV3Brick()
#UltrassomDireita = UltrasonicSensor(Port.S1)
#UltrassomEsquerda = us(Port.S3)
#LuzDireita = LightSensor(Port.S3)
#SensorToque = TouchSensor(Port.S3)

LuzEsquerda = LightSensor(Port.S4)
watch = StopWatch()

# Variáveis
tempo_empilhadeira = 1600

ev3.speaker.set_speech_options('pt-br', 'f4')

