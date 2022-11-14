from declaracoes import *
from servidor import *
from cores import *

tempo_empilhadeira = 5400
tempo_garra = 9700 #10800
tamanho_do_tubo_na_garra = 0
tamanho_lista_frente = 2
lista_ultrassom_frente = tamanho_lista_frente * [100000]
porcentagem_centro = 1 #qt por cento a empilhadeira tem q subir do seu máximo para estar no centro
LUIGI_NAO_ENTREGOU = False

def luigi_entregou_tubo(): # Se o Luigi não entregou o tubo, voltar pro gasoduto e medir
    global LUIGI_NAO_ENTREGOU
    a = LUIGI_NAO_ENTREGOU
    LUIGI_NAO_ENTREGOU = False
    return a


def le_distancia_frente():
    global lista_ultrassom_frente
    distancia = UltrassomFrente.distance()
    lista_ultrassom_frente.pop(0)
    lista_ultrassom_frente.append(distancia)

def checa_distancia_frente_devolucao():
    global lista_ultrassom_frente
    global tamanho_lista_frente
    if (sum(lista_ultrassom_frente)/tamanho_lista_frente) <= 80:
        return True
    else:
        return False




def sobe_empilhadeira(i = 1, continuar = False): #Função utilizada para subir a empilhadeira
    if not continuar:
        MotorEmpilhadeira.run_time(-200, tempo_empilhadeira *i*1.015)
    else:
        MotorEmpilhadeira.run_time(-200, tempo_empilhadeira *i*1.015, then = Stop.HOLD, wait = False)
    return

def desce_empilhadeira(i =1, continuar = False): #Função utilizada para fescer a empilhadeira
    if not continuar:
        MotorEmpilhadeira.run_time(200, tempo_empilhadeira* i)
    else:
        MotorEmpilhadeira.run_time(200, tempo_empilhadeira* i, then = Stop.HOLD, wait = False)
    return

def desce_empilhadeira_centro(i = True):
    global porcentagem_centro
    if i:
        desce_empilhadeira(porcentagem_centro)
    else:
        desce_empilhadeira(1 - porcentagem_centro)

def sobe_empilhadeira_centro(i = True, continuar = False):
    global porcentagem_centro
    if i:
        if continuar:
            sobe_empilhadeira(porcentagem_centro, True)
        else:
            sobe_empilhadeira(porcentagem_centro)
    else:
        sobe_empilhadeira(1 - porcentagem_centro)

def desce_empilhadeira_gasoduto():
    desce_empilhadeira(0.45)

def sobe_empilhadeira_gasoduto():
    sobe_empilhadeira(0.45 - 1 + porcentagem_centro) #Sobe para o centro após colocar o tubo no gasoduti

def fecha_garra(i = 1, continuar = False):  #Função utilizada para fechar a garra da empilhadeira - Retorna TRUE quando um tubo foi pego e False quando não foi pego
    if i == 10:
        i = 1
        tempo = 3200
    elif i == 15:
        i = 1
        tempo = 5500 #4700
    elif i == 20:
        i = 1
        tempo = tempo_garra
    else:
        tempo = tempo_garra
    tempo *= 0.4
    if not continuar:
        MotorGarra.run_time(-1000,1*i* tempo)
    else:
        MotorGarra.run_time(-1000, i*tempo, then=Stop.HOLD, wait = False)

def abre_garra(i =1, continuar = False): #Função utilizada para abrir a garra da empilhadeira - if continue = True, abrir e continuar o programa
    if i == 10:
        i = 1
        tempo = 3200
    elif i == 15:
        i = 1
        tempo = 5500 #4700
    elif i == 20:
        i = 1
        tempo = tempo_garra
    else:
        tempo = tempo_garra
    tempo *= 0.4
    if not continuar:
        MotorGarra.run_time(1000, i*tempo)
        #MotorGarra.run_time(1000, tempo * 0.4)
        #MotorGarra.run_time(-1000,tempo * 0.4)
    else:
        MotorGarra.run_time(800, i*tempo, then=Stop.HOLD, wait = False) #Continuar o código enquanto abre a garra
    return

def fecha_garra_alinhar(i = 10, condition = True): # i [e o tamanho]
    tempo10 = 0.7
    if i == 10:
        if condition:
            MotorGarra.run_time(-1000, 6000 * tempo10)
        else:
            MotorGarra.run_time(-1000, 6000 * tempo10)


