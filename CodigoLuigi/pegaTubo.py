from declaracoes import *
from cores import *



def desce_empilhadeira(): #TODO Ele vai descer até forçar o motor?? E depois ele vai subir por 800ms?
    global estado_empilhadeira

    motorEmpilhadeira.run_until_stalled(-250,then = Stop.BRAKE) 
    motorEmpilhadeira.run_time(250, 800) #run_time(speed, time)
    estado_empilhadeira = "baixo"

def sobe_empilhadeira():
    global estado_ultrassom
    global estado_empilhadeira

    motorEmpilhadeira.run_until_stalled(250) #parametros: Velocidade (para subir, < 0), tempo;
    estado_empilhadeira = "cima"


'''def le_ultrassom():

    leitura_ultrassom = ultrassom.distance()
    
    print('ultrassom está lendo: ',leitura_ultrassom)
    return

def define_dist_chao_e_tubo():
    global leitura_ultrassom
    global distancia_chao
    global tubo_esta_perto

    distancia_chao = leitura_ultrassom
    tubo_esta_perto = distancia_chao - 8
    
    return distancia_chao, tubo_esta_perto
'''

def ve_tubo(): #Identifica se o ultrassom está lendo algo a frente
    global tubo_esta_perto

    if ultrassom.distance() < tubo_esta_perto:
        ev3.speaker.beep()
        return True

def define_intensidade_motor_ultrassom_pro_radar():
    global estado_ultrassom
 
    if estado_ultrassom == "esquerda":
        intensidade_motor = 50
        estado_ultrassom = "direita"
        
    else:
        intensidade_motor = -50
        estado_ultrassom = "esquerda"
    
    return intensidade_motor

def radar_tubo(): #essa função atua como um radar no tubo, escaneando sua largura.
    leitura_radar = []
    
    global estado_ultrassom
    global alinhado_ao_tubo

    alinhado_ao_tubo = True
    intensidade_motor_ultrassom = define_intensidade_motor_ultrassom_pro_radar()

    while not motorUltrassom.stalled():
        leitura_ultrassom = ultrassom.distance()
        leitura_radar.append(leitura_ultrassom)
        if leitura_ultrassom < 15:
            ev3.speaker.beep()
            return leitura_radar
            break
        motorUltrassom.run(intensidade_motor_ultrassom)

    return leitura_radar

def verifica_alinhado_ao_tubo(leitura_radar):
    global alinhado_ao_tubo
    vendo_branco = [23,24,25,26,27,28,29,30,31]

    for i in vendo_branco:
        if i in leitura_radar:
            alinhado_ao_tubo = False
        else:
            alinhado_ao_tubo = True

    return alinhado_ao_tubo

def pega_tubo():
    global estado_empilhadeira
    global estado_ultrassom
    global pegou_tubo

    rodas.straight(-30)
    if estado_empilhadeira == "cima":
        desce_empilhadeira()
    rodas.straight(150)
    sobe_empilhadeira()
    estado_empilhadeira = "cima"

    leitura_ultrassom = ultrassom.distance()
    
    print('aqui deu {}'.format(leitura_ultrassom))
    if leitura_ultrassom < 20:
        pegou_tubo = True

    else:
        pegou_tubo = False
        desce_empilhadeira()
        estado_empilhadeira = "baixo"

    return pegou_tubo
    
def entra_na_area_e_pega_tubo():
    global pegou_tubo

    while pegou_tubo != True:
        le_sensor_cor()
        if ve_borda():
            atitude_borda()

        elif ve_tubo():
            pegou_tubo = pega_tubo()
        else:
            rodas.drive(80,0)

def sai_da_area_com_tubo():
    global cor_da_area 
    global valorCorEquerda
    global valorCorDireita

    while not ve_preto():
        rodas.drive(-60,0)        

