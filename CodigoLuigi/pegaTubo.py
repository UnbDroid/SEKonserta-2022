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

def lado_ultrassom():
    motorUltrassom.run_time(-1500, 3000, then=Stop.BRAKE)

def frente_ultrassom():
    motorUltrassom.run_time(1000, 1500, then=Stop.BRAKE)

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
    #print(leituras_ultrassom)

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
        #print('ainda n vi preto')
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

    # rodas.reset()
    # while rodas.distance() < 400:
    #     segue_linha_sensor_esquerdo_prop(-100)
    rodas.straight(-365)
    rodas.turn(90)
    rodas.straight(40)
    desce_empilhadeira()
    rodas.straight(-100)

def pega_tubo():
    global estado_empilhadeira
    global estado_ultrassom
    global pegou_tubo

    rodas.straight(-50)
    if estado_empilhadeira == "cima":
        desce_empilhadeira()
    
    
    while not ve_ultrassom(100,120):
        le_sensor_cor()
        if ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX):
            rodas.stop()
            sai_da_area_cores()
            print('sai da area cores')
            break
        else:
            le_sensor_cor()
            rodas.drive(80,0)
    rodas.stop()

    # motorEmpilhadeira.run_time(-250,100)
    # rodas.turn(60)
    # rodas.turn(-60)

    rodas.straight(150)
    
    sobe_empilhadeira()
    estado_empilhadeira = "cima"

    #print('aqui deu {}'.format(leitura_ultrassom))
    #ve_ultrassom(100,100) == True or 
    if ve_ultrassom(100,30):
        pegou_tubo = True
        print('entrou aqui, vi o tubo')
        rodas.stop()
    else:
        pegou_tubo = False

    return pegou_tubo

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
  
def sai_do_ponto_inicial_e_vai_pra_area():
    ordem_areas = getOrdemAreas()
    caixa_de_correio = getCaixaDeCorreio()
    distancia = 0
    index = 0
    
    distancias_comeco_areas = [0,750,1500]

    for i in ordem_areas:
        print('a cor que o mario pediu é: ',caixa_de_correio)
        if i == caixa_de_correio:
            print('oq eu recebi e o que eu tenho é igual')
            index = ordem_areas.index(i)

    distancia = distancias_comeco_areas[index]
    print(ordem_areas)
    print('a dist qeu ele vai andar é: ',distancia)
    print('o index da lista é: ',index)
    
    rodas.reset()

    rodas.straight(-40)
    rodas.turn(-75)

    while rodas.distance() < distancia:
        le_sensor_cor()
        segue_linha_sensor_direito_prop(100)

