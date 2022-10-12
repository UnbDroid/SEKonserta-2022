from cores import *

def desce_empilhadeira(): #TODO Ele vai descer até forçar o motor?? E depois ele vai subir por 800ms?
    global estado_empilhadeira

    motorEmpilhadeira.run_until_stalled(-250,then = Stop.BRAKE) 
    #motorEmpilhadeira.run_time(250, 750) #run_time(speed, time)
    estado_empilhadeira = "baixo"

def sobe_empilhadeira():
    global estado_ultrassom
    global estado_empilhadeira

    motorEmpilhadeira.run_until_stalled(250) #parametros: Velocidade (para subir, < 0), tempo;
    estado_empilhadeira = "cima"

def media_ponderada(lista):
    lista_aux = lista.copy()
    elementos = sorted(set(lista))
    pesos = []
    vezes_que_aparece  = 0
    numerador = 0
    denominador = 0

    for i in elementos:
        while i in lista_aux:
            vezes_que_aparece  += 1
            lista_aux.remove(i)
        pesos.append(vezes_que_aparece)
        vezes_que_aparece  = 0

    for i in range(len(elementos)):
        numerador += elementos[i]*pesos[i]
        denominador += pesos[i]

    return numerador/denominador

def ve_ultrassom(num_leituras,quanto_quero_que_leia):
    leituras_ultrassom = []
    leu_certo = []
    viu = False

    for i in range(num_leituras):
        leituras_ultrassom.append(ultrassom.distance())

    for i in leituras_ultrassom:
        if(i <= quanto_quero_que_leia):
            leu_certo.append(i)

    porcentagem = len(leu_certo)/len(leituras_ultrassom)
    #print('aqui: ',porcentagem)
    #print(leituras_ultrassom)

    if porcentagem > 0.7:
        viu = True

    return viu

def sai_da_area_cores():
    while not ve_cor(PRETO_ESQ_MIN, PRETO_ESQ_MAX, PRETO_DIR_MIN, PRETO_DIR_MAX):
        le_sensor_cor()
        rodas.drive(-80,0) #sai da area 1
    alinha_preto_re()
    rodas.straight(-60)


def ve_tubo(): #Identifica se o ultrassom está lendo algo a frente
    global tubo_esta_perto

    if ultrassom.distance() < tubo_esta_perto:
        ev3.speaker.beep()
        return True

def posiciona_tubo_mario():
    rodas.turn(75)

    while not ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX): 
        le_sensor_cor()
        segue_linha_sensor_esquerdo_prop(100)

    rodas.straight(-150)
    rodas.turn(90)
    desce_empilhadeira()

def pega_tubo():
    global estado_empilhadeira
    global estado_ultrassom
    global pegou_tubo

    rodas.straight(-50)
    if estado_empilhadeira == "cima":
        desce_empilhadeira()
    
    while not ve_ultrassom(100,120):
        rodas.drive(80,0)
    rodas.stop()
    
    sobe_empilhadeira()
    estado_empilhadeira = "cima"

    #print('aqui deu {}'.format(leitura_ultrassom))
    if ve_ultrassom(100,100) == True or ve_ultrassom(100,2550):
        pegou_tubo = True
    else:
        pegou_tubo = False
        desce_empilhadeira()
        estado_empilhadeira = "baixo"

    return pegou_tubo

def encontra_tubo_com_ultrassom_lateral():
    global cor_pega_tubo
    achou = False

    ev3.speaker.beep()
    cores = ['amarelo','vermelho','azul']
    tamanhos = [100,150,200]
    tamanho_do_tubo = 0
    leituras_ultrassom = []

    for i in cores:
        if i == cor_pega_tubo:
            index_em_cores = cores.index(i)
    
    tamanho_do_tubo = tamanhos[index_em_cores]
    print(tamanho_do_tubo)

    while ultrassom_lateral.distance() > 40:
        segue_linha_sensor_direito_prop(100)
    rodas.stop()

    rodas.reset()
    while ultrassom_lateral.distance() < 50:
        leituras_ultrassom.append(ultrassom_lateral.distance())
        rodas.drive(80,0)
    
    rodas.stop()
    distancia = rodas.distance()
    print(distancia)
    if rodas.distance() >= tamanho_do_tubo:
        rodas.straight(-((2*tamanho_do_tubo)/3))
        achou = True

    return achou
    #print(leituras_ultrassom)

def entra_na_area_e_pega_tubo():
    global pegou_tubo
    global estado_empilhadeira
    desce_empilhadeira()
    estado_empilhadeira = 'baixo'

    while pegou_tubo != True:
        leitura_ultrassom = ve_ultrassom(100)
        le_sensor_cor()
        if ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX) :
            atitude(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX,TURN_BORDA)

        elif leitura_ultrassom < 130: 
            pegou_tubo = pega_tubo()
        else:
            rodas.drive(80,0)
  
def sai_do_ponto_inicial_e_pega_tubo():
    ordem_areas = getOrdemAreas()
    global cor_pega_tubo
    
    distancia = 0
    index = 0
    
    distancias_comeco_areas = [0,750,1500]
    for i in ordem_areas:
        if i == cor_pega_tubo:
            index = ordem_areas.index(cor_pega_tubo)

    distancia = distancias_comeco_areas[index]
    
    rodas.reset()

    rodas.straight(-40)
    rodas.turn(-75)

    while rodas.distance() < distancia:
        segue_linha_sensor_direito_prop(100)
    
    if encontra_tubo_com_ultrassom_lateral():
        rodas.turn(90)
        '''while not ve_cor(PRETO_ESQ_MIN, PRETO_ESQ_MAX, PRETO_DIR_MIN, PRETO_DIR_MAX):
            rodas.drive(80,0)
        alinha_preto_frente()'''
        entra_na_area_e_pega_tubo()
        sai_da_area_cores()

def verifica_tubo_reto(distancia_que_ve_tubo,velocidade_robo):
    listaVeReto = []
    distancia_andada = []
    distancia_terminal = 0
    semValoresRepetidos = 0
    tubos_distancia = {}
    porcentagem = 0
    global pegou_tubo
    global estado_empilhadeira

    rodas.reset()

    sobe_empilhadeira()

    
    while distancia_terminal < 840:   
        listUltrassom = []
        
        while ultrassom_lateral.distance() > distancia_que_ve_tubo:
            segue_linha_sensor_direito_prop(velocidade_robo)
        rodas.stop()
        
        while len(listUltrassom) < 2000:
            rodas.drive(velocidade_robo,0)
            listUltrassom.append(ultrassom_lateral.distance())          
        rodas.stop()

        for i in listUltrassom:
            if(i <= distancia_que_ve_tubo - 10):
                listaVeReto.append(i)

        porcentagem = len(listaVeReto)/len(listUltrassom)
        #print(porcentagem)

        if(porcentagem > 0.7): 
            while(ultrassom.distance() <= 25):
                ve_tubo_reto = True
            rodas.stop()
            #rodas.straight(-45)
            rodas.turn(90)
            estado_empilhadeira = "cima"
            pegou_tubo = pega_tubo()            
            break

        distancia_terminal = rodas.distance()
    rodas.stop()
    #print('{}/{}'.format(len(listaVeReto),len(listUltrassom)))
    #print(listUltrassom)
    #print(porcentagem)

   

def loop_empilhadeira():
    while True:
        sobe_empilhadeira()
        desce_empilhadeira()










    


