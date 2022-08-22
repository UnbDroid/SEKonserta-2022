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
import rpyc

#bbk sempre à direita, e ele é conectado ao cabo

def sobe_empilhadeira():
    MotorEmpilhadeira.on_for_seconds(SpeedPercent(15), tempo_empilhadeira)
    return

def desce_empilhadeira():
    MotorEmpilhadeira.on_for_seconds(SpeedPercent(-15), tempo_empilhadeira)
    return

conn = rpyc.classic.connect('192.168.0.1')


ev3dev2_motor = conn.modules['ev3dev2.motor']
ev3dev2_sensor = conn.modules['ev3dev2.sensor']
ev3dev2_sensor_lego = conn.modules['ev3dev2.sensor.lego']


#ts = ev3dev2_sensor_lego.TouchSensor(ev3dev2_sensor.INPUT_1)
SensorCorDireita = ColorSensor(INPUT_1)
SensorCorEsquerda = ColorSensor(INPUT_2)
Giroscopio = GyroSensor(INPUT_3)
tank_drive = MoveTank(OUTPUT_D, OUTPUT_A)  # D - Esquerda  ------------- A - direita

MotorEmpilhadeira = ev3dev2_motor.Motor(ev3dev2_motor.OUTPUT_A)
UltrassomDireita = ev3dev2_sensor_lego.UltrasonicSensor(ev3dev2_sensor.INPUT_1)
UltrassomEsquerda = ev3dev2_sensor_lego.UltrasonicSensor(ev3dev2_sensor.INPUT_2)
LuzDireita = ev3dev2_sensor_lego.Sensor(ev3dev2_sensor.INPUT_3)
LuzEsquerda = ev3dev2_sensor_lego.Sensor(ev3dev2_sensor.INPUT_4)

# Variáveis e Parâmetros

tempo_empilhadeira = 0.65


# Início do Programa

#desce_empilhadeira()
MotorEmpilhadeira.on_for_seconds(SpeedPercent(15), 0.3)

while True:
    dist = UltrassomDireita.value()
    if dist < 50:
        tank_drive.on_for_seconds(SpeedPercent(10), SpeedPercent(10), 2)
        sobe_empilhadeira()
        time.sleep(1)
        tank_drive.on_for_seconds(SpeedPercent(5), SpeedPercent(5), 2)
        desce_empilhadeira()
        tank_drive.on_for_seconds(SpeedPercent(-10), SpeedPercent(-10), 3) 