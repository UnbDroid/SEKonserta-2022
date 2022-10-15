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
    motorUltrassom.run_time(500, 2500, then=Stop.BRAKE)
    #motorUltrassom.run_until_stalled(500)

def frente_ultrassom():
    motorUltrassom.run_time(-500, 2500, then=Stop.BRAKE)


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
    #print('O ULTRASSOM SUPERIOR LEU')
    print(leituras_ultrassom)

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
    rodas.straight(-120)

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
            alinha_robo(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX)
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

    rodas.straight(75)
    
    sobe_empilhadeira()
    estado_empilhadeira = "cima"

    #print('aqui deu {}'.format(leitura_ultrassom))
    #ve_ultrassom(100,100) == True or 
    if not ve_ultrassom(200,2000):
        pegou_tubo = True
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
            atitude(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX,TUpeRN_BORDA)

        elif leitura_ultrassom < 130: 
            pegou_tubo = pega_tubo()
        else:
            rodas.drive(80,0)
  
def sai_do_ponto_inicial_e_vai_pra_area():
    ordem_areas = getOrdemAreas()
    caixa_de_correio = getCaixaDeCorreio()
    distancia = 0
    index = 0
    
    print(ordem_areas)

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
    porcentagem = 0
    global pegou_tubo
    global estado_empilhadeira
    pegou = False
    largura_tubo = 0

    caixa_de_correio = getCaixaDeCorreio()
    rodas.reset()
    sobe_empilhadeira()
    distancia_que_percorreu = 0
    
    # for i in cores:
    #     if i == caixa_de_correio:
    #         index = cores.index(i)
    # leituras_ultrassom = numero_de_leituras[index]

    if caixa_de_correio == 'amarelo':
        tamanho_tubo = 100
    if caixa_de_correio == 'vermelho':
        tamanho_tubo = 150
    if caixa_de_correio == 'azul':
        tamanho_tubo = 200
    
    while distancia_terminal < 600:   
        largura_tubo = 0
        distancia_terminal = distancia_que_percorreu + rodas.distance()
        #print('dist terminal é: ',distancia_terminal
        #print(ultrassom_lateral.distance())
        if ultrassom_lateral.distance() > distancia_que_ve_tubo:
            le_sensor_cor()
            segue_linha_sensor_direito_prop(velocidade_robo)

        else: 
            ev3.speaker.beep()
            rodas.stop()                
            
            largura_tubo = rodas.distance()
            #300 é 5 cm, 600 é 10 cm, 1000 é 20 cm
            #while distancia_que_ve_tubo_min < ultrassom_lateral.distance() < distancia_que_ve_tubo_max:
            while ultrassom_lateral.distance() < distancia_que_ve_tubo:
                #print(ultrassom_lateral.distance())
                le_sensor_cor()
                segue_linha_sensor_direito_prop(velocidade_robo-20)
            
            ev3.speaker.beep()
            largura_tubo = rodas.distance() - largura_tubo
            print('a largura_tubo q ele leu é: ',largura_tubo)

            if largura_tubo < tamanho_tubo - 3:
                pass
            else:
                rodas.stop()
                if caixa_de_correio == 'azul':
                    rodas.straight(-80)
                if caixa_de_correio == 'vermelho':
                    rodas.straight(-50)
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
                        rodas.stop()
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


def volta_pro_comeco_area(distancia):
    rodas.turn(90)
    rodas.straight(-10)
    rodas.turn(75)
    rodas.reset()
    while rodas.distance() < distancia or ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX):
        le_sensor_cor()
        segue_linha_sensor_esquerdo_prop(120)
    rodas.stop()
    if ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX):
        le_sensor_cor()
        alinha_robo(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX)
        rodas.straight(-80)
    rodas.turn(180)

   
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

    #falhou uma
    rodas.reset()
    while distancia_terminal > -530:   
        listUltrassom = []
        listaVeReto = []
        print('distancia_terminal é = ',distancia_terminal)
        distancia_terminal = distancia_que_percorreu + rodas.distance()
        

        if ultrassom_lateral.distance() > distancia_que_valida_tubo:  
            rodas.drive(-velocidade_robo,0)
            
        else:
            while len(listUltrassom) < 300:
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
            

            if(porcentagem > 0.7): 
                rodas.stop()
                rodas.straight(95)
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










    


