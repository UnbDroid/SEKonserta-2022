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
        le_sensor_cor()
        rodas.drive(-80,0)
    rodas.straight(-40)
    rodas.stop()
    
    #alinha_robo(BRANCO_ESQ_MIN, BRANCO_ESQ_MAX, BRANCO_DIR_MIN, BRANCO_DIR_MAX)

    # while not ve_cor(PRETO_ESQ_MIN, PRETO_ESQ_MAX, PRETO_DIR_MIN, PRETO_DIR_MAX):
    #     print('ainda n vi preto')
    #     le_sensor_cor()
    #     rodas.drive(-80,0) #sai da area 1
    # alinha_preto_re()
    # rodas.straight(-60)


def ve_tubo(): #Identifica se o ultrassom está lendo algo a frente
    global tubo_esta_perto

    if ultrassom.distance() < tubo_esta_perto:
        ev3.speaker.beep()
        return True

def posiciona_tubo_mario():
    pegou_tubo = getPegouTubo()

    print('entrou no posicina_tubo_mario')
    #rodas.straight(30)
    rodas.turn(75)
    while not ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX): 
        le_sensor_cor()
        segue_linha_sensor_esquerdo_prop(100)
    rodas.straight(-365)
    rodas.turn(90)
    desce_empilhadeira()
    rodas.straight(-50)
    sobe_empilhadeira()
    #motorEmpilhadeira.run_time(250,1000)
    rodas.straight(120) #20
    if getCaixaDeCorreio() == 'amarelo': #ir mais pra frente se for um de 10!
        rodas.straight(20)
        rodas.straight(-60)
    else:
        rodas.straight(-40)
    #sobe_empilhadeira()

    pegou_tubo = False


def pega_tubo():
    global estado_empilhadeira
    global estado_ultrassom
    pegou_tubo = getPegouTubo()
    viu_borda = False

    rodas.straight(-50)
    if estado_empilhadeira == "cima":
        desce_empilhadeira()
    
    while not ve_ultrassom(100,120):
        le_sensor_cor()
        if ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX):
            le_sensor_cor()
            alinha_robo(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX)
            rodas.stop()
            sai_da_area_cores()
            rodas.turn(-90)
            print('sai da area cores')
            viu_borda = True
            break
        else:
            rodas.drive(80,0)
    rodas.stop()

    if not viu_borda:
        rodas.straight(80)

    # motorEmpilhadeira.run_time(-250,100)
    # rodas.turn(60)
    # rodas.turn(-60)

    sobe_empilhadeira()
    estado_empilhadeira = "cima"

    #print('aqui deu {}'.format(leitura_ultrassom))
    #ve_ultrassom(100,100) == True or 
    if not ve_ultrassom(200,2000):
        pegou_tubo = True
        rodas.stop()
    else:
        pegou_tubo = False
        
    
    setPegouTubo(pegou_tubo)
    print('printtei o tubo aq',pegou_tubo)
    return pegou_tubo

def entra_na_area_e_pega_tubo():
    pegou_tubo = getPegouTubo()
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
    viu_borda = False
    
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

    rodas.straight(-30)
    rodas.turn(-80)

    if distancia > 0:
        while rodas.distance() < distancia:
            le_sensor_cor()
            segue_linha_sensor_direito_prop(100)

def verifica_tubo_reto(distancia_que_ve_tubo,velocidade_robo,dist_area):
    distancia_terminal = 0
    pegou_tubo = getPegouTubo()
    global estado_empilhadeira
    largura_tubo = 0

    caixa_de_correio = getCaixaDeCorreio()
    rodas.reset()
    sobe_empilhadeira()
    distancia_que_percorreu = 0


    if caixa_de_correio == 'amarelo':
        tamanho_tubo = 100
    if caixa_de_correio == 'vermelho':
        tamanho_tubo = 150
    if caixa_de_correio == 'azul':
        tamanho_tubo = 200
    
    while distancia_terminal < dist_area:   
        largura_tubo = 0
        distancia_terminal = distancia_que_percorreu + rodas.distance()
        #print('dist terminal é: ',distancia_terminal
        #print(ultrassom_lateral.distance())
        if ultrassom_lateral.distance() > distancia_que_ve_tubo:
            distancia_terminal = distancia_que_percorreu + rodas.distance()
            le_sensor_cor()
            segue_linha_sensor_direito_prop(velocidade_robo)

        else: 
            print('cheguei a ler o comeco do tubo')
            ev3.speaker.beep()
            rodas.stop()                
            
            largura_tubo = rodas.distance()
            while ultrassom_lateral.distance() < distancia_que_ve_tubo:
                #print(ultrassom_lateral.distance())
                le_sensor_cor()
                segue_linha_sensor_direito_prop(velocidade_robo-20)
            rodas.stop()            
            ev3.speaker.beep()
            largura_tubo = rodas.distance() - largura_tubo
            print('a largura_tubo q ele leu é: ',largura_tubo)

            if largura_tubo < tamanho_tubo - 10:
                print('entrou aqui, vi que {} é menor que {}'.format(largura_tubo,tamanho_tubo - 10))
                pass
            else:
                print('terminei de ler o comeco do tubo')
                rodas.stop()
                if caixa_de_correio == 'azul':
                    rodas.straight(-(fabs(largura_tubo - tamanho_tubo)+20))
                    print('a re q ele vai dar é de: ',-(fabs(largura_tubo - tamanho_tubo)+25))
                if caixa_de_correio == 'vermelho':
                    rodas.straight(-(fabs(largura_tubo - tamanho_tubo)+20))
                if caixa_de_correio == 'amarelo':
                    rodas.straight(-(fabs(largura_tubo - tamanho_tubo)+2))
                rodas.turn(90)
                rodas.straight(40)
                estado_empilhadeira = "cima"
                distancia_que_percorreu = rodas.distance()

                pegou_tubo = pega_tubo()
                if pegou_tubo:
                    sai_da_area_cores()
                    #rodas.turn(75)
                else:
                    print('nao consegui pegar tubo')
                    rodas.reset()
                    desce_empilhadeira()
                    sai_da_area_cores()
                    rodas.turn(-90)
                    rodas.reset()

    rodas.stop()
    setPegouTubo(pegou_tubo)
    print('pegar tubo deu: ',pegou_tubo)

    return pegou_tubo

