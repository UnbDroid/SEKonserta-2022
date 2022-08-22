#!/usr/bin/env pybricks-micropython
#file -- use_declarações.py --
import declarações
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




# Create your objects here.
ev3 = EV3Brick()

SensorCorDireita = ColorSensor(Port.S1)
SensorCorEsquerda = ColorSensor(Port.S2)
Giroscopio = GyroSensor(Port.S3)
UltrassomFrente = UltrasonicSensor(Port.S4)
RodaEsquerda = Motor(Port.D)
RodaDireita = Motor(Port.A)
robot = DriveBase(RodaEsquerda, RodaDireita, wheel_diameter=55.5, axle_track=104)

# Write your program here.
ev3.speaker.beep()

server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

# The server must be started before the client!
print('waiting for connection...')
server.wait_for_connection()
print('connected!')

# In this program, the server waits for the client to send the first message
# and then sends a reply.
mbox.wait()
print(mbox.read())
mbox.send('hello to you!')

while True:
    print(mbox.read())
    time.sleep(2.1)
    if (mbox.read() == 'Oi sdds'):
        ev3.speaker.beep()
        #robot.turn(360)

