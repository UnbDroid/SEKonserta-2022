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
    print('mailbox antes deu: ',MboxCores.read())
    while MboxCores.read() =='Nada' or MboxCores.read() == None:
        pass
    setCaixaDeCorreio(MboxCores.read())
    print('mailbox depois deu: ',MboxCores.read())
    print('caixa de correio entrou: ',getCaixaDeCorreio())
    sai_do_ponto_inicial_e_vai_pra_area()
    verifica_tubo_reto(30,80)
    sai_da_area_cores()
    posiciona_tubo_mario()
    MboxConfirmacao.send('Tubo entregue')
    while MboxConfirmacao.read() !='Tubo pego':
        pass
    rodas.straight(100)
    rodas.turn(-90)
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


# if not verifica_tubo_reto(30,80):
#     acha_tubo_re(60,80)



# vai_pro_ponto_inicial(True)
# acha_localizacao_das_cores()
# sai_do_ponto_inicial_e_vai_pra_area()
# if not verifica_tubo_reto(30,80):
#     acha_tubo_re(60,80)
# sai_da_area_cores()
# posiciona_tubo_mario()\

# vai_pro_ponto_inicial(True)
# acha_localizacao_das_cores()

# if not verifica_tubo_reto(30,80):
#     acha_tubo_re(60,80)

verifica_tubo_reto(30,80)

#acha_tubo_re(60,80)

# while True:
#     le_sensor_cor()


# if not verifica_tubo_reto(30,80):
#     acha_tubo_re(60,80)

# desce_empilhadeira()
# while True:
#     frente_ultrassom()
#     lado_ultrassom()
    
    
# while True:
#     rodaEsquerda.run(-100)
#     rodaDireita.run(-100)
#     rodaEsquerda.control.pid()
#     rodaDireita.control.pid()

#rodas.straight(-950)


# if not verifica_tubo_reto(30,80):
#     acha_tubo_re(60,80)



#abre_ultrassom()
#
# while True:
#     print(ultrassom_lateral.distance())

# while rodas.distance() < 830:
#     print(ultrassom_lateral.distance())
#     le_sensor_cor()
#     segue_linha_sensor_direito_prop(80)

#verifica_tubo_reto(30,80)

#inicio()

#rodas.turn(-90)
#vai_pro_ponto_inicial(True)
#acha_localizacao_das_cores()
#sai_do_ponto_inicial_e_vai_pra_area()

# vai_pro_ponto_inicial(False)
# acha_localizacao_das_cores()
# sai_do_ponto_inicial_e_vai_pra_area()
# verifica_tubo_reto(30,50)
# sai_da_area_cores()
# posiciona_tubo_mario()
    
#descobre_info_area()
#rodas.straight(833)
# vai_pro_ponto_inicial(False)
# rodas.straight(-40)
# rodas.turn(-75)
# verifica_tubo_reto(30,50)
# rodas.straight(-60)
# rodas.turn(75)
# vai_pro_ponto_inicial(False)

#vai_pro_ponto_inicial(False)
# rodas.straight(-40)
# while True:
#     le_sensor_cor()
#     alinha_robo(PRETO_ESQ_MIN,PRETO_ESQ_MAX,PRETO_DIR_MIN,PRETO_DIR_MAX) 

#verifica_tubo_reto(30,50)
# while True:
#     #print('e:{} d:{}'.format(luzEsquerda.reflection(),luzDireita.reflection()))
#     if luzEsquerda.reflection() > 10:
#         while luzEsquerda.reflection() > 10:
#             rodaEsquerda.run(200)
#         rodaEsquerda.stop()
#     elif luzDireita.reflection() > 10:
#         while luzDireita.reflection() > 10:
#             rodaDireita.run(200)
#         rodaDireita.stop()