def verifica_tubo_90(distancia_que_ve_tubo,velocidade_robo,dist_area):
    distancia_terminal = 0
    pegou_tubo = getPegouTubo()
    global estado_empilhadeira
    largura_tubo = 0
    tamanho_tubo = 0

    caixa_de_correio = getCaixaDeCorreio()
    rodas.reset()
    sobe_empilhadeira()
    distancia_que_percorreu = 0


    if caixa_de_correio == 'amarelo':
        tamanho_tubo = 100
    if caixa_de_correio == 'vermelho':
        tamanho_tubo = 150
    if caixa_de_correio == 'azul':
        tamanho_tubo = 200
    
    while distancia_terminal < dist_area:   
        largura_tubo = 0
        distancia_terminal = distancia_que_percorreu + rodas.distance()
        #print('dist terminal é: ',distancia_terminal
        #print(ultrassom_lateral.distance())

        le_sensor_cor()
        if ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX):
            ve_sensor_cor()
            alinha_robo(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX)
            distancia_terminal = 1000

        else:
            if ultrassom_lateral.distance() > distancia_que_ve_tubo:
                distancia_terminal = distancia_que_percorreu + rodas.distance()
                le_sensor_cor()
                segue_linha_sensor_direito_prop(velocidade_robo)

            else: 
                print('cheguei a ler o comeco do tubo')
                ev3.speaker.beep()
                rodas.stop()                
                
                largura_tubo = rodas.distance()
                while ultrassom_lateral.distance() < distancia_que_ve_tubo:
                    le_sensor_cor()
                    segue_linha_sensor_direito_prop(velocidade_robo-20)

                ev3.speaker.beep()
                rodas.stop()            
                largura_tubo = rodas.distance() - largura_tubo
                print('a largura_tubo q ele leu é: ',largura_tubo)



                if  largura_tubo > 30:
                    rodas.reset()
                    vai_cair = False
                    # print('ele vai p frente: ',300-(fabs(largura_tubo - tamanho_tubo)))
                    while rodas.distance() < 300-(fabs(largura_tubo - tamanho_tubo)):
                        # print('dist do robo: ',rodas.distance())
                        le_sensor_cor()
                        if ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX):
                            rodas.stop()
                            distancia_terminal = 1000                         
                            vai_cair = True
                        else:
                            rodas.drive(80,0)
                    if not vai_cair:
                        rodas.straight(-50)
                        rodas.turn(90)
                        rodas.straight(-30)
                        while not ve_cor(PRETO_ESQ_MIN,PRETO_ESQ_MAX,PRETO_DIR_MIN,PRETO_DIR_MAX):
                            le_sensor_cor()
                            rodas.drive(80,0)
                        alinha_robo(PRETO_ESQ_MIN,PRETO_ESQ_MAX,PRETO_DIR_MIN,PRETO_DIR_MAX) 

                        while ultrassom_lateral.distance() > distancia_que_ve_tubo:
                            le_sensor_cor()
                            if ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX):
                                rodas.stop()
                                le_sensor_cor()
                                while not ve_cor(BRANCO_ESQ_MIN, BRANCO_ESQ_MAX, BRANCO_DIR_MIN, BRANCO_DIR_MAX):
                                    le_sensor_cor()
                                    rodas.drive(-80,0)
                                rodas.turn(-90)
                                distancia_terminal = 1000
                            else:
                                rodas.drive(80,0)

                        largura_tubo = rodas.distance()
                        while ultrassom_lateral.distance() < distancia_que_ve_tubo:
                            rodas.drive(80,0)
                        largura_tubo = rodas.distance() - largura_tubo

                        if caixa_de_correio == 'azul':
                            rodas.straight(-(fabs(largura_tubo - tamanho_tubo)+25))
                        if caixa_de_correio == 'vermelho':
                            rodas.straight(-(fabs(largura_tubo - tamanho_tubo)+20))
                        if caixa_de_correio == 'amarelo':
                            rodas.straight(-(fabs(largura_tubo - tamanho_tubo)+2))

                        rodas.turn(90)
                        if pega_tubo():
                            distancia_terminal = 10000
                            rodas.turn(-90)
                            sai_da_area_cores()
                            # while not ve_cor(BRANCO_ESQ_MIN, BRANCO_ESQ_MAX, BRANCO_DIR_MIN, BRANCO_DIR_MAX):
                            #     le_sensor_cor()
                            #     rodas.drive(80,0)
                            # rodas.stop()
                            # alinha_robo(BRANCO_ESQ_MIN, BRANCO_ESQ_MAX, BRANCO_DIR_MIN, BRANCO_DIR_MAX)




    rodas.stop()
 