def fecha_garra_gasoduto():
    fecha_garra(0.4)

def abre_garra_gasoduto():
    abre_garra(0.4)



def checa_tubo(tamanho):  #Função utilizada para checar se o robô está alinhado ao tubo (de tamanho definido no parâmetro da função) antes de pegá-lo - se não está alinhado ela alinha - 
    distancia = UltrassomFrente.distance()
    if tamanho == 10:
        angulo = 30
    elif tamanho == 15:
        angulo = 22 #falta testar
    elif tamanho == 20:
        angulo = 30
    print("a distância é", distancia)
    robot.turn(angulo)
    time.sleep(1)
    distancia_direita = UltrassomFrente.distance()
    print("a distância na direita é", distancia_direita)
    robot.turn(angulo * -2)
    time.sleep(1)
    distancia_esquerda = UltrassomFrente.distance()
    print("a distância na esquerda é", distancia_esquerda)
    robot.turn(angulo)
    time.sleep(1)
    diff = distancia_direita - distancia_esquerda

    robot.turn(angulo * diff * 0.005) # Corrigindo para o meio do tubo
    return

def devolve_tubo(tam =20):  #Função utilizada apenas para colocar o tubo no gasoduto, já considerando o robô posicionado corretamente
    desce_empilhadeira_gasoduto()
    fecha_garra(0.4)
    robot.straight(-200)
    sobe_empilhadeira_gasoduto()
    ev3.speaker.beep(200)
    abre_garra_gasoduto()
    ev3.speaker.beep(900)
    fecha_garra(tam, True)


def posiciona_gasoduto(): #Função que posiciona o robô de forma correta para colocar o tubo no gasoduto
    # distancia = UltrassomFrente.distance()
    # while distancia > 80:
    #     distancia = UltrassomFrente.distance()
    #     robot.drive(70,0)
    # robot.stop()
    # robot.straight(10)
    robot.stop()
    robot.straight(250)
    robot.straight(-34)
    robot.stop()


def pega(): # Função feita apenas para testar a captura de um tubo na frente do robô, e a sua devolução no gasoduto a sua frente também
    robot.drive(70,0)
    distancia = UltrassomFrente.distance()
    if distancia < 180:
        robot.stop()
        pegar_tubo()
        posiciona_gasoduto()
        devolve_tubo()
        fecha_garra(15)

def pega2(tam):  #Outra função apenas de teste para pegar e devolver o tubo
    distancia = UltrassomFrente.distance()
    while distancia > 180:
        robot.drive(70,0)
        distancia = UltrassomFrente.distance()
    robot.stop()
    pegar_tubo(tam)
    posiciona_gasoduto()
    devolve_tubo(tam)

def alinha_tubo(tamanho):
    MotorGarra.run_time(1000, 6000) # abriu
    robot.straight(105)
    fecha_garra_alinhar(tamanho)
    MotorGarra.run_time(1000, 2100)
    robot.straight(-65)
    MotorGarra.run_time(-1000, 2100)
    fecha_garra_alinhar(tamanho, False)



def pega_tubo(tamanho): #Função que pega o tubo já alinhado com ele previamente, com o tubo na sua frente a uma distância indefinida
    global tamanho_do_tubo_na_garra
    global LUIGI_NAO_ENTREGOU
    robot.straight(-25)
    while not posso_pegar_tubo():
        pass
    DistanciaUltrassomFrente = UltrassomFrente.distance()
    le_sensor_cor()
    while (DistanciaUltrassomFrente > 170):
        le_sensor_cor()
        robot.drive(70,0)
        DistanciaUltrassomFrente = UltrassomFrente.distance()
        if (viu_preto() or viu_amarelo() or viu_azul() or viu_vermelho()):
            LUIGI_NAO_ENTREGOU = True
            break
    robot.stop()
    if not LUIGI_NAO_ENTREGOU: #Se o Luigi entregou o tubo, pegar ele
        robot.stop()
        ev3.speaker.beep()
        desce_empilhadeira_centro()
        if tamanho == 10:
            alinha_tubo(tamanho)
        robot.straight(91)
        tamanho_do_tubo_na_garra = tamanho
        print("o tamanho é esse", tamanho_do_tubo_na_garra)
        if tamanho == 15:
            ev3.speaker.beep(900,700)
        abre_garra(tamanho)
        sobe_empilhadeira()
    manda_nada_cores_luigi()
    manda_confirmacao_luigi()

