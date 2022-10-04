from pegaTubo import *
from declaracoes import *
from pegaTubo import *
from cores import *

def desce_empilhadeira():
    global estado_empilhadeira

    motorEmpilhadeira.run_until_stalled(-250,then = Stop.BRAKE)
    motorEmpilhadeira.run_time(250, 800)
    estado_empilhadeira = "baixo"

def ajustes_comeco():
    desce_empilhadeira()

def desvia_borda():
    rodas.stop()
    rodas.straight(-60)
    rodas.turn(90)

def desvia_rampa():
    rodas.stop()
    rodas.straight(-60)
    rodas.turn(180)

def atitude_borda(): #atitudes que ele deve tomar logo que ve a borda, se alinha e desvia
    alinha_borda()
    desvia_borda()

def atitude_rampa(): #atitudes que ele deve tomar logo que ve a rampa, se alinha e desvia
    alinha_rampa()
    desvia_rampa() 


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
        if ve_borda():
            atitude_borda()
        elif ve_rampa():
            atitude_rampa()     
        elif ve_preto():
            alinha_preto_frente()
            viu_preto = True
        else:
            rodas.drive(80,0)
    rodas.stop()
    rodas.straight(40)

        #identifica a cor e seta como zero. Se puder virar p esquerda, vira e conta a distância, se não, vira p direita e conta a distância. Assim ele vai conseguir identificar as 3 cores

    