def volta_pro_comeco_area(distancia):
    tamanho_re = 40
    rodas.straight(-tamanho_re)
    rodas.turn(180)
    rodas.reset()
    while rodas.distance() < distancia-tamanho_re:
        le_sensor_cor()
        if ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX):
            rodas.stop()
            alinha_robo(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX)
            break
        else:
            segue_linha_sensor_esquerdo_prop(120)
    rodas.stop()
    
    rodas.straight(-80)
    rodas.turn(180)


def devolve_tubo():
    ordem_areas = getOrdemAreas()
    ordem_areas = list(reversed(ordem_areas))
    print(ordem_areas)
    tubo_pra_devolver = getTuboPraDevolver()
    print(tubo_pra_devolver)
    distancias_comeco_areas = [0,800,1700]
    distancia = 0
    tamanho_tubo = 0

    cores = ['amarelo','vermelho','azul']
    tamanhos_tubos = [100,150,200]
    for i in range(3):
        if cores[i] == tubo_pra_devolver:
            tamanho_tubo = tamanhos_tubos[i]

    rodas.straight(-40)
    rodas.turn(-90)
    le_sensor_cor()
    while not ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX): 
        le_sensor_cor()
        segue_linha_sensor_direito_prop(100)

    rodas.straight(-80)
    rodas.turn(180)
    

    dist_ultrassom_lateral = ultrassom_lateral.distance()
    while dist_ultrassom_lateral > 40:
        dist_ultrassom_lateral = ultrassom_lateral.distance()
        le_sensor_cor()
        segue_linha_sensor_esquerdo_prop(100)
    ev3.speaker.beep()

    largura_tubo = rodas.distance()
    dist_ultrassom_lateral = ultrassom_lateral.distance()
    while dist_ultrassom_lateral < 40:
        dist_ultrassom_lateral = ultrassom_lateral.distance()
        le_sensor_cor()
        segue_linha_sensor_esquerdo_prop(100)

    largura_tubo = fabs(rodas.distance() - largura_tubo)
    if tubo_pra_devolver == 'azul':
        rodas.straight(-(fabs(largura_tubo - tamanho_tubo)+20))
    if tubo_pra_devolver == 'vermelho':
        rodas.straight(-(fabs(largura_tubo - tamanho_tubo)+20))
    if caixa_de_correio == 'amarelo':
        tubo_pra_devolver.straight(-(fabs(largura_tubo - tamanho_tubo)+2))

    print(ultrassom_lateral.distance())
    
    sobe_empilhadeira()
    rodas.reset()
    rodas.turn(90)
    pega_tubo()

    while not ve_cor(PRETO_ESQ_MIN, PRETO_ESQ_MAX, PRETO_DIR_MIN, PRETO_DIR_MAX):
        le_sensor_cor()
        rodas.drive(-80,0)
    rodas.stop()
    rodas.straight(110)
    rodas.turn(-90)

    distancia = fabs(rodas.distance())

    index = 0
    for i in ordem_areas:
        if i == tubo_pra_devolver:
            index = ordem_areas.index(i)

    distancia = distancias_comeco_areas[index] - distancia
    
    rodas.reset()

    if distancia > 0:
        while rodas.distance() < distancia:
            le_sensor_cor()
            segue_linha_sensor_esquerdo_prop(100)
    rodas.stop()
    rodas.turn(-90)
    rodas.straight(-50)
    desce_empilhadeira()
    rodas.straight(-50)
    sobe_empilhadeira()
    rodas.straight(150)
    rodas.straight(-60)
    

    
    
    



    










    


