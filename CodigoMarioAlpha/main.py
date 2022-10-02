#!/usr/bin/env pybricks-micropython

from declaracoes import *
from pegatubo import *
from servidor import*
from percorregasoduto import *
from cores import *
from comeco import *

#Azul Esquerda = 2 - 3  -- Direita 3
# Precipicio Esquerda 0 - 1 Direita 0 - 1
#Verde Esquerda 2 - Direita 1   #5 esquerda e 4 sensor colando na rampa
#Branco Esquerda 43 - Direita 31
#Preto Esquerda 5 e direita 4
#Saindo do branco pro verde, ele lê 2 e 1

# def teste():
#     global ValorCorEsquerda
#     global ValorCorDireita
#     while True:
#         le_sensor_cor()
#         #ValorCorEsquerda = SensorCorEsquerda.reflection()
#         #ValorCorDireita = SensorCorDireita.reflection()
#         print("Valor na Esquerda é:", ValorCorEsquerda, "E na direita é", ValorCorDireita)



#teste2()
conecta_alpha_beta()
inicio()
#percorre_gasoduto_esquerda()
#sobe_empilhadeira(0.15)
#desce_empilhadeira(0.5)
# while True:
#     ValorCorEsquerda = SensorCorEsquerda.reflection()
#     ValorCorDireita = SensorCorDireita.reflection()
#     print("Valor na Esquerda é:", ValorCorEsquerda, "E na direita é", ValorCorDireita)

# robot.drive(-100,0)
#abre_garra()
#sobe_empilhadeira(0.3)
#desce_empilhadeira(0.1)
#wait(3000)
#sobe_empilhadeira()
#wait(5000)
#desce_empilhadeira()
#abre_garra()
#ev3.speaker.beep()
#wait(3000)
#fecha_garra()
# while True:
#     robot.drive(100,0)
#     ValorCorEsquerda = SensorCorEsquerda.reflection()
#     ValorCorDireita = SensorCorDireita.reflection()
#     print("Valor na Esquerda é:", ValorCorEsquerda, "E na direita é", ValorCorDireita)
#     if (ValorCorEsquerda < 15 or ValorCorDireita < 10):
#         robot.stop()
#sobe_empilhadeira(0.2)
#conecta_alpha_beta()
#conecta_alpha_luigi()

# while True:
#     ev3.speaker.say('CRISTIANOOOOOOOO')
#     wait(1000)

# while True:
#     sobe_empilhadeira()
#     wait(5000)
#     desce_empilhadeira()
#     wait(4000)

#fecha_garra(0.2)
#desce_empilhadeira()
#sobe_empilhadeira(0.6)
# while True:
#     abre_garra()
#     sobe_empilhadeira()
#     fecha_garra()
#     desce_empilhadeira()

#conecta_alpha_beta()
# sobe_empilhadeira()
# desce_empilhadeira()
# #fecha_garra()
# abre_garra()
# fecha_garra()

#ev3.speaker.say('CRISTIANOOOOOOOO')

# sobe_empilhadeira(0.5)
#percorre_gasoduto_esquerda()



# Giroscopio.reset_angle(0)
# while True:
#     fator = (0 - Giroscopio.angle())*3
#     print(fator)
#     robot.drive(220,fator)

# sobe_empilhadeira(0.1)
#while True:
#    robot.drive(-100,0)
#fecha_garra()
#pega2(15)
#pega2(15)
#pega2(20)
#sobe_empilhadeira(0.1)
#pega2(15)
#sobe_empilhadeira(0.1)
#pega2(10)
