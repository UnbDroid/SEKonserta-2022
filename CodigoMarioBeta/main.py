#!/usr/bin/env pybricks-micropython

from declaracoes import *
from servidor import *
from percorregasoduto import *



conecta_alpha_beta()
while not (MboxAlphaBeta.read() == "PercorrimentoGasodutoEsquerda"):
    print(MboxAlphaBeta.read())
percorre_gasoduto_esquerda()



while True:
    wait(200)
    print('A ambient é:', LuzEsquerda.ambient(), 'Já a reflection é:', LuzEsquerda.reflection())#, 'Toque:',SensorToque.pressed())
    # print("a distancia é", UltrassomEsquerda.distance())