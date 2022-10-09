from declaracoes import *
from cores import *
from pegaTubo import *


def ajustes_comeco():
    global distancia_chao
    global tubo_esta_perto
    desce_empilhadeira()


def valida_cores_com_ultrassom():
    o_que_ve = 'nada'
    leitura_ultrassom = ve_ultrassom(50)

    if leitura_ultrassom > 2000:
        print('entrou aqui')
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

def descobre_info_area():
    global cor_da_area

    le_sensor_cor()

    '''    while not ve_cor(PRETO_ESQ_MIN, PRETO_ESQ_MAX, PRETO_DIR_MIN, PRETO_DIR_MAX):
        le_sensor_cor()
        rodas.drive(80,0)
    alinha_preto_frente()'''

    rodas.straight(40) #entra na área colorida    
    le_sensor_cor()
    cor_da_area = identifica_cor_da_area()
    rodas.straight(-40)
    ev3.speaker.beep()

    return cor_da_area


def vai_pro_ponto_inicial():
    global ValorCorEsquerda
    global ValorCorDireita
    global comeco
    #global cor_da_area
    global ordem_areas
    global distancia_primeira_cor_do_ponto_inicial

    ajustes_comeco()
    viu_preto = False
    leitura_ultrassom = valida_cores_com_ultrassom()

    while not (viu_preto):
        le_sensor_cor() 
        
        if watch.time() > 10000:
            rodas.turn(90)
            watch.reset()

        if ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX):
            atitude(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX, TURN_BORDA)
            watch.reset()

        elif (ve_cor(RAMPA_ESQ_MIN, RAMPA_ESQ_MAX, RAMPA_DIREITO_MIN_, RAMPA_DIREITO_MAX) or ve_cor(PRETO_ESQ_MIN, PRETO_ESQ_MAX, PRETO_DIR_MIN, PRETO_DIR_MAX)):
            le_sensor_cor()
            rodas.stop()
            if comeco:
                leitura_ultrassom = valida_cores_com_ultrassom()
                print(comeco)
            if leitura_ultrassom == "viu_rampa":
                print('vi uma RAMPA')
                atitude(RAMPA_ESQ_MIN, RAMPA_ESQ_MAX, RAMPA_DIREITO_MIN_, RAMPA_DIREITO_MAX, TURN_RAMPA)
                watch.reset()

            elif leitura_ultrassom == "viu_preto":
                print('vi um PRETO')
                rodas.reset()
                viu_preto = True
                alinha_preto_frente() 
                cor_da_area = descobre_info_area()
                ordem_areas.append(cor_da_area)
                watch.reset()
        else:
            rodas.drive(100,0)
    
    rodas.straight(-40)
    rodas.turn(75)

    while not ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX): 
        le_sensor_cor()
        segue_linha_sensor_esquerdo_prop()

    distancia_primeira_cor_do_ponto_inicial = rodas.distance()

    rodas.stop()
    alinha_robo(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX)
    rodas.straight(-80)
    rodas.turn(-90)
    
    while not ve_cor(PRETO_ESQ_MIN,PRETO_ESQ_MAX,PRETO_DIR_MIN,PRETO_DIR_MAX):
        le_sensor_cor()
        rodas.drive(100,0)
    alinha_preto_frente()
    rodas.stop()

    comeco = False
    
    return cor_da_area



def muda_de_area(distancia):
    rodas.turn(-75) #vira 90 graus para andar até a area 2
    rodas.reset()
    while rodas.distance() < distancia:
        segue_linha_sensor_direito_prop() #anda até chegar no meio da area 2
    rodas.turn(90) #vira 90 graus em direcao da area 2

def acha_localizacao_das_cores():
    global ordem_areas
    global distancia_primeira_cor_do_ponto_inicial
    global cor_da_area


    print(ordem_areas)
    print(distancia_primeira_cor_do_ponto_inicial)
    cores = ['vermelho','amarelo','azul']

    
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
        sobe_empilhadeira()
        sai_da_area_cores()
        muda_de_area(distancia = 840)
        ordem_areas.append(descobre_info_area())

        for i in cores:
            if i not in ordem_areas:
                ordem_areas.append(i)
    
    print(ordem_areas)
    return
    



def inicio():
    global pegou_tubo

    while True:
        le_sensor_cor()
        if ve_borda():
            atitude_borda()
            #viu_borda = True

        if ve_rampa():
            atitude_rampa()
            
        if ve_preto():
            alinha_preto()
            rodas.straight(30)
            le_sensor_cor()

        elif pegou_tubo == True:
            rodas.drive(-60,0)
            if ve_preto():
                alinha_preto()
                rodas.turn(180)
                break 
        elif ve_tubo():
            pegou_tubo = pega_tubo()
        else:
            rodas.drive(80,0) #numero > 0, vai pra direita // < 0 



def teste_ultrassom_lateral():
    ultrassom_valores = []
    ultrassom_analise = []
    lista_apoio = []


    while rodas.distance() < 830:
        ultrassom_valores.append(ultrassom_lateral.distance())
        rodas.drive(100,0)


    for i in ultrassom_valores:
        if i < 400:
            lista_apoio.append(i)
        else:
            if len(lista_apoio) > 0:
                ultrassom_analise.append(lista_apoio)
                lista_apoio = []
                
    print(ultrassom_valores)
    print(ultrassom_analise)
