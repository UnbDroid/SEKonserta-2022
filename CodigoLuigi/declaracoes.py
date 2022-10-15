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
motorUltrassom = Motor(Port.B)

#ultrassom = UltrasonicSensor(Port.S1)
ultrassom = UltrasonicSensor(Port.S2)
ultrassom_lateral = InfraredSensor(Port.S1)
luzEsquerda = ColorSensor(Port.S3)
luzDireita = ColorSensor(Port.S4)

rodaDireita = Motor(Port.D)
rodaEsquerda = Motor(Port.C)
rodas = DriveBase(rodaEsquerda, rodaDireita, wheel_diameter= 41, axle_track=114) #axel track >= 109.5 < 109.8 foi demais. 108 foi demais
rodas.settings(100, 270, 150) #velocidade_reto / aceleração reto / velocidade de giro / aceleração de giro

distancia_chao = 210
caixa_de_correio = ''
#caixa_de_correio = ['vermelho','nada']
distancia_primeira_cor_do_ponto_inicial = 0
leitura_ultrassom = ultrassom.distance()
tubo_esta_perto = distancia_chao - 8
ValorCorEsquerda = luzEsquerda.rgb()
ValorCorDireita = luzDireita.rgb()

watch = StopWatch()

cor_da_area = "nada"
estado_empilhadeira = "cima"

comeco = True
eq = False
dr = False
pegou_tubo = False
alinhado_ao_tubo = False #identifica seo robô esta alinhado
alinhado_ao_preto = False
viu_borda = False

ordem_areas = []#lista que contém distância ao ponto inicial e sua respectiva área (que ainda será identificada)
#ordem_areas = ['amarelo','vermelho','azul']
#ordem_areas = ['amarelo']


BORDA_ESQ_MIN = [0,0,0]
BORDA_ESQ_MAX = [2,2,2]

BORDA_DIR_MIN = [0,0,0]
BORDA_DIR_MAX = [2,2,2]

TURN_BORDA = -90

RAMPA_ESQ_MIN = [0, 8, 0]
RAMPA_ESQ_MAX = [10, 20, 5]
RAMPA_DIREITO_MIN_ = [2, 9, 3]
RAMPA_DIREITO_MAX = [6, 22, 11] 

TURN_RAMPA = 180

BRANCO_ESQ_MIN = [59, 68, 64]
BRANCO_ESQ_MAX = [100,100,100]
BRANCO_DIR_MIN = [82, 76, 100]
BRANCO_DIR_MAX = [100,100,100]

AMARELO_ESQ_MIN = [60, 40, 7]
AMARELO_ESQ_MAX = [74,50,13]
AMARELO_DIR_MIN = [82, 40, 23]
AMARELO_DIR_MAX = [100,60,30]

AZUL_ESQ_MIN = [2, 5, 6]
AZUL_ESQ_MAX = [7,10,15]
AZUL_DIR_MIN = [6, 9, 25]
AZUL_DIR_MAX = [11,15,40]

VERMELHO_ESQ_MIN = [45, 5, 2]
VERMELHO_ESQ_MAX = [60,10,5]
VERMELHO_DIR_MIN = [64, 9, 10]
VERMELHO_DIR_MAX = [85,15,17] 

PRETO_ESQ_MIN = [4, 5, 3]
PRETO_ESQ_MAX = [20,20,10]
PRETO_DIR_MIN = [6, 11, 13]
PRETO_DIR_MAX = [20,22,20] 



# max rampa [15, 18, 10]

def setCores(valor):
    global cor_da_area
    cor_da_area = valor

def getCores():
    global cor_da_area
    return cor_da_area

def setDr(valor):
    global dr
    dr = valor

def getDr():
    global dr
    return dr

def setEq(valor):
    global eq
    eq = valor

def getEq():
    global eq
    return eq

def setValorCorEsquerda(valor):
    global ValorCorEsquerda
    ValorCorEsquerda = valor

def getValorCorEsquerda():
    global ValorCorEsquerda
    return ValorCorEsquerda

def setValorCorDireita(valor):
    global ValorCorDireita
    ValorCorDireita = valor
    
def getValorCorDireita():
    global ValorCorDireita
    return ValorCorDireita

def setOrdemAreas(valor):
    global ordem_areas
    ordem_areas = valor
    
def getOrdemAreas():
    global ordem_areas
    return ordem_areas

def setCaixaDeCorreio(valor):
    global caixa_de_correio
    caixa_de_correio = valor
    
def getCaixaDeCorreio():
    global caixa_de_correio
    return caixa_de_correio