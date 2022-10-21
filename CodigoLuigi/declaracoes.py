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
ultrassom = UltrasonicSensor(Port.S2)
ultrassom_lateral = InfraredSensor(Port.S1)
luzEsquerda = ColorSensor(Port.S3)
luzDireita = ColorSensor(Port.S4)

rodaDireita = Motor(Port.D)
rodaEsquerda = Motor(Port.C)
rodas = DriveBase(rodaEsquerda, rodaDireita, wheel_diameter= 41, axle_track=108) #axel track >= 109.5 < 109.8 foi demais. 108 foi demais
rodas.settings(100, 270, 150) #velocidade_reto / aceleração reto / velocidade de giro / aceleração de giro

distancia_chao = 210
caixa_de_correio = 'amarelo'
tubo_pra_devolver = ''
pegou_tubo = False
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

# ordem_areas = []#lista que contém distância ao ponto inicial e sua respectiva área (que ainda será identificada)
ordem_areas = ['vermelho','amarelo','azul']
# ordem_areas = ['azul','vermelho','amarelo']
#ordem_areas = ['amarelo']
# ordem_areas = ['vermelho','azul','amarelo']


BORDA_ESQ_MIN = [0,0,0]
BORDA_ESQ_MAX = [2,2,2]

BORDA_DIR_MIN = [0,0,0]
BORDA_DIR_MAX = [2,2,2]

TURN_BORDA = -90

RAMPA_ESQ_MIN = [5, 35, 13]
RAMPA_ESQ_MAX = [10, 40, 16]
RAMPA_DIREITO_MIN_ = [7, 31,39]
RAMPA_DIREITO_MAX = [11, 48, 44] 

TURN_RAMPA = 180

BRANCO_ESQ_MIN = [65, 75, 78]
BRANCO_ESQ_MAX = [70,82,82]
BRANCO_DIR_MIN = [87, 87, 99]
BRANCO_DIR_MAX = [94,94,100]

AMARELO_ESQ_MIN = [60, 40, 10]
AMARELO_ESQ_MAX = [67,50,16]
AMARELO_DIR_MIN = [81, 47, 35]
AMARELO_DIR_MAX = [93,56,41]

AZUL_ESQ_MIN = [46, 30, 6]
AZUL_ESQ_MAX = [12,38,58]
AZUL_DIR_MIN = [13, 36, 99]
AZUL_DIR_MAX = [18,46,100]

VERMELHO_ESQ_MIN = [40, 5, 2]
VERMELHO_ESQ_MAX = [52,10,7]
VERMELHO_DIR_MIN = [64, 9, 15]
VERMELHO_DIR_MAX = [77,15,19] 

PRETO_ESQ_MIN = [4, 7, 3]
PRETO_ESQ_MAX = [8,11,6]
PRETO_DIR_MIN = [7, 10, 11]
PRETO_DIR_MAX = [10,13,15] 





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

def setTuboPraDevolver(valor):
    global tubo_pra_devolver
    tubo_pra_devolver = valor
    
def getTuboPraDevolver():
    global tubo_pra_devolver
    return tubo_pra_devolver

def setPegouTubo(valor):
    global pegou_tubo
    pegou_tubo = valor
    
def getPegouTubo():
    global pegou_tubo
    return pegou_tubo

def setPontoInicial(valor):
    global ponto_inicial
    ponto_inicial = valor
    
def setPontoInicial():
    global ponto_inicial
    return ponto_inicial