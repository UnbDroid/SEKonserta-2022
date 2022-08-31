from declaracoes import *
from servidor import *

def percorre_gasoduto_esquerda():
    while True:
        ValorLuzEsquerda = LuzEsquerda.reflection()
        print(ValorLuzEsquerda)
        MboxAlphaBeta.send(str(ValorLuzEsquerda))
        #MboxAlphaBeta.wait_new()
        ValorUltrassomEsquerda = UltrassomEsquerda.distance()
        MboxAlphaBeta2.send(str(ValorUltrassomEsquerda))
        #MboxAlphaBeta2.wait_new()
        print(ValorUltrassomEsquerda)
