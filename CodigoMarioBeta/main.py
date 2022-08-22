#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import *
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import *
from pybricks.nxtdevices import LightSensor
import time



def sobe_empilhadeira():
    MotorEmpilhadeira.run_time(100, tempo_empilhadeira)
    return

def desce_empilhadeira():
    MotorEmpilhadeira.run_time(-100, tempo_empilhadeira)
    return




# Motores e Sensores
ev3 = EV3Brick()
MotorEmpilhadeira = Motor(Port.A)
UltrassomDireita = UltrasonicSensor(Port.S1)
UltrassomEsquerda = UltrasonicSensor(Port.S2)
LuzDireita = LightSensor(Port.S3)
LuzEsquerda = LightSensor(Port.S4)

# Variáveis
tempo_empilhadeira = 1600


# Write your program here.
ev3.speaker.beep()



# This is the name of the remote EV3 or PC we are connecting to.
SERVER = 'ev3dev'

client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)

print('establishing connection...')
client.connect(SERVER)
print('connected!')

# In this program, the client sends the first message and then waits for the
# server to reply.
mbox.send('hello!')
mbox.wait()
print(mbox.read())
mbox.send('Oie')

while True:
    if mbox.read() == 'É menor':
        desce_empilhadeira()

    continue
while True:
    time.sleep(2)
    mbox.send('Oi sdds')
    sobe_empilhadeira()
    time.sleep(2.1)
    desce_empilhadeira()
    print("Sai")