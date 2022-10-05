#!/usr/bin/env pybricks-micropython

from declaracoes import *
from pegatubo import *
from servidor import*
from percorregasoduto import *
from cores import *
from comeco import *
from movimentacao import *

#
# while True:
#     wait(3000)
#     abre_garra(20)
#     ev3.speaker.beep(400,3000)
#     #wait(3000)
#     fecha_garra(20)
#fecha_garra(0.3)

    
#sobe_empilhadeira_centro()
# conecta_alpha_beta()
# percorre_gasoduto_esquerda('entregar')
#fecha_garra()

# abre_garra(15)
# wait(5000)
# fecha_garra(15)
# ev3.speaker.beep()
#fecha_garra(10)
# ------------------------------------- Código Certo --------------------------------------------
sobe_empilhadeira_centro()
conecta_alpha_beta()
inicio()
while not FIM_DO_PROGRAMA:
    percorre_gasoduto_esquerda('medir')
    gasoduto_apos_pegar_tubo()
    percorre_gasoduto_esquerda('entregar')
# -----------------------------------Final Código Certo ------------------------------------------------

