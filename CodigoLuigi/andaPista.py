from declaracoes import *
from cores import *
from pegaTubo import *


def ajustes_comeco():
    global distancia_chao
    global tubo_esta_perto
    desce_empilhadeira()

    '''le_ultrassom()
    distancia_chao,tubo_esta_perto = define_dist_chao_e_tubo()
    print(distancia_chao, tubo_esta_perto)
    return'''

def valida_cores_com_ultrassom():
    global distancia_chao
    o_que_ve = 'nada'

    leitura_ultrassom = ultrassom.distance()
    print('a leitura é: ',leitura_ultrassom)
    if leitura_ultrassom >= distancia_chao+10:
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
    while not ve_cor(PRETO_ESQ_MIN, PRETO_ESQ_MAX, PRETO_DIR_MIN, PRETO_DIR_MAX):
        le_sensor_cor()
        rodas.drive(80,0)
    alinha_preto_frente()

    rodas.straight(40) #entra na área colorida    
    le_sensor_cor()
    cor_da_area = identifica_cor_da_area()

    return cor_da_area

def segue_linha_sensor_esquerdo_tres_cores():
    global ValorCorEsquerda
    global PRETO_ESQ_MIN
    global PRETO_ESQ_MAX
    
    viu_preto = 0

    le_sensor_cor()
    for i in range(3):
        if ValorCorEsquerda[i] > PRETO_ESQ_MIN[i] and ValorCorEsquerda[i] < PRETO_ESQ_MAX[i] :
            viu_preto += 1
    
    if viu_preto == 3:
        rodas.drive(30,30)
    else:
        rodas.drive(30,-30)
    viu_preto = 0

def segue_linha_sensor_esquerdo_prop():
    PRETO = 8
    
    threshold = 50
    PROPORTIONAL_GAIN = 1.5
    DRIVE_SPEED = 100

    leitura_sensor = luzEsquerda.reflection()
    print(leitura_sensor)
    
    deviation =  threshold - leitura_sensor 
    turn_rate = PROPORTIONAL_GAIN * deviation
    rodas.drive(DRIVE_SPEED, turn_rate)

def vai_pro_ponto_inicial():
    global ValorCorEsquerda
    global ValorCorDireita
    global cor_da_area

    viu_preto = False
    viu_borda = False

    o_que_ele_andou_vendo = []
    leitura_ultrassom = valida_cores_com_ultrassom()


    while not (viu_preto and viu_borda):
        le_sensor_cor() 
        leitura_ultrassom = valida_cores_com_ultrassom()
        
        if watch.time() > 5000:
            print('entrou aq')
            rodas.turn(90)
            watch.reset()

        if ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX): 
            viu_borda = True
            o_que_ele_andou_vendo.append("viu_borda")
            atitude(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX, TURN_BORDA)
            watch.reset()

        elif (ve_cor(RAMPA_ESQ_MIN, RAMPA_ESQ_MAX, RAMPA_DIREITO_MIN_, RAMPA_DIREITO_MAX) or ve_cor(PRETO_ESQ_MIN, PRETO_ESQ_MAX, PRETO_DIR_MIN, PRETO_DIR_MAX)):
            print('vi uma BORDA')
            le_sensor_cor()
            if leitura_ultrassom == "viu_rampa":
                atitude(RAMPA_ESQ_MIN, RAMPA_ESQ_MAX, RAMPA_DIREITO_MIN_, RAMPA_DIREITO_MAX, TURN_RAMPA)
                watch.reset()

            elif leitura_ultrassom == "viu_preto":
                cor_da_area = descobre_info_area()
                viu_preto = True
                o_que_ele_andou_vendo.append("viu_preto")
                alinha_preto_frente() 
                atitude_preto()
                watch.reset()
        else:
            rodas.drive(100,0)
    
    if o_que_ele_andou_vendo[-1] == "viu_preto":
        rodas.turn(-25)
        while luzEsquerda.reflection() < 60:
            rodas.drive(50,0)
        rodas.stop()

        while not ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX): 
            le_sensor_cor()
            segue_linha_sensor_esquerdo_prop()
        rodas.stop()
        alinha_robo(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX)
        rodas.straight(-60)
        rodas.turn(-90)
    
    while not ve_cor(PRETO_ESQ_MIN,PRETO_ESQ_MAX,PRETO_DIR_MIN,PRETO_DIR_MAX):
        le_sensor_cor()
        rodas.drive(100,0)

    alinha_preto_frente()
    rodas.stop()




def sai_da_area_cores():
    while not ve_cor(PRETO_ESQ_MIN, PRETO_ESQ_MAX, PRETO_DIR_MIN, PRETO_DIR_MAX):
        le_sensor_cor()
        rodas.drive(-80,0) #sai da area 1
    alinha_preto_re()
    rodas.straight(-40)


def muda_de_area_para_localizacao():
    rodas.turn(-90) #vira 90 graus para andar até a area 2
    rodas.straight(840) #anda até chegar no meio da area 2
    rodas.turn(90) #vira 90 graus em direcao da area 2

def acha_localizacao_das_cores():
    global ordem_areas
    cores = ['vermelho','amarelo','azul']

    sobe_empilhadeira()
    ordem_areas.append(descobre_info_area())

    sai_da_area_cores()
    muda_de_area_para_localizacao()

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
