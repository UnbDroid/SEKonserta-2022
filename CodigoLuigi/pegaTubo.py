from cores import *

viu_borda_pegando_tubo = False
mudou_de_area_pegando_tubo = False

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
    #print(leituras_ultrassom)

    if porcentagem > 0.7:
        viu = True
    return viu


def ve_ultrassom_lateral(num_leituras,quanto_quero_que_leia):
    leituras_ultrassom = []
    leu_certo = []
    viu = False

    for i in range(num_leituras):
        leituras_ultrassom.append(ultrassom_lateral.distance())
    #print(leituras_ultrassom)

    for i in leituras_ultrassom:
        if(i <= quanto_quero_que_leia):
            leu_certo.append(i)

    porcentagem = len(leu_certo)/len(leituras_ultrassom)
    #print('O ULTRASSOM LATERAL LEU')
    #print(leituras_ultrassom)

    if porcentagem > 0.7:
        viu = True

    return viu

def sai_da_area_cores(segue_linha_interno):
    while not ve_cor(PRETO_ESQ_MIN, PRETO_ESQ_MAX, PRETO_DIR_MIN, PRETO_DIR_MAX):
        le_sensor_cor()
        rodas.drive(-80,0)
    #alinha_robo(PRETO_ESQ_MIN, PRETO_ESQ_MAX, PRETO_DIR_MIN, PRETO_DIR_MAX)
    if segue_linha_interno:
        print('entrou aqui')
        rodas.straight(90)
        rodas.turn(-90)
    else:
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
    rodas.straight(-40)
    motorEmpilhadeira.run_time(250,1000)
    rodas.straight(20)
    le_sensor_cor()
    if getCaixaDeCorreio() == 'amarelo': #ir mais pra frente se for um de 10!
        rodas.straight(20)
        rodas.straight(-20)
    while not ve_cor(PRETO_ESQ_MIN,PRETO_ESQ_MAX,PRETO_DIR_MIN,PRETO_DIR_MAX):
        le_sensor_cor()
        rodas.drive(-80,0)
    rodas.stop()
    alinha_preto_re()
    sobe_empilhadeira()
    rodas.straight(125)
    rodas.turn(-90)


    # else:
    #     rodas.straight(-60)
    # sobe_empilhadeira()
    setPegouTubo(False)


def pega_tubo(interno):
    global estado_empilhadeira
    global estado_ultrassom
    global viu_borda_pegando_tubo
    global mudou_de_area_pegando_tubo
    pegou_tubo = getPegouTubo()
    ordem_areas = getOrdemAreas()
    # cores_que_ele_ta_vendo = ['nada','branco']
    

    rodas.straight(-50)
    if estado_empilhadeira == "cima":
        desce_empilhadeira()
    
    while not ve_ultrassom(100,120):
        le_sensor_cor()
        # cores_que_ele_ta_vendo.append(identifica_cor_da_area())
        
        if ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX):
            rodas.reset()
            le_sensor_cor()
            alinha_robo(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX)
            rodas.stop()
            sai_da_area_cores(interno)
            if not interno:
                rodas.turn(-90)
            print('sai da area cores')
            viu_borda_pegando_tubo = True
            break
        # elif getCaixaDeCorreio() not in cores_que_ele_ta_vendo:
        #     rodas.reset()
        #     rodas.turn(-90)
        #     sai_da_area_cores()
        #     print('sai da area cores')
        #     mudou_de_area_pegando_tubo = True
        #     break
        else:
            rodas.drive(80,0)
        # cores_que_ele_ta_vendo = ['nada','branco']
    rodas.stop()

    if not viu_borda_pegando_tubo: #and not mudou_de_area_pegando_tubo:
        rodas.straight(80)
        sobe_empilhadeira()
        estado_empilhadeira = "cima"

        if not ve_ultrassom(200,2000):
            pegou_tubo = True
            rodas.stop()
        else:
            pegou_tubo = False
            
    
    setPegouTubo(pegou_tubo)
    print('printtei o tubo aq',getPegouTubo())
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
            pegou_tubo = pega_tubo(False)
        else:
            rodas.drive(80,0)
  
