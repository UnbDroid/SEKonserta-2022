from declaracoes import *
from pegaTubo import *

def ajustes_comeco():
    desce_empilhadeira()
    desce_ultrassom()

def ve_borda():
    if luzEsquerda.reflection() < 5 or luzDireita.reflection() < 5:
        rodas.straight(10)    
        if luzEsquerda.reflection() < 5 or luzDireita.reflection() < 5:
            return True
        else:
            return False

    else:
        return False

def desvia_borda():
    rodas.stop()
    rodas.straight(-60)
    rodas.turn(90)

