#!/usr/bin/env pybricks-micropython 

from servidor import *
from declaracoes import *
from pegaTubo import *
from andaPista import *
from cores import *



def inicio():
    #comeco()
    desce_empilhadeira()
    procura_tubo()
    #pega_tubo()
    while not pega_tubo():
        if leitura_ultrassom < tubo_esta_perto:
            ev3.speaker.beep()
            pega_tubo()
        else:
            entra_na_area_e_pega_tubo()

    '''#le_sensor_cor()
        if ve_borda():
            atitude_borda()
            #viu_borda = True

        if ve_rampa():
            atitude_rampa()
            
        if ve_preto():
            alinha_preto_frente()##########################
            rodas.straight(30)
            le_sensor_cor()

        elif pegou_tubo:
            rodas.drive(-60,0)
            if ve_preto():
                alinha_preto()
                rodas.turn(180)
                break 
        elif ve_tubo():
            pegou_tubo = pega_tubo()
        else:
            rodas.drive(80,0) #numero > 0, vai pra direita // < 0 

#entra_na_area_e_pega_tubo()]'''
inicio()