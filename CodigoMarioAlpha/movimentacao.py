from declaracoes import *
from pegatubo import *
from servidor import*
from percorregasoduto import *
from cores import *
from comeco import *

#Arquivo para as funções de movimentação do meio do desafio como subir e descer rampas, encontrar tubos e etc

eq = False
dr = False

def le_ultrassom_frente_cores():
    global DistanciaUltrassomFrente
    le_sensor_cor()
    DistanciaUltrassomFrente = UltrassomFrente.distance()
    return

def reposiciona_gasoduto(): #Se reposiciona no gasoduto para continuar seu percorrimnto após a entrega de um tubo
    DistanciaUltrassomFrente = UltrassomFrente.distance()
    while DistanciaUltrassomFrente > 160:
        DistanciaUltrassomFrente = UltrassomFrente.distance()
        le_sensor_cor()
        if viu_beirada():
            robot.drive(20,40)
        else:
            robot.drive(70,0)
    robot.stop()
    watch.reset()
    while watch.time()<2650:
        robot.drive(8, 29)
    robot.stop()
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
        if DistanciaUltrassomFrente < 100:
            robot.straight(-100)
            ev3.speaker.beep(900,900)
            vira_90_cuidadoso()
        elif viu_beirada():
            alinha_beirada()
            robot.straight(-100)
            robot.turn(90)
        else:
            robot.drive(70,0)
    alinha_verde_azul()

def gasoduto_ate_rampa_final():  #Volta para a rampa após o final do gasoduto
    global DistanciaUltrassomFrente
    robot.straight(-80)
    vira_90_cuidadoso()
    le_sensor_cor()
    while not(viu_verde_azul()):
        le_sensor_cor()
        if viu_beirada():
            robot.drive(70,10)
        else:
            robot.drive(70,0)
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

def anda_ate_direita_branco():   #Alinhado no branco em cima, vira a direita e chega até o fim da arena na direita, pra pegar o tubo
    robot.straight(50)
    robot.turn(180)
    while not viu_verde_branco():
        le_sensor_cor()
        robot.drive(50,0)
    alinha_verde_branco()
    robot.straight(-100)
    robot.turn(-90)
    le_sensor_cor()
    while not viu_beirada():
        le_sensor_cor()
        if viu_verde_branco():
            robot.drive(50,-5)
        else:
            robot.drive(90,0)
    alinha_beirada()
    robot.straight(-400) #VALOR COMBINADO COM O LUIGI
    robot.turn(-90)

def anda_ate_fim_direita_branco(): #vai até o outro lado da arena buscar o tubo depois de devolver o tubo do lado esquerdo
    le_sensor_cor()
    while not viu_beirada():
        le_sensor_cor()
        if not viu_branco_dr():
            ev3.speaker.beep(900)
            robot.drive(90,-9)
        else:
            robot.drive(90,2)
    alinha_beirada()
    robot.straight(-400) #VALOR COMBINADO COM O LUIGI
    robot.turn(-90)



def sobe_rampa():   # Sobe rampa de frente já alinhado
    global eq
    global dr
    le_sensor_cor()
    while not viu_branco():
        le_sensor_cor()
        if viu_beirada_eq():
            print('Entrei aqui na esquerda -rampa')
            robot.drive(80,30)
        elif viu_beirada_dr():
            print('Entrei aqui na direita - rampa')
            robot.drive(80,-30)
        else:
            robot.drive(120,0)
    robot.stop()
    alinha_branco()
    robot.stop()

def posiciona_para_devolver_Luigi(tamanho_do_tubo_na_garra, tamanho_do_tubo_espera): # Já em cima da rampa, se posiciona e coloca o tubo no lugar para o Luigi devolver
    robot.straight(100)
    robot.turn(-90)
    while not viu_beirada():
        le_sensor_cor()
        if not viu_branco_eq():
            ev3.speaker.beep(900)
            robot.drive(80,9)
        else:
            robot.drive(80,0)
    alinha_beirada()
    robot.straight(-400) #Valor combinado
    robot.turn(90)
    robot.straight(120) # Valor combinado
    desce_empilhadeira()
    fecha_garra(tamanho_do_tubo_na_garra)
    robot.straight(-120)
    sobe_empilhadeira_centro()
    tamanho_do_tubo_na_garra = 0
    robot.turn(90)
    busca_tubo_ja_acima(tamanho_do_tubo_espera)

def busca_tubo(tamanho):  # Função chamada depois de encontrar o GAP do gasoduto, engloba a saída do gasoduto até a pegada do tubo (alinhando em baixo)
    gasoduto_ate_rampa()
    anda_ate_direita_rampa()
    sobe_rampa()
    pega_tubo(tamanho)
    return

def busca_tubo_em_cima(tamanho): #Igual a de cima, porém se alinha em cima - começando no gasoduto
    gasoduto_ate_rampa()
    sobe_rampa()
    anda_ate_direita_branco()
    pega_tubo(tamanho)
    return

def busca_tubo_ja_acima(tamanho): #Busca tubo já estando na parte de cima, depois de devolver um tubo
    anda_ate_fim_direita_branco()
    pega_tubo(tamanho)
    gasoduto_apos_pegar_tubo()
    #percorre_gasoduto_esquerda('entregar') # essa func já está sendo chamada no while not tubo foi entregue na main()
    return



def gasoduto_apos_pegar_tubo():  #Função para chegar no gasoduto após pegar um tubo
    desce_rampa_costas()
    chega_no_gasoduto()

def devolve_tubo_ao_Luigi(tamanho_do_tubo_na_garra, tamanho_do_tubo_espera):
    gasoduto_ate_rampa_final()
    sobe_rampa()
    posiciona_para_devolver_Luigi(tamanho_do_tubo_na_garra, tamanho_do_tubo_espera)