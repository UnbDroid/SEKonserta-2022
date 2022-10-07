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

#ultrassom = UltrasonicSensor(Port.S1)
ultrassom = InfraredSensor(Port.S1)
ultrassomLateral = UltrasonicSensor(Port.S2)
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



BORDA_ESQ_MIN = [0,0,0]
BORDA_ESQ_MAX = [2,2,2]

BORDA_DIR_MIN = [0,0,0]
BORDA_DIR_MAX = [2,2,2]

TURN_BORDA = 90

RAMPA_ESQ_MIN = [2, 15, 0]
RAMPA_ESQ_MAX = [6, 20, 3]

RAMPA_DIREITO_MIN_ = [2, 12, 6]
RAMPA_DIREITO_MAX = [8, 16, 14] 

TURN_RAMPA = 180

BRANCO_ESQ_MIN = [59, 68, 64]
BRANCO_ESQ_MAX = [100,100,100]
BRANCO_DIR_MIN = [82, 76, 100]
BRANCO_DIR_MAX = [100,100,100]

AMARELO_ESQ_MIN = [60, 42, 7]
AMARELO_ESQ_MAX = [72,50,11]
AMARELO_DIR_MIN = [82, 49, 23]
AMARELO_DIR_MAX = [96,54,26]

AZUL_ESQ_MIN = [2, 5, 6]
AZUL_ESQ_MAX = [6,10,13]
AZUL_DIR_MIN = [6, 9, 28]
AZUL_DIR_MAX = [11,15,36]

VERMELHO_ESQ_MIN = [46, 6, 2]
VERMELHO_ESQ_MAX = [55,10,5]
VERMELHO_DIR_MIN = [64, 9, 10]
VERMELHO_DIR_MAX = [73,13,16] 

PRETO_ESQ_MIN = [4, 6, 3]
PRETO_ESQ_MAX = [6,8,5]
PRETO_DIR_MIN = [9, 12, 13]
PRETO_DIR_MAX = [12,14,20] 
