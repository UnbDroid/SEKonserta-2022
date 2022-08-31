#!/usr/bin/env pybricks-micropython

from declaracoes import *
from pegatubo import *
from servidor import*
from percorregasoduto import *


conecta_alpha_beta()
sobe_empilhadeira()
abre_garra()

percorre_gasoduto_esquerda()

while True:
    pega()
