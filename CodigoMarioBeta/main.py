#!/usr/bin/env pybricks-micropython

from declaracoes import *
from servidor import *
from percorregasoduto import *

conecta_alpha_beta()
while not (MboxAlphaBeta.read() == "PercorrimentoGasodutoEsquerda"):
    print(MboxAlphaBeta.read())
percorre_gasoduto_esquerda()

# while True:
#     wait(100)
#     print('A ambient é:', LuzEsquerda.ambient(), 'Já a reflection é:', LuzEsquerda.reflection())