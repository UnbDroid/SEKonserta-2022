#!/usr/bin/env pybricks-micropython 

from declaracoes import *
from pegaTubo import *
from servidor import *
from andaPista import *
from cores import *


def inicio():
    global pegou_tubo

    ajustes_comeco()
    while True:
        le_sensor_cor()
        if ve_borda():
            atitude_borda()
            #viu_borda = True

        if ve_rampa():
            atitude_rampa()
            
        if ve_preto():
            alinha_preto()
            rodas.straight(30)
            le_sensor_cor()
            print(qual_cor_ve())

        elif pegou_tubo == True:
            rodas.drive(-60,0)
            if ve_preto():
                alinha_preto()
                rodas.turn(180)
                break 
        elif ve_tubo():
            pegou_tubo = pega_tubo()
        else:
            rodas.drive(80,0) #numero > 0, vai pra direita // < 0 



inicio()

'''elif ve_tubo():
            alinhado_ao_tubo = verifica_alinhado_ao_tubo()
            radar
            if alinhado_ao_tubo():
                pegou_tubo = pega_tubo()'''

'''
while True:
    le_sensor_cor()
    if ve_rampa():
        rodas.stop()
        alinha_rampa()
        desvia_rampa()
    else:
        rodas.drive(80,0)'''