def sai_do_ponto_inicial_e_vai_pra_area():
    ordem_areas = getOrdemAreas()
    caixa_de_correio = getCaixaDeCorreio()
    distancia = 0
    index = 0
    viu_borda = False
    
    print(ordem_areas)

    #distancias_comeco_areas = [0,750,1500]
    distancias_comeco_areas = [0,633,1470]

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
    else:
        rodas.turn(-15)

def verifica_tubo_reto(distancia_que_ve_tubo,velocidade_robo,dist_area,interno):
    distancia_terminal = 0
    pegou_tubo = getPegouTubo()
    global estado_empilhadeira
    global viu_borda_pegando_tubo
    largura_tubo = 0
    ordem_areas = getOrdemAreas()
    caixa_de_correio = getCaixaDeCorreio()

    if caixa_de_correio == ordem_areas[0]:
        dist_area = dist_area - 130

    rodas.reset()
    caixa_de_correio = getCaixaDeCorreio()
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
            if interno:
                segue_linha_sensor_esquerdo_interno(velocidade_robo)
            else:
                segue_linha_sensor_direito_prop(velocidade_robo)

        else: 
            distancia_terminal = distancia_que_percorreu + rodas.distance()
            print('cheguei a ler o comeco do tubo')
            ev3.speaker.beep()
            rodas.stop()                
            largura_tubo = rodas.distance()

            while ultrassom_lateral.distance() < distancia_que_ve_tubo:
                distancia_terminal = distancia_que_percorreu + rodas.distance()
                #print(ultrassom_lateral.distance())
                le_sensor_cor()
                if ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX):
                    rodas.stop()
                    distancia_terminal = 10000
                else:
                    if interno:
                        segue_linha_sensor_esquerdo_interno(velocidade_robo-20)
                    else:
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
                # rodas.stop()
                if caixa_de_correio == 'azul':
                    rodas.straight(-(fabs(largura_tubo - tamanho_tubo)+55))
                    #print('a re q ele vai dar é de: ',-(fabs(largura_tubo - tamanho_tubo)+25))
                if caixa_de_correio == 'vermelho':
                    rodas.straight(-(fabs(largura_tubo - tamanho_tubo)+25))
                if caixa_de_correio == 'amarelo':
                    rodas.straight(-(fabs(largura_tubo - tamanho_tubo)+2))
                
                
                distancia_que_percorreu = rodas.distance()
                print('dist q percorreu é',distancia_que_percorreu)
                distancia_terminal = distancia_que_percorreu + rodas.distance()
                print('dist terminal é {} e dist q percorreu é {}'.format(distancia_terminal,distancia_que_percorreu))
                
                rodas.reset()
                rodas.turn(90)
                rodas.straight(40)

                pega_tubo(interno)
                if getPegouTubo():
                    sai_da_area_cores(False)
                    break
                    #rodas.turn(75)
                else:
                    rodas.reset()
                    if not viu_borda_pegando_tubo:
                        print('nao consegui pegar tubo')
                        desce_empilhadeira()
                        sai_da_area_cores(interno)
                        sobe_empilhadeira()
                        rodas.turn(-90)
                    rodas.reset()
                    distancia_terminal = distancia_que_percorreu + rodas.distance()
                    #print('depois de não pegar tubo na borda,dist terminal é',distancia_terminal)

    rodas.stop()
    #setPegouTubo(pegou_tubo)
    print('pegar tubo deu: ',getPegouTubo())

    return pegou_tubo

