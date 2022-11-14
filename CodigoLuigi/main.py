#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import *

def loop_tubo():
    MboxConfirmacao.send('Nada')
    print('mailbox cores recebe antes deu: ',MboxCores.read())
    print('mailbox cores devolve antes deu: ',MboxCoresDevolve.read()) 
    if getTuboPraDevolver() != 'Nada':
        devolve_tubo()
        vai_pro_ponto_inicial(False)
    while MboxCores.read() =='Nada' or MboxCores.read() == None:
        pass
    setTuboPraDevolver(MboxCoresDevolve.read())
    setCaixaDeCorreio(MboxCores.read())
    print('caixa de correio entrou: ',getCaixaDeCorreio())
    print('mailbox cores devolve depois deu: ',getTuboPraDevolver()) 
    sai_do_ponto_inicial_e_vai_pra_area()

    verifica_tubo_reto(50,80,770,False)
    if not getPegouTubo():
        volta_pro_comeco_area(770)
        verifica_tubo_reto(50,80,760,False)
        print('pegar tubo no main deu',getPegouTubo())
        if not getPegouTubo():#passada interna
            volta_pro_comeco_area(760)
            entra_na_na_area()
            verifica_tubo_reto(50,80,760,True)
            print('pegar tubo no main deu',getPegouTubo())   
            if not getPegouTubo():
                sai_da_area()
                volta_pro_comeco_area(760)
                verifica_tubo_90(50,80,770)
                print('pegar tubo no main deu',getPegouTubo()) 
                if not getPegouTubo():
                    setPegouTubo(True)
                    rodas.turn(180)

    posiciona_tubo_mario()
    le_sensor_cor()
    while not ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX): 
        le_sensor_cor()
        segue_linha_sensor_esquerdo_prop(100)
    atitude(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX,TURN_BORDA)

    MboxConfirmacao.send('Tubo entregue')
    while MboxConfirmacao.read() !='Tubo pego':
        pass

def inicio():
    conecta_alpha_luigi()
    rodas.straight(-100)
    ajustes_comeco()
    while not MboxPodeComecar.read():
        pass
    vai_pro_ponto_inicial(True)
    acha_localizacao_das_cores()
    setTuboPraDevolver('Nada')
    while True:
        loop_tubo()

inicio()

# verifica_tubo_reto(50,80,760,False)

# while True:
#     motorUltassom.run(100)

# while True:
#     le_sensor_cor()
#     rodas.drive(20,0)

# while True:
#     le_sensor_cor()
#     rodas.drive(80,0)
# verifica_tubo_reto(50,80,770,False)

# verifica_tubo_90(50,80,770)

# ----------------------------------------------------------------------------------
# cores_teste = ['vermelho','amarelo','azul']
# devolve_teste = ['vermelho','azul','amarelo']


# comeco = True
# for i in range(3):
        # pegou_mesmo = True
#     setCaixaDeCorreio(cores_teste[i])
#     setTuboPraDevolver(devolve_teste[i])
#     if comeco:
#         vai_pro_ponto_inicial(True)
#         acha_localizacao_das_cores()
#         comeco = False
#     else:
#         vai_pro_ponto_inicial(False)
    
#     if getTuboPraDevolver() == 'Nada':
#         wait(800)
#     else:
#         devolve_tubo()
#         vai_pro_ponto_inicial(False)

#     sai_do_ponto_inicial_e_vai_pra_area()
    # verifica_tubo_reto(50,80,770,False)
    # if not getPegouTubo():
    #     volta_pro_comeco_area(770)
    #     verifica_tubo_reto(50,80,760,False)
    #     print('pegar tubo no main deu',getPegouTubo())
    #     if not getPegouTubo():#passada interna
    #         volta_pro_comeco_area(760)
    #         entra_na_na_area()
    #         verifica_tubo_reto(50,80,760,True)
    #         print('pegar tubo no main deu',getPegouTubo())   
    #         if not getPegouTubo():
    #             sai_da_area()
    #             volta_pro_comeco_area(760)
    #             verifica_tubo_90(50,80,770)
    #             print('pegar tubo no main deu',getPegouTubo()) 
    #             if not getPegouTubo():
    #                 setPegouTubo(True)
    #                 pegou_mesmo = False
    #                 rodas.turn(180)

# if pegou_mesmo:
#     posiciona_tubo_mario()
#     le_sensor_cor()
#     while not ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX): 
#         le_sensor_cor()
#         segue_linha_sensor_esquerdo_prop(100)
#     atitude(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX,TURN_BORDA)

# ----------------------------------------------------------------------------------------------------    
=======

ev3 = EV3Brick()
motor_esq = Motor(Port.D)
motor_dir = Motor(Port.C)
sensor_cor_esq = ColorSensor(Port.S3)
giroscopio = GyroSensor(Port.S2)
rodas = DriveBase(motor_esq, motor_dir, wheel_diameter= 40, axle_track=110)
#ultrassom = UltrasonicSensor(Port.S1)
MotorUltrassom = Motor(Port.B)


client = BluetoothMailboxClient()
MboxAlphaLuigi = TextMailbox('alphaluigi', client)

def conecta_alpha_luigi():
    # This is the name of the remote EV3 or PC we are connecting to.
    SERVER = 'ev3dev'

=======
        # In this program, the client sends the first message and then waits for the
        # server to reply.
    MboxAlphaLuigi.send('hello!')
    MboxAlphaLuigi.wait()
    print(MboxAlphaLuigi.read())
