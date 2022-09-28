from declaracoes import *

def sobe_empilhadeira():
    global estado_ultrassom
    global estado_empilhadeira

    motorEmpilhadeira.run_until_stalled(250) #parametros: Velocidade (para subir, < 0), tempo;
    estado_empilhadeira = "cima"

def desce_empilhadeira():
    global estado_empilhadeira

    motorEmpilhadeira.run_until_stalled(-250,then = Stop.BRAKE)
    motorEmpilhadeira.run_time(250, 800)
    estado_empilhadeira = "baixo"

def desce_ultrassom():
    global estado_ultrassom

    motorUltrassom.run_until_stalled(-150, then = Stop.BRAKE) #Parametros: velocidade
    estado_ultrassom = "baixo"

def sobe_ultrassom(): 
    global estado_ultrassom

    motorUltrassom.run_until_stalled(150, then = Stop.BRAKE) 
    estado_ultrassom = "cima"
    
def ve_tubo(): #Identifica se o ultrassom está lendo algo a frente
    global tubo_esta_perto

    leitura_ultrassom = ultrassom.distance()
    if leitura_ultrassom < tubo_esta_perto:
        ev3.speaker.beep()
        return True
    
def radar_tubo(): #essa função atua como um radar no tubo, escaneando sua largura. Devolve a %
    leitura_radar = []
    percebe_cano_em_frente = 0
    angulo_inicial = 0
    angulo_da_menor_leitura = 0
    menor_leitura = 50
    angulo_depois_do_giro = 0
    variacao_de_angulo = 0
    global leitura_tubo_porcentagem 
    global leitura_ultrassom 
    global tubo_esta_perto
    
    angulo_inicial = giroscopio.angle()
    rodas.turn(50)
    angulo_depois_do_giro = giroscopio.angle()

    variacao_de_angulo = angulo_depois_do_giro - angulo_inicial
    while giroscopio.angle() > (angulo_inicial-variacao_de_angulo):
        leitura_ultrassom = ultrassom.distance()

        if leitura_ultrassom <= tubo_esta_perto:
            percebe_cano_em_frente += 1
            if leitura_ultrassom < menor_leitura:
                menor_leitura = leitura_ultrassom
                angulo_da_menor_leitura = giroscopio.angle()

        leitura_radar.append(leitura_ultrassom)
        rodas.drive(0,-30)
    rodas.stop()

    leitura_tubo_porcentagem = percebe_cano_em_frente/len(leitura_radar) #as vezes da o erro de divisão por zero, pq daria zero em algum momento?
    
    rodas.turn(variacao_de_angulo)

    print('{} = {} / {} '.format(leitura_tubo_porcentagem,percebe_cano_em_frente,len(leitura_radar)))
    '''print(menor_leitura)
    print(angulo_da_menor_leitura)
    print(giroscopio.angle())
    '''

def valida_se_esta_vendo_tubo():
    global alinhado_ao_tubo
    global cor_da_area
    global leitura_tubo_porcentagem 
    
    if 0.56 > (leitura_tubo_porcentagem) > 0.14:
        alinhado_ao_tubo = True    
    else:
        alinhado_ao_tubo = False

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
    if leitura_ultrassom < 20:
        pegou_tubo = True
        sobe_ultrassom()
        estado_ultrassom = "cima"
    else:
        pegou_tubo = False
        desce_empilhadeira()
        estado_empilhadeira = "baixo"

    return pegou_tubo

    
    
'''if cor_da_area == "amarelo": #tubo de 10 cm
    if 0.26 > (leitura_tubo_porcentagem) > 0.14:
        alinhado_ao_tubo = True

if cor_da_area == "vermelho": #tubo de 15 cm
    if 0.36 > (leitura_tubo_porcentagem) > 0.26:
        alinhado_ao_tubo = True

if cor_da_area == "azul": #tubo de 20 cm
    if 0.55 > (leitura_tubo_porcentagem) > 0.4:
        alinhado_ao_tubo = True'''


def teste_ultrassom():
    leitura_ultrassom = ultrassom.distance()
    print(leitura_ultrassom)

    if leitura_ultrassom < tubo_esta_perto:
        ev3.speaker.beep()
def teste_radar(x_vezes):
    for i in range(x_vezes):
        radar_tubo()
