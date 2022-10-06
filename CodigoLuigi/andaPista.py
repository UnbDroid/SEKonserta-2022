from declaracoes import *
from cores import *
from pegaTubo import *


def ajustes_comeco():
    global distancia_chao
    global tubo_esta_perto

    desce_empilhadeira()

    le_ultrassom()
    distancia_chao,tubo_esta_perto = define_dist_chao_e_tubo()
    #print(distancia_chao, tubo_esta_perto)
    return

def valida_se_viu_preto():
    global leitura_ultrassom
    global distancia_chao
    
    le_ultrassom()
    if leitura_ultrassom <= distancia_chao:
        

def desvia(turn):  
    rodas.stop()
    rodas.straight(-60) 
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

def vai_pro_ponto_inicial():
    global ValorCorEsquerda
    global ValorCorDireita

    viu_preto = False
    viu_borda = False
    o_que_ele_andou_vendo = []
    ajustes_comeco()

    while viu_preto == False:
        desvia_mario() 
        le_sensor_cor() 
        
        if ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX): 
            atitude(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX, TURN_BORDA)

        elif ve_cor(RAMPA_ESQ_MIN, RAMPA_ESQ_MAX, RAMPA_DIREITO_MIN_, RAMPA_DIREITO_MAX):
            atitude(RAMPA_ESQ_MIN, RAMPA_ESQ_MAX, RAMPA_DIREITO_MIN_, RAMPA_DIREITO_MAX, TURN_RAMPA)

        elif ve_cor(PRETO_ESQ_MIN, PRETO_ESQ_MAX, PRETO_DIR_MIN, PRETO_DIR_MAX):

            alinha_preto_frente() 
            viu_preto = True
            o_que_ele_andou_vendo.append("viu_preto")
            atitude_preto()

        elif ve_borda():
            viu_borda = True
            atitude_borda()
            o_que_ele_andou_vendo.append("viu_borda")
        
        elif ve_rampa():
            atitude_rampa()
        else:
            rodas.drive(130,0)
    
    if o_que_ele_andou_vendo[-1] == "viu_preto":
        while not ve_borda():
            le_sensor_cor()
            if ve_preto(): #como a função ve preto retorna true caso ele veja com apenas um dos sensores, é o que eu quero
                rodas.turn(5) 
            rodas.drive(130,0)

        rodas.stop()
        rodas.straight(-60)
        rodas.turn(-90)
    
    '''rodas.drive(80,0) 
    rodas.stop()
    rodas.straight(40) 
'''
        



def descobre_info_area():
    global cor_da_area

    le_sensor_cor()
    while not ve_preto():
        le_sensor_cor()
        rodas.drive(80,0)
    alinha_preto_frente()

    rodas.straight(40) #entra na área colorida    
    le_sensor_cor()
    cor_da_area = identifica_cor_da_area()
    print(cor_da_area)

    return cor_da_area

def muda_de_area_para_localizacao():
    while not ve_preto():
        le_sensor_cor()
        rodas.drive(-80,0) #sai da area 1
    alinha_preto_re()
    rodas.straight(-40)


    rodas.turn(-90) #vira 90 graus para andar até a area 2
    rodas.straight(830) #anda até chegar no meio da area 2
    rodas.turn(90) #vira 90 graus em direcao da area 2

def acha_localizacao_das_cores():
    global ordem_areas
    cores = ['vemelho','amarelo','azul']

    sobe_empilhadeira()
    ordem_areas.append(descobre_info_area())
    muda_de_area_para_localizacao()
    ordem_areas.append(descobre_info_area())
    
    for i in cores:
        if i not in ordem_areas:
            ordem_areas.append(i)
    
    print(ordem_areas)
    return
    
