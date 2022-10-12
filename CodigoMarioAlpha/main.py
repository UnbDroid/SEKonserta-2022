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



# ------------------------------------- Código Certo -> Voltando pegar o tubo após ler o primeiro GAP --------------------------------------------
modo_do_programa = "SemVarreduraCompleta"
#sobe_empilhadeira_centro(True, True) #Usando o centro
#fecha_garra(20)
#abre_garra()
#conecta_nos_dois()
conecta_alpha_beta()
manda_nada_luigi()
#inicio()
print('oi')
manda_nada_luigi()
while not fim_programa():
    if precisa_medir(): #Só não precisa medir se já souber um tamanho que está faltando, que é quando ele passou por gap de tamanho diferente já com um tubo na garra
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