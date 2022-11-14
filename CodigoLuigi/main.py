#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import *



ev3 = EV3Brick()
motor_esq = Motor(Port.D)
motor_dir = Motor(Port.C)
sensor_cor_esq = ColorSensor(Port.S3)
giroscopio = GyroSensor(Port.S2)
rodas = DriveBase(motor_esq, motor_dir, wheel_diameter= 40, axle_track=110)
#ultrassom = UltrasonicSensor(Port.S1)
MotorUltrassom = Motor(Port.B)


client = BluetoothMailboxClient()
MboxAlphaLuigi = TextMailbox('alphaluigi', client)

def conecta_alpha_luigi():
    # This is the name of the remote EV3 or PC we are connecting to.
    SERVER = 'ev3dev'


    print('establishing connection...')
    client.connect(SERVER)
    print('connected!')

        # In this program, the client sends the first message and then waits for the
        # server to reply.
    MboxAlphaLuigi.send('hello!')
    MboxAlphaLuigi.wait()
    print(MboxAlphaLuigi.read())