#!/usr/bin/env pybricks-micropython

from declaracoes import *
from pegatubo import *
from servidor import*
from percorregasoduto import *
from cores import *
from comeco import *
from movimentacao import *

FIM_DO_PROGRAMA = False
TUBO_ENTREGUE = False

#sobe_empilhadeira()
#abre_garra()
busca_tubo_em_cima(15)



while True:
    pass

conecta_alpha_beta()
percorre_gasoduto_esquerda()

#fecha_garra(10)
# ------------------------------------- Código Certo -> Voltando pegar o tubo após ler o primeiro GAP --------------------------------------------
#fecha_garra()
modo_do_programa = "SemVarreduraCompleta"
#sobe_empilhadeira_centro()
conecta_alpha_beta()
#inicio()
while not fim_programa():
    percorre_gasoduto_esquerda('medir')
    if fim_programa():
        break
    gasoduto_apos_pegar_tubo()
    print('entrei pra entregar')
    while not tubo_foi_entregue():   # ele continuar entregando, caso ele tenha q devolver 
        percorre_gasoduto_esquerda('entregar')
# -----------------------------------Final Código Certo ------------------------------------------------

while True: #Fica apitando infinitamente quando acaba o programa
    ev3.speaker.beep(1100,500)
    wait(400)



# #----------------------------------- Código fazendo varredura inicial no começo -------------------------- #

# modo_do_programa = 'ComVarreduraCompleta'
# sobe_empilhadeira_centro()
# conecta_alpha_beta()
# inicio()
# while not FIM_DO_PROGRAMA:
#     percorre_gasoduto_esquerda('ignorar')
#     if FIM_DO_PROGRAMA:
#         break
#     gasoduto_apos_pegar_tubo()
#     percorre_gasoduto_esquerda('entregar')

# #-------------------------------------- Final Código ----------------------------------------------------- #