def verifica_tubo_90(distancia_que_ve_tubo,velocidade_robo,dist_area):
    distancia_terminal = 0
    pegou_tubo = getPegouTubo()
    global estado_empilhadeira
    global mudou_de_area_pegando_tubo
    global viu_borda_pegando_tubo
    distancia_que_voltou = 0
    largura_tubo = 0
    tamanho_tubo = 0
    ordem_areas = getOrdemAreas()
    caixa_de_correio = getCaixaDeCorreio()

    if caixa_de_correio == ordem_areas[0]:
        dist_area = dist_area - 130

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
            if not ve_ultrassom_lateral(50,distancia_que_ve_tubo): # > distancia_que_ve_tubo:
                distancia_terminal = distancia_que_percorreu + rodas.distance()
                le_sensor_cor()
                segue_linha_sensor_direito_prop(velocidade_robo)
            else: 
                print('cheguei a ler o comeco do tubo')
                ev3.speaker.beep()
                rodas.stop()  
                rodas.straight(5)              
                
                largura_tubo = rodas.distance()
                while ve_ultrassom_lateral(50,distancia_que_ve_tubo): #ultrassom_lateral.distance() < distancia_que_ve_tubo:
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

                        distancia_que_percorreu = rodas.distance()
                        # print('dist q percorreu é',distancia_que_percorreu)
                        distancia_terminal = distancia_que_percorreu + rodas.distance()
                        # print('dist terminal é {} e dist q percorreu é {}'.format(distancia_terminal,distancia_que_percorreu))
                        
                        rodas.reset()
                        rodas.turn(90)
                        rodas.straight(40)

                        pega_tubo(False)
                        if getPegouTubo():
                            distancia_terminal = 10000
                            rodas.turn(-90)
                            sai_da_area_cores(False)
                        else:
                            distancia_que_voltou = rodas.distance()
                            print('a distancia que voltou foi:',distancia_que_voltou)
                            rodas.reset()
                            if mudou_de_area_pegando_tubo:
                                distancia_terminal = 0
                                rodas.turn(-90)
                            elif not viu_borda_pegando_tubo:
                                print('nao consegui pegar tubo')
                                desce_empilhadeira()
                                distancia_terminal = distancia_que_percorreu + distancia_que_voltou
                                print('dist terminal é',distancia_terminal)
                                rodas.turn(-90)
                                sai_da_area_cores(False)
                                sobe_empilhadeira()
                                rodas.turn(-90)                                
                                # while not ve_cor(BRANCO_ESQ_MIN, BRANCO_ESQ_MAX, BRANCO_DIR_MIN, BRANCO_DIR_MAX):
                                #     le_sensor_cor()
                                #     rodas.drive(80,0)
                                # rodas.stop()
                                # alinha_robo(BRANCO_ESQ_MIN, BRANCO_ESQ_MAX, BRANCO_DIR_MIN, BRANCO_DIR_MAX)
                            #print('dist que percorreu é',distancia_que_percorreu)
                            




    rodas.stop()

def volta_pro_comeco_area(distancia):
    ordem_areas = getOrdemAreas()
    caixa_de_correio = getCaixaDeCorreio()

    if caixa_de_correio == ordem_areas[0]:
        distancia = distancia + 110

    tamanho_re = 60
    rodas.straight(-tamanho_re)
    rodas.turn(180)
    rodas.reset()
    while rodas.distance() < distancia-tamanho_re:
        le_sensor_cor()
        if ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX):
            rodas.stop()
            alinha_robo(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX)
            rodas.stop()    
            rodas.straight(-80)
            break
        else:
            segue_linha_sensor_esquerdo_prop(120)
    rodas.stop()    
    rodas.turn(180)


def devolve_tubo():
    tem_tubo_pra_pegar = True
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

    watch.reset()
    while not ve_ultrassom_lateral(50,40): # dist_ultrassom_lateral > 40:
        if watch.time() > 6000:
           tem_tubo_pra_pegar = False
           rodas.turn(-90)
           break
        else:
            dist_ultrassom_lateral = ultrassom_lateral.distance()
            le_sensor_cor()
            segue_linha_sensor_esquerdo_prop(100)
    ev3.speaker.beep()

    if tem_tubo_pra_pegar:
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
            rodas.straight(-(fabs(largura_tubo - tamanho_tubo)+2))

        print(ultrassom_lateral.distance())
        
        sobe_empilhadeira()
        rodas.reset()
        rodas.turn(90)
        pega_tubo(False)

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
    

    
    
    



    










    


