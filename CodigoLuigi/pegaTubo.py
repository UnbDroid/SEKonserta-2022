from declaracoes import *
from cores import *
from andaPista import *

def desce_empilhadeira():
    global estado_empilhadeira

    motorEmpilhadeira.run_until_stalled(-250,then = Stop.BRAKE)
    motorEmpilhadeira.run_time(250, 800)
    estado_empilhadeira = "baixo"

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
    
    motorEmpilhadeira.run_time(250,700)
    
    rodas.straight(120)
    desce_empilhadeira()
    rodas.straight(100)
    sobe_empilhadeira()
    estado_empilhadeira = "cima"

    leitura_ultrassom = ultrassom.distance()
    print('aqui deu {}'.format(leitura_ultrassom))
    if leitura_ultrassom <= 15:
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
    
    le_sensor_cor()
    if ve_borda():
            atitude_borda()

    leitura_ultrassom = ultrassom.distance()
    print(leitura_ultrassom)
    ACHOU = False
    while not ACHOU:
        print(leitura_ultrassom)
        leituras_ultrassom = []
        rodas.straight(100)
        
        le_sensor_cor()
        if ve_borda():
            atitude_borda()

        leitura_ultrassom = ultrassom.distance()
        leituras_ultrassom.append(leitura_ultrassom)
        leituras_ultrassom.sort()
        print(leituras_ultrassom)
        if leituras_ultrassom[0] < tubo_esta_perto:
            ev3.speaker.beep()
            ACHOU = True
            break
        
        for i in range(6):
            if ACHOU:
                break
            rodas.turn(15)
            leitura_ultrassom = ultrassom.distance()
            leituras_ultrassom.append(leitura_ultrassom)
            leituras_ultrassom.sort()
            print(leituras_ultrassom)
            if leituras_ultrassom[0] < tubo_esta_perto:
                ev3.speaker.beep()
                ACHOU = True
                break
        if ACHOU:
            break
            
        rodas.turn(-90)
        leituras_ultrassom = []
        for i in range(6):
            if ACHOU:
                break
            rodas.turn(-15)
            leitura_ultrassom = ultrassom.distance()
            leituras_ultrassom.append(leitura_ultrassom)
            leituras_ultrassom.sort()
            print(leituras_ultrassom)
            if leituras_ultrassom[0] < tubo_esta_perto:
                ev3.speaker.beep()
                ACHOU = True
                break
        if ACHOU:
                break
        
        rodas.turn(90)
        leituras_ultrassom = []
        leitura_ultrassom = ultrassom.distance()

def teste_ultrassom():
    leitura_ultrassom = ultrassom.distance()
    print(leitura_ultrassom)

    if leitura_ultrassom < tubo_esta_perto:
        ev3.speaker.beep()
        