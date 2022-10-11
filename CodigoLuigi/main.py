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


def inicio():
    conecta_alpha_luigi()
    vai_pro_ponto_inicial(True)
    acha_localizacao_das_cores()
    print('mailbox deu: ',MboxCores.read())
    while MboxCores.read() =='Nada':
        pass
    setCaixaDeCorreio(MboxCores.read())
    print('mailbox deu: ',MboxCores.read())
    print('caixa de correio entrou: ',getCaixaDeCorreio())
    #caixa_de_correio = getCaixaDeCorreio()
    sai_do_ponto_inicial_e_vai_pra_area()
    verifica_tubo_reto(30,50)
    sai_da_area_cores()
    posiciona_tubo_mario()
    MboxConfirmacao.send('Tubo entregue')
    rodas.straight(-100)


# vai_pro_ponto_inicial(True)
# acha_localizacao_das_cores()
sai_do_ponto_inicial_e_vai_pra_area()
verifica_tubo_reto(30,50)
sai_da_area_cores()
posiciona_tubo_mario()
rodas.turn(-90)
vai_pro_ponto_inicial(False)

# while True:
#     le_sensor_cor()
#     segue_linha_sensor_direito_prop(100)

#sobe_empilhadeira()
# rodas.straight(-400)
# rodas.turn(90)
# rodas.straight(40)
# desce_empilhadeira()
# rodas.straight(-40)


#inicio()
# acha_localizacao_das_cores()
# vai_pro_ponto_inicial(False)
#vai_pro_ponto_inicial(True)
# while True:
#     le_sensor_cor()
#     segue_linha_sensor_esquerdo_prop(100)
#acha_localizacao_das_cores()
#vai_pro_ponto_inicial(False)

#vai_pro_ponto_inicial(True)
#ve_ultrassom(100,250)
#le_sensor_cor()
#descobre_info_area()

# while True:
#     le_sensor_cor()
#     segue_linha_sensor_direito_prop(100)
# #rodas.straight(-30)
# rodas.stop()

# sobe_empilhadeira()
# posiciona_tubo_mario()

#le_sensor_cor()
#identifica_cor_da_area()



#verifica_tubo_reto(35,50)
#desce_empilhadeira()
