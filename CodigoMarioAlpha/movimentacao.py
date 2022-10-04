from declaracoes import *
from pegatubo import *
from servidor import*
from percorregasoduto import *
from cores import *
from comeco import *

#Arquivo para as funções de movimentação do meio do desafio como subir e descer rampas, encontrar tubos e etc



def le_ultrassom_frente_cores():
    global DistanciaUltrassomFrente
    le_sensor_cor()
    DistanciaUltrassomFrente = UltrassomFrente.distance()
    return

def vira_90_cuidadoso():  #Vira 90 graus sem trombar no gasoduto
    robot.straight(-45)  #Dando uma rézinha antes pra n bater no gasoduto
    watch_virada.reset()
    while watch_virada.time() < 3000:
        robot.drive(30,30)
    robot.stop()

def desce_rampa_costas(): #Desce rampa de costas, já estando de costas pra rampa, e gira
    le_sensor_cor()
    while not (viu_azul()): # Descendo a rampa
        le_sensor_cor()
        robot.drive(-70,0)
    while not (viu_verde_azul()):
        le_sensor_cor()
        robot.drive(70,0)
    alinha_verde_azul()
    robot.straight(-100)
    robot.turn(90)
    return


def gasoduto_ate_rampa():  #Após achar um GAP, percurso do gasoduto até encontrar o verde da rampa
    global DistanciaUltrassomFrente
    vira_90_cuidadoso()
    le_ultrassom_frente_cores()
    while not(viu_verde_azul()):
        le_ultrassom_frente_cores()
        if DistanciaUltrassomFrente < 200:
            vira_90_cuidadoso()
        else:
            robot.drive(120,0)
    alinha_verde_azul()


def anda_ate_direita_rampa():   #Alinhado no verde em baixo, vira a direita e chega até o fim da arena na direita e se alinha no verde novamente
    robot.straight(-100)
    robot.turn(90)
    while not viu_beirada():
        le_sensor_cor()
        if viu_verde_azul():
            robot.drive(20,40)
        else:
            robot.drive(100,0)
    alinha_beirada()
    robot.straight(-400) #VALOR COMBINADO COM O LUIGI
    robot.turn(-90)
    while not viu_verde_azul():
        le_sensor_cor()
        robot.drive(120,0)
    alinha_verde_azul()

def sobe_rampa():   # Sobe rampa de frente já alinhado
    le_sensor_cor()
    while not viu_branco():
        robot.drive(80,0)
        le_sensor_cor()
    robot.stop()
    alinha_branco()
    robot.stop()
    # wait(5000)
    # robot.straight(100)
    # robot.stop()

def busca_tubo(tamanho):  # Função chamada depois de encontrar o GAP do gasoduto, engloba a saída do gasoduto até a pegada do tubo
    gasoduto_ate_rampa()
    anda_ate_direita_rampa()
    sobe_rampa()
    pega_tubo(tamanho)
    return

def gasoduto_apos_pegar_tubo():
    desce_rampa_costas()
    chega_no_gasoduto()
