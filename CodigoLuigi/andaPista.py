from declaracoes import *
from cores import *
from pegaTubo import *


def ajustes_comeco():
    desce_empilhadeira()

def desvia(turn):  
    rodas.stop()
    rodas.straight(-60) 
    rodas.turn(turn)

def atitude(eq_min, eq_max, dr_min, dr_max, turn): 
    alinha_robo(eq_min, eq_max, dr_min, dr_max)
    desvia(turn)


def desvia_mario():
    if ultrassom.distance() < 20:
        rodas.straight(-60)
        rodas.turn(90)

def comeco():
    viu_preto = False
    ajustes_comeco() 

    while viu_preto == False:
        desvia_mario() 
        le_sensor_cor() 
        
        if ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX): 
            atitude(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX, TURN_BORDA)

        elif ve_cor(RAMPA_ESQ_MIN, RAMPA_ESQ_MAX, RAMPA_DIREITO_MIN_, RAMPA_DIREITO_MAX):
            atitude(RAMPA_ESQ_MIN, RAMPA_ESQ_MAX, RAMPA_DIREITO_MIN_, RAMPA_DIREITO_MAX, TURN_RAMPA)

        elif ve_cor(PRETO_ESQ_MIN, PRETO_ESQ_MAX, PRETO_DIR_MIN, PRETO_DIR_MAX): 
            alinha_preto_frente() 
            viu_preto = True
        else:
            rodas.drive(80,0) 
    rodas.stop()
    rodas.straight(40) 

        

    
