from declaracoes import *
from servidor import *
from pegatubo import *
from cores import *

tamanho_media = 1  #Quantos valores são considerados para fazer a média das últimas n medições do ultrassom
ListaDistanciaUltrassomEsquerda = tamanho_media * [0]
ValorLuzEsquerda = 0                                                                         
DistanciaUltrassomEsquerda = 0
DistanciaUltrassomFrente = 0
valor_minimo = 5
valor_maximo = 65

def le_valores_percorrimento_esquerda():
    global ValorLuzEsquerda                                                                           
    global DistanciaUltrassomEsquerda
    global DistanciaUltrassomFrente
    global ValorCorEsquerda
    global ValorCorDireita
    ValorLuzEsquerda = MboxAlphaBetaLuz.read()                                                                            
    DistanciaUltrassomEsquerda = MboxAlphaBetaUltrassom.read()
    DistanciaUltrassomFrente = UltrassomFrente.distance()
    le_sensor_cor()

def adiciona_lista_ultrassom_esquerda():
    global DistanciaUltrassomEsquerda
    if not DistanciaUltrassomEsquerda == 772550: #2550 é o valor máx e as vezes buga nele, então para elimiar ele (esse 772550 é um valor q nunca chega)
        ListaDistanciaUltrassomEsquerda.pop(0)
        ListaDistanciaUltrassomEsquerda.append(DistanciaUltrassomEsquerda)   


def checa_distancia_ultrassom_esquerda():  # Retorna True se não foi visto tubo na esquerda
    global tamanho_media
    global ListaDistanciaUltrassomEsquerda
    if (sum(ListaDistanciaUltrassomEsquerda))/tamanho_media > 200:
        return True
    else:
        return False

def checa_distancia_ultrassom_frente():
    global DistanciaUltrassomFrente
    if DistanciaUltrassomFrente <= 140:
        return True
    else:
        return False

def checa_luz_esquerda(a):
    global valor_minimo
    global valor_maximo
    global ValorLuzEsquerda
    if a == 'min':
        if ValorLuzEsquerda <= valor_minimo:
            return True
        return False
    elif a  == 'max':
        if ValorLuzEsquerda >= valor_maximo:
            return True
        return False

def le_valores_max_min():
    global valor_maximo
    global valor_minimo
    MboxAlphaBetaLuz.wait()  # Esperando o valor mínimo
    valor_minimo = MboxAlphaBetaLuz.read()  
    print(valor_minimo)    
    MboxAlphaBetaLuz.wait() # Esperando o valor máximo
    valor_maximo = MboxAlphaBetaLuz.read()  
    print(valor_minimo)

def define_tamanho_gap():
    global distancia_percorrida
    if distancia_percorrida <= 70: #Não é GAP, só um buraquinho do gasoduto msm
        return False
    elif distancia_percorrida <= 120: # GAP - 10 cm
        print("É um buraco de 10 cm!, Foi Medido:", distancia_percorrida)
        ev3.speaker.beep(200, 700)
        return 10
    elif distancia_percorrida <= 170: #GAP - 15 cm
        print("É um buraco de 15 cm!, Foi Medido:", distancia_percorrida)
        ev3.speaker.beep(500, 700)
        return 15
    elif distancia_percorrida <= 220:# GAP - 20 cm
        print("É um buraco de 20 cm!, Foi Medido:", distancia_percorrida)
        ev3.speaker.beep(800, 700)
        return 20
    return False

def coloca_tubo(tamanho):
    global distancia_percorrida
    global condition
    robot.stop()
    if condition:  #Se a condição é verdadeira, ele parou de ler o buraco durante a curva
            pass

    else:
        watch.reset()
        if tamanho == 10:
            while watch.time()<3000:
                robot.drive(-21, -32)
        elif tamanho == 15:
            while watch.time()<3000:
                robot.drive(-38, -31)
        elif tamanho == 20:
            while watch.time()<3000:
                robot.drive(-42, -29.5)
        robot.stop()
        wait(1000)
        posiciona_gasoduto()
        devolve_tubo(tamanho)

def virada_gasoduto_esquerda():
    robot.drive(50, -16)

def virada_gasoduto_direita():
    robot.drive(50, 20)

