from declaracoes import *
from pegaTubo import *
from cores import *


SENSOR_ESQUERDO_MIN_BORDA = [0,0,0]
SENSOR_ESQUERDO_MAX_BORDA = [2,2,2]

SENSOR_DIREITO_MIN_BORDA = [0,0,0]
SENSOR_DIREITO_MAX_BORDA = [2,2,2]

TURN_BORDA = 90

SENSOR_ESQUERDO_MIN_RAMPA = [2, 15, 0]
SENSOR_ESQUERDO_MAX_RAMPA = [6, 20, 3]

SENSOR_DIREITO_MIN_RAMPA = [2, 12, 6]
SENSOR_DIREITO_MAX_RAMPA = [8, 16, 14] 

TURN_RAMPA = 180


def ajustes_comeco():
    desce_empilhadeira()

def desvia(turn):  
    rodas.stop()
    rodas.straight(-60) #[DESCRICAO] dá ré
    rodas.turn(turn)

def atitude(eq_min, eq_max, dr_min, dr_max, turn): #atitudes que ele deve tomar logo que ve a borda, se alinha e desvia
    alinha_robo(eq_min, eq_max, dr_min, dr_max)
    desvia(turn)


def desvia_mario():
    if ultrassom.distance() < 20:
        rodas.straight(-60)
        rodas.turn(90)

def comeco():
    viu_preto = False
    ajustes_comeco() #[DESCRICAO] basicamente ele desce a empilhadeira aqui

    while viu_preto == False:
        desvia_mario() 
        le_sensor_cor() 
        if ve_borda(): 
            atitude(SENSOR_ESQUERDO_MIN_BORDA, SENSOR_ESQUERDO_MAX_BORDA, SENSOR_DIREITO_MIN_BORDA, SENSOR_DIREITO_MAX_BORDA, TURN_BORDA)
        elif ve_rampa(): 
            atitude(SENSOR_ESQUERDO_MIN_RAMPA, SENSOR_ESQUERDO_MAX_RAMPA, SENSOR_DIREITO_MIN_RAMPA, SENSOR_DIREITO_MAX_RAMPA, TURN_RAMPA)   
        elif ve_preto(): 
            alinha_preto_frente() #[DESCRICAO] se alinha
            viu_preto = True
        else:
            rodas.drive(80,0) #[DESCRICAO] drive (speed, turn_rate)
    rodas.stop()
    rodas.straight(40) #[DESCRICAO] andar reto por 40mm (distance)

        #identifica a cor e seta como zero. Se puder virar p esquerda, vira e conta a distância, se não, vira p direita e conta a distância. Assim ele vai conseguir identificar as 3 cores

    