def verifica_tubo_reto(distancia_que_ve_tubo,velocidade_robo):
    listaVeReto = []
    distancia_andada = []
    distancia_terminal = 0
    semValoresRepetidos = 0
    tubos_distancia = {}
    porcentagem = 0
    global pegou_tubo
    global estado_empilhadeira
    pegou = False

    caixa_de_correio = getCaixaDeCorreio()
    rodas.reset()
    sobe_empilhadeira()
    distancia_que_percorreu = 0

    
    while distancia_terminal < 660:   
        #print(ultrassom_lateral.distance())
        listUltrassom = []
        distancia_terminal = distancia_que_percorreu + rodas.distance()
        #print('dist terminal é: ',distancia_terminal)

        if ultrassom_lateral.distance() > distancia_que_ve_tubo:
            #print(ultrassom_lateral.distance())
            le_sensor_cor()
            segue_linha_sensor_direito_prop(velocidade_robo)

        else: 
            rodas.stop()        
            while len(listUltrassom) < 300:
                #print('tamanho da lista é:',len(listUltrassom))
                le_sensor_cor()
                segue_linha_sensor_direito_prop(velocidade_robo)
                listUltrassom.append(ultrassom_lateral.distance())          
            rodas.stop()

            print(listUltrassom)
            for i in listUltrassom:
                if(i <= distancia_que_ve_tubo - 10):
                    listaVeReto.append(i)
            
            print(listaVeReto)
            porcentagem = len(listaVeReto)/len(listUltrassom)
            #print(porcentagem)

            if(porcentagem > 0.7): 
                # while(ultrassom.distance() <= 25):
                #     ve_tubo_reto = True
                rodas.stop()
                rodas.straight(80)
                rodas.straight(-30)
                if caixa_de_correio == 'amarelo':
                    rodas.straight(-70)
                rodas.turn(90)
                estado_empilhadeira = "cima"
                distancia_que_percorreu = rodas.distance()
                if pega_tubo():
                    break
                else:
                    rodas.reset()
                    le_sensor_cor()
                    if ve_cor(BRANCO_ESQ_MIN, BRANCO_ESQ_MAX, BRANCO_DIR_MIN, BRANCO_DIR_MAX):
                        #print('entrou aqui1')
                        while not ve_cor(PRETO_ESQ_MIN, PRETO_ESQ_MAX, PRETO_DIR_MIN, PRETO_DIR_MAX):
                            le_sensor_cor()
                            rodas.drive(80,0)
                            alinha_robo(PRETO_ESQ_MIN,PRETO_ESQ_MAX,PRETO_DIR_MIN,PRETO_DIR_MAX) 
                        rodas.straight(-60)    
                    else:
                        #print('entrou aqui2')
                        sai_da_area_cores()    
                        rodas.turn(-75)
                    rodas.reset()
                    

                
    rodas.stop()
    print(pegou_tubo)
    return pegou_tubo
    #print('{}/{}'.format(len(listaVeReto),len(listUltrassom)))
    #print(listUltrassom)
    #print(porcentagem)

   
def acha_tubo():    
    if not verifica_tubo_reto(30,80):
        desce_empilhadeira()
        rodas.turn(94)
        rodas.straight(150)
        rodas.turn(94)

        rodas.reset()
        while rodas.distance() < 650:
            if ve_ultrassom(100,160):
                rodas.stop()
                #ev3.speaker.beep()
            else:
                rodas.drive(80,0)

def acha_tubo_re(distancia_que_ve_tubo,velocidade_robo): 
    listaVeReto = []
    distancia_andada = []
    distancia_terminal = 0
    semValoresRepetidos = 0
    tubos_distancia = {}
    porcentagem = 0
    global pegou_tubo
    global estado_empilhadeira
    distancia_que_percorreu = 0

    rodas.reset()
    while distancia_terminal > -590:   
        listUltrassom = []
        distancia_terminal = distancia_que_percorreu + rodas.distance()
        print('distancia_terminal é = ',distancia_terminal)

        if ultrassom_lateral.distance() > distancia_que_ve_tubo:  
            rodas.drive(-velocidade_robo,0)
            
        else:
            while len(listUltrassom) < 200:
                #print('tamanho da lista é:',len(listUltrassom))
                distancia_terminal = rodas.distance()
                rodas.drive(-velocidade_robo,0)
                listUltrassom.append(ultrassom_lateral.distance())          
            rodas.stop()

            print(listUltrassom)
            for i in listUltrassom:
                if(i <= distancia_que_ve_tubo - 10):
                    listaVeReto.append(i)
            
            print(listaVeReto)
            porcentagem = len(listaVeReto)/len(listUltrassom)
            #print(porcentagem)

            if(porcentagem > 0.7): 
                rodas.stop()
                rodas.straight(10)
                if caixa_de_correio == 'amarelo':
                    rodas.straight(120)
                rodas.turn(90)
                estado_empilhadeira = "cima"
                distancia_que_percorreu = distancia_que_percorreu + rodas.distance()
                if pega_tubo():
                    distancia_terminal = -1000
                else:
                    rodas.reset()
                    sai_da_area_cores()
                    rodas.turn(-90)
                    rodas.reset()

def loop_empilhadeira():
    while True:
        sobe_empilhadeira()
        desce_empilhadeira()










    


