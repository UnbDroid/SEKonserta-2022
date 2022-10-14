from pegaTubo import *
from servidor import *

def ajustes_comeco():
    global distancia_chao
    global tubo_esta_perto
    sobe_empilhadeira()
    


def valida_cores_com_ultrassom():
    o_que_ve = 'nada'

    if not ve_ultrassom(100,500):
        #print('entrou aqui')
        o_que_ve = "viu_rampa"
    else:
        o_que_ve = "viu_preto"
    
    return o_que_ve

def desvia(turn):  
    rodas.straight(-70) 
    rodas.turn(turn)

def atitude(eq_min, eq_max, dr_min, dr_max, turn): 
    alinha_robo(eq_min, eq_max, dr_min, dr_max)
    desvia(turn)

def atitude_preto():
    alinha_preto_frente()
    rodas.straight(-60)
    rodas.turn(90)

def desvia_mario():
    if ultrassom.distance() < 20:
        rodas.straight(-60)
        rodas.turn(90)

def identifica_cor_da_area():
    setCores("nada")
    
    if ve_cor(AMARELO_ESQ_MIN, AMARELO_ESQ_MAX, AMARELO_DIR_MIN, AMARELO_DIR_MAX) and getDr(): 
        setCores("amarelo")

    elif ve_cor(VERMELHO_ESQ_MIN, VERMELHO_ESQ_MAX, VERMELHO_DIR_MIN, VERMELHO_DIR_MAX) and getDr():
        setCores("vermelho")

    elif ve_cor(AZUL_ESQ_MIN, AZUL_ESQ_MAX, AZUL_DIR_MIN, AZUL_DIR_MAX) and getDr():
        setCores("azul")

    elif ve_cor(BRANCO_ESQ_MIN, BRANCO_ESQ_MAX, BRANCO_DIR_MIN, BRANCO_DIR_MAX ):
        setCores("branco")
    
    ev3.speaker.beep()
    ev3.speaker.beep()
    print('eu vi a cor',getCores())
    return getCores()

def descobre_info_area():
    rodas.straight(50) #entra na área colorida    
    le_sensor_cor()
    setCores(identifica_cor_da_area())
    rodas.straight(-60)

    return getCores()       


def vai_pro_ponto_inicial(comeco):
    watch.reset()
    global distancia_primeira_cor_do_ponto_inicial
    ordem_areas = getOrdemAreas()

    ajustes_comeco()
    viu_preto = False
    leitura_ultrassom = valida_cores_com_ultrassom()

    while not (viu_preto):
        le_sensor_cor()

        if watch.time() > 5000:
            rodas.turn(90)
            watch.reset()

        if ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX):
            le_sensor_cor()
            atitude(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX, TURN_BORDA)
            watch.reset()
        elif (ve_cor(RAMPA_ESQ_MIN, RAMPA_ESQ_MAX, RAMPA_DIREITO_MIN_, RAMPA_DIREITO_MAX) or ve_cor(PRETO_ESQ_MIN, PRETO_ESQ_MAX, PRETO_DIR_MIN, PRETO_DIR_MAX)):
            rodas.stop()
            print("Ou vi rampa ou vi preto")
            le_sensor_cor()
            leitura_ultrassom = valida_cores_com_ultrassom()
            print(leitura_ultrassom)
            rodas.stop()
            if leitura_ultrassom == "viu_rampa":
                print("Vi rampa")
                le_sensor_cor()
                atitude(RAMPA_ESQ_MIN, RAMPA_ESQ_MAX, RAMPA_DIREITO_MIN_, RAMPA_DIREITO_MAX, TURN_RAMPA)
                watch.reset()
            elif leitura_ultrassom == "viu_preto":
                print("vi preto")
                le_sensor_cor()
                alinha_robo(PRETO_ESQ_MIN,PRETO_ESQ_MAX,PRETO_DIR_MIN,PRETO_DIR_MAX) 
                setCores(descobre_info_area())
                print(getCores())
                if getCores() == "nada":
                    print("primeiro vi preto e percebi rampa")
                    le_sensor_cor()
                    atitude(RAMPA_ESQ_MIN, RAMPA_ESQ_MAX, RAMPA_DIREITO_MIN_, RAMPA_DIREITO_MAX, TURN_RAMPA)
                elif getCores() == "branco":
                    print('vi branco dps de alinhar')
                    rodas.straight(40)
                else:
                    print('primeiro vi preto e validou preto')
                    rodas.reset()
                    viu_preto = True
                    rodas.straight(-40)
                    rodas.turn(75)
                    print('antes de add, ordem ares é: ',ordem_areas)
                    if comeco:
                        ordem_areas.append(getCores())
                        print('depois de add, ordem ares é: ',ordem_areas)
                watch.reset()     
        else:
            rodas.drive(100,0)
    
    print("sai do while vendo preto")

    le_sensor_cor()
    while not ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX):
        #print("não vi borda final") 
        le_sensor_cor()
        segue_linha_sensor_esquerdo_prop(100)

    distancia_primeira_cor_do_ponto_inicial = rodas.distance()

    rodas.stop()

    le_sensor_cor()
    alinha_robo(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX)
    rodas.straight(-80)
    rodas.turn(-90)
    
    while not ve_cor(PRETO_ESQ_MIN,PRETO_ESQ_MAX,PRETO_DIR_MIN,PRETO_DIR_MAX):
        le_sensor_cor()
        rodas.drive(100,0)
    
    le_sensor_cor()
    alinha_robo(PRETO_ESQ_MIN,PRETO_ESQ_MAX,PRETO_DIR_MIN,PRETO_DIR_MAX) 
    rodas.stop()


def muda_de_area(distancia):
    rodas.turn(-75) #vira 90 graus para andar até a area 2
    rodas.reset()
    while rodas.distance() < distancia:
        le_sensor_cor()
        segue_linha_sensor_direito_prop(100) #anda até chegar no meio da area 2
    rodas.turn(90) #vira 90 graus em direcao da area 2

def acha_localizacao_das_cores():
    global distancia_primeira_cor_do_ponto_inicial
    ordem_areas = getOrdemAreas()

    #print(getCores())
    #print(distancia_primeira_cor_do_ponto_inicial)

    cores = ['vermelho','amarelo','azul']

    print('a primeira cor ele achou em: ',distancia_primeira_cor_do_ponto_inicial)
    if distancia_primeira_cor_do_ponto_inicial >= 830: 
        primeira_cor = descobre_info_area()
        #print(primeira_cor)
        if distancia_primeira_cor_do_ponto_inicial >= 1660:
            terceira_cor = ordem_areas[0]
            for i in cores:
                if i != terceira_cor and i != primeira_cor:
                    segunda_cor = i
        else: 
            segunda_cor = ordem_areas[0]
            for i in cores:
                if i != segunda_cor and i != primeira_cor:
                    terceira_cor = i
        ordem_areas = []
        ordem_areas.append(primeira_cor)
        ordem_areas.append(segunda_cor)
        ordem_areas.append(terceira_cor)
    
    else:
        print('ordem areas1 é ',ordem_areas)
        sobe_empilhadeira()
        sai_da_area_cores()
        muda_de_area(distancia = 840)
        ordem_areas.append(descobre_info_area())
        print('ordem areas2 é ',ordem_areas)
        vai_pro_ponto_inicial(False)

        for i in cores:
            if i not in ordem_areas:
                ordem_areas.append(i)
    
    print(ordem_areas)
    return


def calibra_settings():
    while True:
        rodas.turn(360)
        wait(3000)
