from declaracoes import *
from pegaTubo import *
from cores import *

def ajustes_comeco():
    desce_empilhadeira()

def desvia_borda():
    rodas.stop()
    rodas.straight(-60)
    rodas.turn(90)

def desvia_rampa():
    rodas.stop()
    rodas.straight(-60)
    rodas.turn(180)


def atitude_borda(): #atitudes que ele deve tomar logo que ve a borda, se alinha e desvia
    rodas.stop()
    alinha_borda()
    desvia_borda()

def atitude_rampa(): #atitudes que ele deve tomar logo que ve a rampa, se alinha e desvia
    rodas.stop()
    alinha_rampa()
    desvia_rampa() 


