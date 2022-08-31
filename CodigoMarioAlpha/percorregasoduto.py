from declaracoes import *
from servidor import *



def percorre_gasoduto_esquerda():
    while True:
        MboxAlphaBeta.wait()
        ValorLuzEsquerda = MboxAlphaBeta.read()                                                                            
        MboxAlphaBeta2.wait()
        DistanciaUltrassomEsquerda = MboxAlphaBeta2.read()
        DistanciaUltrassomFrente = UltrassomFrente.distance()
        print('Luz Esq',ValorLuzEsquerda, 'Ult Esq', DistanciaUltrassomEsquerda, 'ult frente', DistanciaUltrassomFrente)
        if int(ValorLuzEsquerda) <= 65:
            robot.drive(30, -15)
        else:
            robot.drive(30,0)
        