#file -- declarações.py --

ev3 = EV3Brick()

SensorCorDireita = ColorSensor(Port.S1)
SensorCorEsquerda = ColorSensor(Port.S2)
Giroscopio = GyroSensor(Port.S3)
UltrassomFrente = UltrasonicSensor(Port.S4)
RodaEsquerda = Motor(Port.D)
RodaDireita = Motor(Port.A)
robot = DriveBase(RodaEsquerda, RodaDireita, wheel_diameter=55.5, axle_track=104)