#!/usr/bin/env pybricks-micropython

from declaracoes import *
from pegatubo import *
from servidor import*
from percorregasoduto import *
from cores import *
from comeco import *
from movimentacao import *


# abre_garra(20)
# ev3.speaker.beep(400)
# wait(1000)
# fecha_garra(20)

# ------------------------------------- Código Certo --------------------------------------------
sobe_empilhadeira_centro()
conecta_alpha_beta()
inicio()
percorre_gasoduto_esquerda('medir')
gasoduto_apos_pegar_tubo()
percorre_gasoduto_esquerda('entregar')
percorre_gasoduto_esquerda('medir')
# -----------------------------------Final Código Certo ------------------------------------------------

