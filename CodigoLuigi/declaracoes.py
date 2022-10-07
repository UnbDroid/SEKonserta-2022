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
ultrassom_lateral = UltrasonicSensor(Port.S2)
luzEsquerda = ColorSensor(Port.S3)
luzDireita = ColorSensor(Port.S4)

rodaDireita = Motor(Port.D)
rodaEsquerda = Motor(Port.C)
rodas = DriveBase(rodaEsquerda, rodaDireita, wheel_diameter= 41, axle_track=109) #axel track >= 109.5 < 109.8 foi demais. 108 foi demais
rodas.settings(130, 300) #velocidade_reto / aceleração reto / velocidade de giro / aceleração de giro

distancia_chao = 28
leitura_ultrassom = ultrassom.distance()
tubo_esta_perto = distancia_chao - 8
ValorCorEsquerda = luzEsquerda.rgb()
ValorCorDireita = luzDireita.rgb()

watch = StopWatch()

cor_da_area = "o café do cabeçs leva um MS"
estado_empilhadeira = "baixo"

pegou_tubo = False
alinhado_ao_tubo = False #identifica seo robô esta alinhado
alinhado_ao_preto = False
viu_borda = False

ordem_areas = []#lista que contém distância ao ponto inicial e sua respectiva área (que ainda será identificada)



BORDA_ESQ_MIN = [0,0,0]
BORDA_ESQ_MAX = [0,0,0]

BORDA_DIR_MIN = [0,0,0]
BORDA_DIR_MAX = [0,0,0]

TURN_BORDA = -90

RAMPA_ESQ_MIN = [0, 8, 0]
RAMPA_ESQ_MAX = [4, 17, 3]

RAMPA_DIREITO_MIN_ = [2, 9, 3]
RAMPA_DIREITO_MAX = [6, 22, 10] 

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
PRETO_ESQ_MAX = [8,13,8]
PRETO_DIR_MIN = [6, 12, 13]
PRETO_DIR_MAX = [16,22,20] 



# max rampa [15, 18, 10]