from declaracoes import *
from cores import *
from andaPista import *

def sobe_empilhadeira():
    global estado_ultrassom
    global estado_empilhadeira

    motorEmpilhadeira.run_until_stalled(250) #parametros: Velocidade (para subir, < 0), tempo;
    estado_empilhadeira = "cima"

def ve_tubo(): #Identifica se o ultrassom está lendo algo a frente
    global tubo_esta_perto

    leitura_ultrassom = ultrassom.distance()
    print(leitura_ultrassom)
    if leitura_ultrassom < tubo_esta_perto:
        ev3.speaker.beep()
        return True


def pega_tubo():
    global estado_empilhadeira
    global estado_ultrassom
    global pegou_tubo

    rodas.straight(-30)
    if estado_empilhadeira == "cima":
        desce_empilhadeira()
    
    #motorEmpilhadeira.run_time(250,700)
    
    rodas.straight(120)
    desce_empilhadeira()
    rodas.straight(100)
    sobe_empilhadeira()
    estado_empilhadeira = "cima"

    leitura_ultrassom = ultrassom.distance()
    print('aqui deu {}'.format(leitura_ultrassom))
    if leitura_ultrassom <= 24:
        pegou_tubo = True

    else:
        pegou_tubo = False
        desce_empilhadeira()
        estado_empilhadeira = "baixo"
    print(pegou_tubo)
    return pegou_tubo
    
def entra_na_area_e_pega_tubo():
    global pegou_tubo

    while not pegou_tubo:
        le_sensor_cor()
        if ve_borda():
            atitude_borda()

        elif ve_tubo():
            pegou_tubo = pega_tubo()
        else:
            rodas.drive(80,0)

def sai_da_area_com_tubo():
    global cor_area
    global valorCorEquerda
    global valorCorDireita

    while not ve_preto():
        rodas.drive(-60,0)

def procura_tubo():
    global tubo_esta_perto

    leitura_ultrassom = ultrassom.distance()
    while leitura_ultrassom > tubo_esta_perto:
        print(leitura_ultrassom)
        le_sensor_cor()
        if ve_borda():
            atitude_borda()
        rodas.stop()
        ev3.speaker.beep()
        rodaEsquerda.run_time(350, 2000, then=Stop.BRAKE, wait=False)
        leitura_ultrassom = ultrassom.distance()
        if leitura_ultrassom < tubo_esta_perto:
            ev3.speaker.beep()
            break
        rodaDireita.run_time(350, 2000, then=Stop.BRAKE, wait=True)
        
        rodas.turn(90)
        leitura_ultrassom = ultrassom.distance()
        if leitura_ultrassom < tubo_esta_perto:
            ev3.speaker.beep()
            break
        rodas.turn(-180)
        leitura_ultrassom = ultrassom.distance()
        if leitura_ultrassom < tubo_esta_perto:
            ev3.speaker.beep()
            break
        rodas.turn(90)
        leitura_ultrassom = ultrassom.distance()

def teste_ultrassom():
    leitura_ultrassom = ultrassom.distance()
    print(leitura_ultrassom)

    if leitura_ultrassom < tubo_esta_perto:
        ev3.speaker.beep()
        