def segue_reto_gasoduto():
    robot.drive(50,0)

def virada_ultrassom_frente():
    robot.stop()
    watch.reset()
    while watch.time()<3000:
        robot.drive(5, 29)

def virada_ultrassom_frente_medindo_gap(): #Faz a virada mas continua medindo o tamanho do GAP
    global condition
    global distancia_percorrida
    global distancia_na_curva
    robot.stop()
    print("Distância (parou na curva):", robot.distance(), "Distancia na curva:", distancia_na_curva)
    wait(2000)
    sobe_empilhadeira(0.1)
    wait(3000)
    distancia = UltrassomFrente.distance()
    while distancia >= 30:
        distancia = UltrassomFrente.distance()
        print(distancia)
        robot.drive(70,0)
    robot.stop()
    wait(5000)
    watch.reset()
    condition = False
    while watch.time()<3000:
        robot.drive(5, 29)
        if not (checa_distancia_ultrassom_esquerda() and condition): #Se ele parar de ver o cano no meio da curva

            print("Distância (parou na curva):", robot.distance(), "Distancia na curva:", distancia_na_curva)
            distancia_percorrida = robot.distance()
            robot.stop()
            ev3.speaker.beep(50,900)
            condition = True

def mede_tamanho_gap():
    global distancia_percorrida
    global distancia_na_curva
    global condition
    condition = False # Essa condição só se torna verdadeira quando o robô para de ler a ausência de tubo durante a curva
    distancia_auxiliar = 0
    distancia_na_curva = 0 # Se a maior parte da distancia lida foi em uma curva, significa q n era um gap mas sim um joelho mal colocado
    robot.reset()
    while checa_distancia_ultrassom_esquerda():
        le_valores_percorrimento_esquerda()
        adiciona_lista_ultrassom_esquerda()
        if checa_luz_esquerda('max'):
            distancia_auxiliar = robot.distance()
            virada_gasoduto_esquerda()
            distancia_na_curva += robot.distance() - distancia_auxiliar
        elif checa_distancia_ultrassom_frente():
            virada_ultrassom_frente_medindo_gap()
                #if define_tamanho_gap():
                    #coloca_tubo(define_tamanho_gap())
        elif checa_luz_esquerda('min'): 
            virada_gasoduto_direita()
        else:
            segue_reto_gasoduto()
    if not condition:
        print("Distancia: ",robot.distance(), "Distancia na curva:", distancia_na_curva)
        #ev3.speaker.beep(200)
        distancia_percorrida = robot.distance()
        robot.stop()
    #if define_tamanho_gap():
        #coloca_tubo(define_tamanho_gap())







def percorre_gasoduto_esquerda():
    global ValorLuzEsquerda                                                                           
    global DistanciaUltrassomEsquerda
    global DistanciaUltrassomFrente
    global ValorCorEsquerda
    global ValorCorDireita
    global valor_minimo
    global valor_maximo
    global distancia_percorrida
    global distancia_na_curva
    global condition
    MboxAlphaBeta.send("PercorrimentoGasodutoEsquerda")
    le_valores_max_min()
    valor_minimo = 61  #De manhã deu 58, 12h deu 75 --- 48
    valor_maximo = 75  #De manhã deu 72, 12h deu 88 -- 58
    MboxAlphaBetaUltrassom.wait()
    while True:
        le_valores_percorrimento_esquerda()
        adiciona_lista_ultrassom_esquerda()
        #print('Luz Esq',ValorLuzEsquerda, 'Ult Esq', DistanciaUltrassomEsquerda, 'ult frente', DistanciaUltrassomFrente)
        if viu_beirada():
            robot.stop()
            wait(40000)
        elif checa_luz_esquerda('max'):
            virada_gasoduto_esquerda()
        elif checa_distancia_ultrassom_frente():
            virada_ultrassom_frente()
        elif checa_distancia_ultrassom_esquerda():
            mede_tamanho_gap()
            if define_tamanho_gap():
                pass
                # coloca_tubo(define_tamanho_gap())
        elif checa_luz_esquerda('min'):
            virada_gasoduto_direita()
        else:
            segue_reto_gasoduto()
        