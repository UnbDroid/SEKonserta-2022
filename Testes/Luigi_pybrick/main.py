#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
motor_esq = Motor(Port.D)
motor_dir = Motor(Port.C)
sensor_cor_esq = ColorSensor(Port.S3)
giroscopio = GyroSensor(Port.S2)

# Write your program here.

print(giroscopio.angle())

rodas = DriveBase(motor_esq, motor_dir, wheel_diameter= 40, axle_track=110)
rodas.settings(100, 300)
print(giroscopio.angle())
rodas.straight(100)
print(giroscopio.angle())
rodas.turn(90)
print(giroscopio.angle())
giroscopio.reset_angle(0)
print(giroscopio.angle())

while giroscopio.angle() > -180:
    motor_esq.run(100)

'''motor_esq.run_time(100,10000)
motor_dir.run_time(100,10000)'''