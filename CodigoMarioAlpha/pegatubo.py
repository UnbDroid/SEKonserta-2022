from declaracoes import *


def sobe_empilhadeira(): #Função utilizada para subir a empilhadeira
    #MotorEmpilhadeira.run_time(100, tempo_empilhadeira)
    MotorEmpilhadeira.run_until_stalled(100, Stop.HOLD)
    return

def desce_empilhadeira(): #Função utilizada para fescer a empilhadeira
    #MotorEmpilhadeira.run_time(-100, tempo_empilhadeira)
    MotorEmpilhadeira.run_until_stalled(-100, Stop.HOLD)
    MotorEmpilhadeira.run_time(100, 200)
    return

def fecha_garra():  #Função utilizada para fechar a garra da empilhadeira - Retorna TRUE quando um tubo foi pego e False quando não foi pego
    MotorGarra.reset_angle(0)
    angulo = MotorGarra.run_until_stalled(100, Stop.HOLD)  #angulo = angulo que o motor rodou até parar
    print(angulo)
    if angulo < 130:
        return True
    else:
        return False

def abre_garra(): #Função utilizada para abrir a garra da empilhadeira
    MotorGarra.run_until_stalled(-100, Stop.HOLD)
    return


def pegar_tubo():      # Função utilizada para pegar um tubo, considerando o robô já alinhado ao tubo
    abre_garra()
    desce_empilhadeira()
    robot.straight(100)
    sobe_empilhadeira()
    print(fecha_garra())



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

def devolve_tubo():  #Função utilizada apenas para colocar o tubo no gasoduto, já considerando o robô posicionado corretamente
    #desce_empilhadeira()
    abre_garra()
    MotorEmpilhadeira.run_time(-150, 300)
    robot.straight(-200)
    MotorEmpilhadeira.run_time(150, 300)
    print(fecha_garra())
    #sobe_empilhadeira()

def posiciona_gasoduto(): #Função que posiciona o robô de forma correta para colocar o tubo no gasoduto
    distancia = UltrassomFrente.distance()
    while distancia > 60:
        distancia = UltrassomFrente.distance()
        robot.drive(70,0)
    robot.stop()
    time.sleep(1)
    robot.straight(40)

def pega(): # Função feita apenas para testar a captura de um tubo na frente do robô, e a sua devolução no gasoduto a sua frente também
    robot.drive(70,0)
    distancia = UltrassomFrente.distance()
    if distancia < 140:
        robot.stop()
        checa_tubo(10)
        pegar_tubo()
        posiciona_gasoduto()
        devolve_tubo()
        time.sleep(4)