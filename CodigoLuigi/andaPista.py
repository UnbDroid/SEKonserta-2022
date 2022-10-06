from declaracoes import *
from pegaTubo import *
from cores import *

def desce_empilhadeira():
    global estado_empilhadeira

    motorEmpilhadeira.run_until_stalled(-250,then = Stop.BRAKE)
    motorEmpilhadeira.run_time(250, 800)
    estado_empilhadeira = "baixo"

def ajustes_comeco():
    desce_empilhadeira()

def desvia_borda():
    rodas.stop()
    rodas.straight(-80)
    rodas.turn(-90)

def desvia_rampa():
    rodas.stop()
    rodas.straight(-60)
    rodas.turn(180)

def atitude_borda(): #atitudes que ele deve tomar logo que ve a borda, se alinha e desvia
    alinha_borda()
    desvia_borda()

def atitude_rampa(): #atitudes que ele deve tomar logo que ve a rampa, se alinha e desvia
    alinha_rampa()
    desvia_rampa() 

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

    while not (viu_preto and viu_borda):
        le_sensor_cor()
        if ve_preto():
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

        #identifica a cor e seta como zero. Se puder virar p esquerda, vira e conta a distância, se não, vira p direita e conta a distância. Assim ele vai conseguir identificar as 3 cores

def descobre_info_area():
    global cor_da_area

    le_sensor_cor()
    while ve_branco():
        le_sensor_cor()
        rodas.drive(80,0)

    rodas.straight(40)
    
    le_sensor_cor()
    cor_da_area = identifica_cor_da_area()
    print(cor_da_area)

    return cor_da_area

def muda_de_area_para_localizacao():
    rodas.straight(-80) #sai da area 1
    rodas.turn(-90) #vira 90 graus para andar até a area 2
    rodas.straight(830) #anda até chegar no meio da area 2
    rodas.turn(90) #vira 90 graus em direcao da area 2

def acha_localizacao_das_cores():
    global info_area_1
    global info_area_2
    global info_area_3

    info_area_1.append(descobre_info_area())
    print(info_area_1)
    muda_de_area_para_localizacao()
    info_area_2.append(descobre_info_area())
    print(info_area_2)
    muda_de_area_para_localizacao()
    info_area_3.append(descobre_info_area())
    print(info_area_3)

    return
    

    



    






