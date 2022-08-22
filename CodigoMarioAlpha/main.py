#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import *
import time
from pybricks.nxtdevices import *

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

#Infos: Conectar o cérebro alpha por cabo no pc e o beta por bluetooth
# Conectar eles por bluetooth pelo Alpha



def sobe_empilhadeira():
    MotorEmpilhadeira.run_time(100, tempo_empilhadeira)
    return

def desce_empilhadeira():
    MotorEmpilhadeira.run_time(-100, tempo_empilhadeira)
    return

def pegar_tubo():
    desce_empilhadeira()
    robot.straight(120)
    sobe_empilhadeira()
    robot.straight(-50)
    #desce_empilhadeira()
    #robot.straight(-100)
    #sobe_empilhadeira()

def devolver_tubo():
    #desce_empilhadeira()
    MotorEmpilhadeira.run_time(-100, 200)
    robot.straight(-200)
    MotorEmpilhadeira.run_time(100, 200)
    #sobe_empilhadeira()




# Create your objects here.
ev3 = EV3Brick()

SensorCorDireita = ColorSensor(Port.S1)
SensorCorEsquerda = ColorSensor(Port.S2)
Giroscopio = GyroSensor(Port.S3)
UltrassomFrente = UltrasonicSensor(Port.S4)
RodaEsquerda = Motor(Port.D)
RodaDireita = Motor(Port.A)
MotorEmpilhadeira = Motor(Port.C)
robot = DriveBase(RodaEsquerda, RodaDireita, wheel_diameter=55.5, axle_track=104)

tempo_empilhadeira = 1100

# # Write your program here.
# ev3.speaker.beep()

# server = BluetoothMailboxServer()
# mbox = TextMailbox('greeting', server)

# # The server must be started before the client!
# print('waiting for connection...')
# server.wait_for_connection()
# print('connected!')

# # In this program, the server waits for the client to send the first message
# # and then sends a reply.
# mbox.wait()
# print(mbox.read())
# mbox.send('hello to you!')

sobe_empilhadeira()

while True:
    #print(mbox.read())
    time.sleep(0.5)
    #if (mbox.read() == 'Oi sdds'):
        #ev3.speaker.beep()
        #robot.turn(360)
    distancia = UltrassomFrente.distance()
    print(distancia)
    if distancia < 180:
        pegar_tubo()
        time.sleep(5)
        devolver_tubo()
