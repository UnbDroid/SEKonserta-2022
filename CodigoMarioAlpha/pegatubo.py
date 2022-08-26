from declaracoes import *


def sobe_empilhadeira(): #Função utilizada para subir a empilhadeira
    MotorEmpilhadeira.run_time(100, tempo_empilhadeira)
    return

def desce_empilhadeira(): #Função utilizada para fescer a empilhadeira
    MotorEmpilhadeira.run_time(-100, tempo_empilhadeira)
    return

def fecha_garra():  #Função utilizada para fechar a garra da empilhadeira
    MotorGarra.run_time(150, tempo_garra)
    return

def abre_garra(): #Função utilizada para abrir a garra da empilhadeira
    MotorGarra.run_time(-150, tempo_garra)
    return


def pegar_tubo():      # Função utilizada para pegar um tubo, considerando o robô já alinhado ao tubo
    desce_empilhadeira()
    robot.straight(100)
    sobe_empilhadeira()
    #fecha_garra()


def checa_tubo(tamanho):  #Função utilizada para checar se o robô está alinhado ao tubo (de tamanho definido no parâmetro da função) antes de pegá-lo - se não está alinhado ela alinha - 
    distancia = UltrassomFrente.distance()
    angulo = 25
    print("a distância é", distancia)
    robot.turn(angulo)
    distancia_direita = UltrassomFrente.distance()
    print("a distância na direita é", distancia_direita)
    time.sleep(3)
    robot.turn(angulo * -2)
    distancia_esquerda = UltrassomFrente.distance()
    print("a distância na esquerda é", distancia_esquerda)
    time.sleep(3)
    robot.turn(angulo)
    diff = distancia_direita - distancia_esquerda
    if diff > 0:
        maior = distancia_direita
    elif diff < 0:
        maior = distancia_esquerda
    else:
        maior - 0
    if maior >= 210:
        print('hehe')
    return

def devolve_tubo():  #Função utilizada apenas para colocar o tubo no gasoduto, já considerando o robô posicionado corretamente
    #desce_empilhadeira()
    MotorEmpilhadeira.run_time(-100, 300)
    abre_garra()
    robot.straight(-200)
    MotorEmpilhadeira.run_time(100, 300)
    #sobe_empilhadeira()

def posiciona_gasoduto(): #Função que posiciona o robô de forma correta para colocar o tubo no gasoduto
    distancia = UltrassomFrente.distance()
    while distancia > 60:
        distancia = UltrassomFrente.distance()
        print(distancia)
        robot.drive(70,0)
    robot.stop()
    time.sleep(1)
    robot.straight(50)

def pega():
    #robot.drive(70,0)
    distancia = UltrassomFrente.distance()
    #print(distancia)
    #robot.drive(30,0)
    if distancia < 140:
        robot.stop()
        checa_tubo(10)
        pegar_tubo()
        posiciona_gasoduto()
        devolve_tubo()