from declaracoes import *
from servidor import *


def calibra_sensor_luz():
    contador = 0
    tempo = 20
    #ev3.speaker.say('Calibrando fora do gasoduto')
    ev3.speaker.beep()
    watch.reset()
    somador = 0
    while watch.time() < tempo:
        contador += 1
        ValorLuzEsquerda = LuzEsquerda.reflection()
        somador = ((somador*(contador - 1)) + ValorLuzEsquerda)/contador

    print(somador)
    valor_minimo = somador
    MboxAlphaBetaLuz.send(valor_minimo)
    ev3.speaker.beep()
    wait(2000)
    ev3.speaker.beep()
    #ev3.speaker.say('Calibrando na parede do gasoduto')
    watch.reset()
    somador = 0
    contador = 0
    while watch.time() < tempo:
        contador += 1
        ValorLuzEsquerda = LuzEsquerda.reflection()
        somador = ((somador*(contador - 1)) + ValorLuzEsquerda)/contador

    print(somador)
    ev3.speaker.beep()
    valor_maximo = somador
    MboxAlphaBetaLuz.send(valor_maximo)
    wait(1000)



def percorre_gasoduto_esquerda():
    calibra_sensor_luz()
    while True:
        wait(100)
        ValorLuzEsquerda = LuzEsquerda.ambient() # Usar quando está claro (De dia e fora da sala)
        #ValorLuzEsquerda = LuzEsquerda.reflection() #Usar quando está escuro (Dentro da sala ou de noite)
        MboxAlphaBetaLuz.send(ValorLuzEsquerda)
        #ValorUltrassomEsquerda = UltrassomEsquerda.distance()
        #MboxAlphaBetaUltrassom.send(ValorUltrassomEsquerda)
        #print('Luz Esq',ValorLuzEsquerda, 'Ult Esq', ValorUltrassomEsquerda)
