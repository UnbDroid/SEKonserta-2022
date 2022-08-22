#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
#from ev3dev.ev3 import *
from ev3dev2.console import *
from time import sleep
import random
import sys
from ev3dev2.sound import Sound


def sobe_empilhadeira():
    MotorEmpilhadeira.on_for_seconds(SpeedPercent(-20), tempo_empilhadeira)
    return

def desce_empilhadeira():
    MotorEmpilhadeira.on_for_seconds(SpeedPercent(20), tempo_empilhadeira)
    return

def abre_ultrassom():
    MotorUltrassom.on_for_seconds(SpeedPercent(15), tempo_ultrassom)
    return

def fecha_ultrassom():
    MotorUltrassom.on_for_seconds(SpeedPercent(-15), tempo_ultrassom*1.1)
    return


def pega_tubo():
        abre_ultrassom()
        tank_drive.on_for_seconds(SpeedPercent(10),SpeedPercent(10), 2.2)
        sobe_empilhadeira()
        time.sleep(3)
        desce_empilhadeira()
        tank_drive.on_for_seconds(SpeedPercent(-10),SpeedPercent(-10), 2.3)
        fecha_ultrassom()
        return


def verifica_tubo():
    tempo = 0.4
    dist_esq = 0
    dist_dir = 0
 
    tank_drive.on_for_seconds(SpeedPercent(10),SpeedPercent(-10), tempo)
    time.sleep(0.3)
    dist_dir = Ultrassom.value()
    print('A distancia na direita é',dist_dir, file=sys.stderr)
    time.sleep(0.3)
    tank_drive.on_for_seconds(SpeedPercent(-10),SpeedPercent(10), tempo*2)
    time.sleep(0.3)
    dist_esq = Ultrassom.value()       
    print('A distancia na esquerda é',dist_esq, file=sys.stderr)
    time.sleep(0.3)
    tank_drive.on_for_seconds(SpeedPercent(10),SpeedPercent(-10), tempo)
    if dist_esq < 67 and dist_dir < 67:
        pega_tubo()
    
    return

# Módulos e suas portas -------------------------------------------------
MotorEmpilhadeira = Motor(OUTPUT_A)
MotorUltrassom = Motor(OUTPUT_B)
tank_drive = MoveTank(OUTPUT_C, OUTPUT_D)  #C - Esquerda    D - Direita

Ultrassom = UltrasonicSensor(INPUT_1)
Giroscopio = GyroSensor(INPUT_2)
coloresquerdo = ColorSensor(INPUT_3)
colordireito = ColorSensor(INPUT_4)

# Valores e Parâmetros ---------------------------------------------------

tempo_empilhadeira = 2.5                    # Tempo necessário para subir/descer a empilhadeira
tempo_ultrassom = 0.44                    # Tempo necessários para abrir/fechar o ultrassom




# Início do código --------------------------------------------------------



while True:
    dist = Ultrassom.value()
    time.sleep(0.3)
    print(dist, file=sys.stderr)
    if dist < 67:
        verifica_tubo()
        #pega_tubo()

