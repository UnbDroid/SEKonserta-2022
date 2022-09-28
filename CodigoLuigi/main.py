#!/usr/bin/env pybricks-micropython 

from declaracoes import *
from pegaTubo import *
from servidor import *
from andaPista import *


def inicio():
    global pegou_tubo

    ajustes_comeco()

    while True:
        print(pegou_tubo)
        if ve_borda():
            desvia_borda()
        elif pegou_tubo == True:
            break
        elif ve_tubo():
            radar_tubo()
            if valida_se_esta_vendo_tubo():
                pegou_tubo = pega_tubo()
        else:
            rodas.drive(80,0) #numero > 0, vai pra direita // < 0 

