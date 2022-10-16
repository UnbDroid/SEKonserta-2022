#!/usr/bin/env pybricks-micropython 

from declaracoes import *
from pegaTubo import *
from servidor import *
from andaPista import *
from cores import *



#cor_da_area = vai_pro_ponto_inicial()
#acha_localizacao_das_cores()
#vai_pro_ponto_inicial()
#sai_do_ponto_inicial_e_pega_tubo()


# sai_do_ponto_inicial_e_vai_pra_area()
# ev3.speaker.beep()
# verifica_tubo_reto(30,50)
# sai_da_area_cores()
# posiciona_tubo_mario()


# conecta_alpha_luigi()
# while MboxCores.read() =='Nada':
#     pass
# print(MboxCores.read())
# ev3.speaker.beep()


def loop_tubo():
    MboxConfirmacao.send('Nada')
    print('mailbox cores recebe antes deu: ',MboxCores.read())
    print('mailbox cores devolve antes deu: ',MboxCoresDevolve.read()) 
    while MboxCores.read() =='Nada' or MboxCores.read() == None:
        #ev3.speaker.beep()
        #wait(500)
        #devolve_tubo()
        pass
    setCaixaDeCorreio(MboxCores.read())
    setTuboPraDevolver(MboxCoresDevolve.read())
    print('mailbox cores recebe depois deu: ',MboxCores.read())
    print('caixa de correio entrou: ',getCaixaDeCorreio())
    print('mailbox cores devolve depois deu: ',MboxCoresDevolve.read()) 
    sai_do_ponto_inicial_e_vai_pra_area()

    pegou_tubo = verifica_tubo_reto(35,80)
    if not pegou_tubo:
        while not pegou_tubo:
            volta_pro_comeco_area(680)
            pegou_tubo = verifica_tubo_reto(50,80)
    posiciona_tubo_mario()
    MboxConfirmacao.send('Tubo entregue')
    while MboxConfirmacao.read() !='Tubo pego':
        pass
    rodas.straight(70)
    rodas.turn(-90)
    le_sensor_cor()
    while not ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX): 
        le_sensor_cor()
        segue_linha_sensor_esquerdo_prop(100)
    atitude(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX,TURN_BORDA)


def inicio():
    conecta_alpha_luigi()
    vai_pro_ponto_inicial(True)
    acha_localizacao_das_cores()
    while True:
        loop_tubo()





# pegou_tubo = verifica_tubo_reto(35,80)
# if not pegou_tubo:
#     volta_pro_comeco_area(680)
#     pegou_tubo = verifica_tubo_reto(50,80)
#     if not pegou_tubo:
#         volta_pro_comeco_area(680)
#         pegou_tubo = verifica_tubo_90(50,80)

#verifica_tubo_90(45,80)
#posiciona_tubo_mario()

# while True:
#     print(ultrassom_lateral.distance())

# devolve_tubo()
# volta_pro_ponto_inicial(False)
# while True:
#     rodas.turn(360)


# -----------------------------------------------------------------------------------
cores_teste = ['azul','vermelho','amarelo']
devolve_teste = ['Nada','azul','Nada']

comeco = True
for i in range(3):
    setCaixaDeCorreio(cores_teste[i])
    setTuboPraDevolver(devolve_teste[i])
    if comeco:
        vai_pro_ponto_inicial(True)
        acha_localizacao_das_cores()
        comeco = False
    else:
        vai_pro_ponto_inicial(False)
    
    if getTuboPraDevolver() == 'Nada':
        wait(800)
    else:
        devolve_tubo()
        vai_pro_ponto_inicial(False)

    sai_do_ponto_inicial_e_vai_pra_area()
    pegou_tubo = verifica_tubo_reto(35,80)
    if not pegou_tubo:
        volta_pro_comeco_area(680)
        pegou_tubo = verifica_tubo_reto(53,80)   
        if not pegou_tubo:
            volta_pro_comeco_area(680)
            pegou_tubo = verifica_tubo_90(50,80)

    posiciona_tubo_mario()
    rodas.straight(85)
    rodas.turn(-90)
    le_sensor_cor()
    while not ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX): 
        le_sensor_cor()
        segue_linha_sensor_esquerdo_prop(100)
    atitude(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX,TURN_BORDA)

# ----------------------------------------------------------------------------------------------------    


