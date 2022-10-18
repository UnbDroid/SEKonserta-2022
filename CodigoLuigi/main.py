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
    if getTuboPraDevolver() != 'Nada':
        devolve_tubo()
        vai_pro_ponto_inicial(False)
    while MboxCores.read() =='Nada' or MboxCores.read() == None:
        pass
    setTuboPraDevolver(MboxCoresDevolve.read())
    setCaixaDeCorreio(MboxCores.read())
    print('caixa de correio entrou: ',getCaixaDeCorreio())
    print('mailbox cores devolve depois deu: ',getTuboPraDevolver()) 
    sai_do_ponto_inicial_e_vai_pra_area()

    setPegouTubo(verifica_tubo_reto(35,80,680))
    if not getPegouTubo():
        volta_pro_comeco_area(680)
        setPegouTubo(verifica_tubo_reto(50,80,600))
        if not getPegouTubo():
            volta_pro_comeco_area(680)
            setPegouTubo(verifica_tubo_reto(50,80,600))

    posiciona_tubo_mario()
    MboxConfirmacao.send('Tubo entregue')
    while MboxConfirmacao.read() !='Tubo pego':
        pass
    rodas.straight(100)
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
    setTuboPraDevolver('Nada')
    while True:
        loop_tubo()

# vai_pro_ponto_inicial(True)
# acha_localizacao_das_cores()

# while True:
#     le_sensor_cor()

#sai_da_area_cores()


# while True:
#     le_sensor_cor()


# verifica_tubo_reto(35,80,680)
# if not getPegouTubo():
#     volta_pro_comeco_area(680)
#     verifica_tubo_reto(50,80,600)
#     print('pegar tubo no main deu',getPegouTubo())
#     if not getPegouTubo():
#         volta_pro_comeco_area(680)
#         verifica_tubo_90(50,80,600)
#         print('pegar tubo no main deu',getPegouTubo())    


vai_pro_ponto_inicial(True)
acha_localizacao_das_cores()
sai_do_ponto_inicial_e_vai_pra_area()

# ----------------------------------------------------------------------------------
# cores_teste = ['amarelo','azul','vermelho']
# devolve_teste = ['Nada','azul','amarelo']

# comeco = True
# for i in range(3):
#     setCaixaDeCorreio(cores_teste[i])
#     setTuboPraDevolver(devolve_teste[i])
#     if comeco:
#         vai_pro_ponto_inicial(True)
#         acha_localizacao_das_cores()
#         comeco = False
#     else:
#         vai_pro_ponto_inicial(False)
    
#     if getTuboPraDevolver() == 'Nada':
#         wait(800)
#     else:
#         devolve_tubo()
#         vai_pro_ponto_inicial(False)

#     sai_do_ponto_inicial_e_vai_pra_area()
#     verifica_tubo_reto(35,80,680)
#     print('sai do primeiro pegou_tubo()')
#     if not getPegouTubo():
#         volta_pro_comeco_area(680)
#         verifica_tubo_reto(50,80,600)
#         print('pegar tubo no main deu',getPegouTubo())
#         if not getPegouTubo():
#             volta_pro_comeco_area(680)
#             verifica_tubo_90(50,80,600)
#             print('pegar tubo no main deu',getPegouTubo())    

#     posiciona_tubo_mario()
#     rodas.straight(85)
#     rodas.turn(-90)
#     le_sensor_cor()
#     while not ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX): 
#         le_sensor_cor()
#         segue_linha_sensor_esquerdo_prop(100)
#     atitude(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX,TURN_BORDA)

# ----------------------------------------------------------------------------------------------------    


