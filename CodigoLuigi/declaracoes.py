from math import*
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

motorEmpilhadeira = Motor(Port.A)
#motorUltrassom = Motor(Port.B)
motorDireito = Motor(Port.D)
motorEsquerdo = Motor(Port.C)

#ultrassom = UltrasonicSensor(Port.S1)
ultrassom = InfraredSensor(Port.S1)
giroscopio = GyroSensor(Port.S2)
luzEsquerda = ColorSensor(Port.S3)
luzDireita = ColorSensor(Port.S4)

rodaDireita = Motor(Port.D)
rodaEsquerda = Motor(Port.C)
rodas = DriveBase(rodaEsquerda, rodaDireita, wheel_diameter= 41, axle_track=110) #axel track >= 109.5 < 109.8 foi demais. 108 foi demais
rodas.settings(100, 300) #velocidade_reto / aceleração reto / velocidade de giro / aceleração de giro
leitura_ultrassom = ultrassom.distance()

cor_area = "vermelho"
estado_empilhadeira = "baixo"
estado_ultrassom = "esquerda"
pegou_tubo = False
alinhado_ao_tubo = False #identifica seo robô esta alinhado
tubo_esta_perto = 24
alinhado_ao_preto = False
lado_pista = "direito"
viu_borda = False

ValorCorEsquerda = luzEsquerda.rgb()
ValorCorDireita = luzDireita.rgb()