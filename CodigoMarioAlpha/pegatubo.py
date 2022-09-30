from declaracoes import *

tempo_empilhadeira = 4900
tempo_garra = 8000


def sobe_empilhadeira(i = 1): #Função utilizada para subir a empilhadeira
    MotorEmpilhadeira.run_time(-200, 1.02*tempo_empilhadeira *i)
    #MotorEmpilhadeira.run_until_stalled(-100, Stop.HOLD)
    return

def desce_empilhadeira(i =1): #Função utilizada para fescer a empilhadeira
    MotorEmpilhadeira.run_time(200, tempo_empilhadeira* i)
    #MotorEmpilhadeira.run_until_stalled(200, Stop.HOLD)
    #MotorEmpilhadeira.run_time(100, 500)
    return

def fecha_garra(i = 1):  #Função utilizada para fechar a garra da empilhadeira - Retorna TRUE quando um tubo foi pego e False quando não foi pego
    if i == 10:
        i = 1
        tempo = tempo_garra/3
    elif i == 15:
        i = 1
        tempo = tempo_garra*0.66
    elif i == 20:
        i = 1
        tempo = tempo_garra
    else:
        tempo = tempo_garra
    MotorGarra.run_time(-400,i* tempo)
    #MotorGarra.run_until_stalled(-300, Stop.HOLD)
    # MotorGarra.reset_angle(0)
    # angulo = MotorGarra.run_until_stalled(-300, Stop.HOLD)  #angulo = angulo que o motor rodou até parar
    # print(angulo)
    # if angulo < 130:
    #     return True
    # else:
    #     return False

def abre_garra(i =1): #Função utilizada para abrir a garra da empilhadeira
    if i == 10:
        i = 1
        tempo = tempo_garra/3
    elif i == 15:
        i = 1
        tempo = tempo_garra/2
    elif i == 20:
        i = 1
        tempo = tempo_garra
    else:
        tempo = tempo_garra
    MotorGarra.run_time(400, i*tempo)
    #MotorGarra.run_until_stalled(300, Stop.HOLD)
    return


def pegar_tubo(tam = 20):      # Função utilizada para pegar um tubo, considerando o robô já alinhado ao tubo
    desce_empilhadeira()
    robot.straight(100)
    abre_garra(tam)
    sobe_empilhadeira()



def checa_tubo(tamanho):  #Função utilizada para checar se o robô está alinhado ao tubo (de tamanho definido no parâmetro da função) antes de pegá-lo - se não está alinhado ela alinha - 
    distancia = UltrassomFrente.distance()
    if tamanho == 10:
        angulo = 15
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
    desce_empilhadeira(0.6)
    fecha_garra(0.4)
    robot.straight(-200)
    sobe_empilhadeira(0.6)
    fecha_garra(tam)

def posiciona_gasoduto(): #Função que posiciona o robô de forma correta para colocar o tubo no gasoduto
    distancia = UltrassomFrente.distance()
    while distancia > 80:
        distancia = UltrassomFrente.distance()
        robot.drive(70,0)
    robot.stop()
    robot.straight(15)

def pega(): # Função feita apenas para testar a captura de um tubo na frente do robô, e a sua devolução no gasoduto a sua frente também
    robot.drive(70,0)
    distancia = UltrassomFrente.distance()
    if distancia < 180:
        robot.stop()
        pegar_tubo()
        posiciona_gasoduto()
        devolve_tubo()
        fecha_garra(15)
        wait(4000)

def pega2(tam):
    distancia = UltrassomFrente.distance()
    while distancia > 180:
        robot.drive(70,0)
        distancia = UltrassomFrente.distance()
    robot.stop()
    pegar_tubo(tam)
    posiciona_gasoduto()
    devolve_tubo(tam)

