#!/usr/bin/env pybricks-micropython

from declaracoes import *
from pegatubo import *
from servidor import*
from percorregasoduto import *
from cores import *
from comeco import *
from movimentacao import *


# conecta_alpha_beta()
# percorre_gasoduto_esquerda('ignorar')

# wait(50000)

# ------------------------------------- Código Certo --------------------------------------------
sobe_empilhadeira_centro()
conecta_alpha_beta()
inicio()
percorre_gasoduto_esquerda('medir')
gasoduto_apos_pegar_tubo()
percorre_gasoduto_esquerda('entregar')
percorre_gasoduto_esquerda('medir')
# -----------------------------------Final Código Certo ------------------------------------------------

