from declaracoes import *

def le_sensor_cor(): #TODO como que esse valor é lido? ele é um inteiro normal? Como que eu sei qual cor que está?!

    setValorCorEsquerda(luzEsquerda.rgb()) # é uma lista de 3 valores RGB
    setValorCorDireita(luzDireita.rgb())

    #print("[LE SENSOR] Valor na Esquerda é:", getValorCorEsquerda(), "E na direita é", getValorCorDireita())

    return

def valor_no_intervalo_ve_cor(min, max, valor):
    pos0_fora = min[0] <= valor[0] <= max[0]
    pos1_fora = min[1] <= valor[1] <= max[1]
    pos2_fora = min[2] <= valor[2] <= max[2]
    # print('lendo valor 0:', pos0_fora)
    # print('lendo valor 1:', pos1_fora)
    # print('lendo valor 2:', pos2_fora)
    # print('and de tudo: ',pos0_fora and pos1_fora and pos2_fora)
    return pos0_fora and pos1_fora and pos2_fora


def ve_cor(eq_min, eq_max, dr_min, dr_max):

    valorEsquerdo = getValorCorEsquerda()
    valorDireito = getValorCorDireita()

    setDr(False)
    setEq(False)
    #print('entrou aq')
    #print(valorDireito)
    if valor_no_intervalo_ve_cor(eq_min, eq_max, valorEsquerdo):
        setEq(True)
    if valor_no_intervalo_ve_cor(dr_min, dr_max, valorDireito):
        setDr(True)
    
    #print('dr eh: ',getDr())    
    return getEq() or getDr()


def ve_cor_dois_sensores(eq_min, eq_max, dr_min, dr_max):

    valorEsquerdo = getValorCorEsquerda()
    valorDireito = getValorCorDireita()

    setDr(False)
    setEq(False)
    #print('entrou aq')
    #print(valorDireito)
    if valor_no_intervalo_ve_cor(eq_min, eq_max, valorEsquerdo):
        setEq(True)
    if valor_no_intervalo_ve_cor(dr_min, dr_max, valorDireito):
        setDr(True)
    
    #print('dr eh: ',getDr())    
    return getEq() and getDr()



def valor_fora_do_intervalo(min, max, val):
    pos0_fora = min[0] > val[0] or val[0] > max[0]
    pos1_fora = min[1] > val[1] or val[1] > max[1]
    pos2_fora = min[2] > val[2] or val[2] > max[2]
    # print(pos0_fora)
    # print(pos1_fora)
    # print(pos2_fora)
    return pos0_fora or pos1_fora or pos2_fora

def valor_no_intervalo(min, max, val):
    pos0_fora = min[0] <= val[0] <= max[0]
    pos1_fora = min[1] <= val[1] <= max[1]
    pos2_fora = min[2] <= val[2] <= max[2] 
    # print(pos0_fora)
    # print(pos1_fora)
    # print(pos2_fora)
    return pos0_fora or pos1_fora or pos2_fora

def alinha_robo(eq_min, eq_max, dr_min, dr_max):
    valorEsquerdo = getValorCorEsquerda()
    valorDireito = getValorCorDireita()

    # RAMPA_DIREITO_MIN_ = [2, 9, 3]
    # RAMPA_DIREITO_MAX = [15, 22, 15] 

    #print('esta alinhando, esq: ',valorEsquerdo)
    #print('esta alinhando, dir: ',valorDireito)
#    rodas.stop()
    le_sensor_cor()
    if(valor_fora_do_intervalo(dr_min, dr_max, valorDireito)):
        #print("entrei no if do valor no intervalo")
        while(valor_fora_do_intervalo(dr_min, dr_max, valorDireito)):
            rodas.drive(15,-30) #direita
            setValorCorDireita(luzDireita.rgb())
            valorDireito = getValorCorDireita()
            #print('lendoSensorCorDir: ',valorDireito)

    elif (valor_fora_do_intervalo(eq_min, eq_max, valorEsquerdo)):
        #print("entrei no if do valor no intervalo")
        #dir vendo_preto
        while valor_fora_do_intervalo(eq_min, eq_max, valorEsquerdo):
            rodas.drive(15,30) #esquerda
            #le_sensor_cor()
            setValorCorEsquerda(luzEsquerda.rgb())
            valorEsquerdo = getValorCorEsquerda()
            #print('lendoSensorCorEsq: ',valorEsquerdo)

    # if  eq_min[0] < valorEsquerdo[0] > eq_max[0] and eq_min[1] < valorEsquerdo[1] > eq_max[1] and eq_min[2] < valorEsquerdo[2] > eq_max[2]: #esq não vendo borda
    #     while  eq_min[0] < valorEsquerdo[0] > eq_max[0] and eq_min[1] < valorEsquerdo[1] > eq_max[1] and eq_min[2] < valorEsquerdo[2] > eq_max[2]: #TODO ValorCorEsquerda se for maior que o mínimo e maior que o máximo?!
    #         rodas.drive(15,30) #direita
    #         setValorCorEsquerda(luzEsquerda.rgb())
    #         valorEsquerdo = getValorCorEsquerda()
    #         print('corEsquerda: ',corEsquerda)
    #         print('lendoSensorCorEsq: ',valorEsquerdo)

    rodas.stop()
    return True


def alinha_robo(eq_min, eq_max, dr_min, dr_max):
    valorEsquerdo = getValorCorEsquerda()
    valorDireito = getValorCorDireita()
    
    le_sensor_cor()
    if(valor_fora_do_intervalo(dr_min, dr_max, valorDireito)):
        #print("entrei no if do valor no intervalo")
        while(valor_fora_do_intervalo(dr_min, dr_max, valorDireito)):
            rodas.drive(15,-30) #direita
            setValorCorDireita(luzDireita.rgb())
            valorDireito = getValorCorDireita()
            #print('lendoSensorCorDir: ',valorDireito)

    elif (valor_fora_do_intervalo(eq_min, eq_max, valorEsquerdo)):
        #print("entrei no if do valor no intervalo")
        #dir vendo_preto
        while valor_fora_do_intervalo(eq_min, eq_max, valorEsquerdo):
            rodas.drive(15,30) #esquerda
            #le_sensor_cor()
            setValorCorEsquerda(luzEsquerda.rgb())
            valorEsquerdo = getValorCorEsquerda()
            #print('lendoSensorCorEsq: ',valorEsquerdo
    rodas.stop()
    return True

def alinha_preto_re():
    valorEsquerdo = getValorCorEsquerda()
    valorDireito = getValorCorDireita()

    eq_min =[4, 6, 3]
    eq_max = [6,8,5]

    dr_min = [9, 12, 13]
    dr_max = [12,14,20] 
    
    if eq_min[0] < valorEsquerdo[0] > eq_max[0] and eq_min[1] < valorEsquerdo[1] > eq_max[1] and eq_min[2] < valorEsquerdo[2] > eq_max[2]: #esq não vendo preto
        while eq_min[0] < valorEsquerdo[0] > eq_max[0] and eq_min[1] < valorEsquerdo[1] > eq_max[1] and eq_min[2] < valorEsquerdo[2] > eq_max[2]:
            rodas.drive(-15,-30) #direita
            le_sensor_cor()
            valorEsquerdo = getValorCorEsquerda()
            #print("Valor na Esquerda é:", valorEsquerdo, "E na direita é", valorDireito)

    elif dr_min[0] < valorDireito[0] > dr_max[0] and dr_min[1] < valorDireito[1] > dr_max[1] and dr_min[2] < valorDireito[2] > dr_max[2]: #dir vendo_preto
        while dr_min[0] < valorDireito[0] > dr_max[0] and dr_min[1] < valorDireito[1] > dr_max[1] and dr_min[2] < valorDireito[2] > dr_max[2]:
            rodas.drive(-15,30) #esquerda
            le_sensor_cor()
            valorDireito = getValorCorDireita()
            
    rodas.stop()

    return True

def alinha_preto_frente():
    valorEsquerdo = getValorCorEsquerda()
    valorDireito = getValorCorDireita()

    eq_min =[4, 6, 3]
    eq_max = [6,8,5]

    dr_min = [9, 12, 13]
    dr_max = [12,14,20] 

    
    if(valor_no_intervalo(eq_min, eq_max, valorEsquerdo)):
        print("AlinhaPretoFrente entrei no if do valor no intervalo")
        while(valor_fora_do_intervalo(eq_min, eq_max, valorEsquerdo)):
            rodas.drive(15,-30) #direita
            setValorCorDireita(luzDireita.rgb())
            valorDireito = getValorCorDireita()
            print('em ALINHA PRETO FRENTE lendoSensorCorDireita: ',valorDireito)

    if (valor_no_intervalo(dr_min, dr_max, valorDireito)):
        print("AlinhaPretoFrente entrei no if do valor no intervalo")
        #dir vendo_preto
        while valor_fora_do_intervalo(eq_min, eq_max, valorEsquerdo):
            rodas.drive(15,30) #esquerda
            #le_sensor_cor()
            setValorCorEsquerda(luzEsquerda.rgb())
            valorEsquerdo = getValorCorEsquerda()
            print('em ALINHA PRETO FRENTE lendoSensorCorEsq: ',valorEsquerdo)

    rodas.stop()
    return True

def segue_linha_sensor_esquerdo_prop(DRIVE_SPEED):
    PRETO = 5#8
    
    threshold = 40 #50
    PROPORTIONAL_GAIN = 1.5

    #leitura_sensor = luzEsquerda.reflection()
    #print(leitura_sensor)
    leitura_sensor = getValorCorEsquerda()

    deviation =  threshold - leitura_sensor[0]
    turn_rate = PROPORTIONAL_GAIN * deviation
    rodas.drive(DRIVE_SPEED, turn_rate)

def segue_linha_sensor_direito_prop(DRIVE_SPEED):
    PRETO = 12 #15
    
    threshold = 70 #75
    PROPORTIONAL_GAIN = 1

    #leitura_sensor = luzDireita.reflection()
    #print(leitura_sensor)
    leitura_sensor = getValorCorDireita()

    deviation =  leitura_sensor[0] - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    rodas.drive(DRIVE_SPEED, turn_rate)

def segue_linha_sensor_esquerdo_re(DRIVE_SPEED):
    PRETO = 5
    
    threshold = 28
    PROPORTIONAL_GAIN = 1.2

    leitura_sensor = luzEsquerda.rgb()
    print(leitura_sensor)
    
    deviation =  threshold - leitura_sensor[0]
    turn_rate = PROPORTIONAL_GAIN * deviation
    rodas.drive(DRIVE_SPEED, -turn_rate)

def segue_linha_sensor_direito_re(DRIVE_SPEED):
    PRETO = 12 #15
    
    threshold = 70 #75
    PROPORTIONAL_GAIN = 1

    #leitura_sensor = luzDireita.reflection()
    #print(leitura_sensor)
    leitura_sensor = getValorCorDireita()

    deviation =  leitura_sensor[0] - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    rodas.drive(DRIVE_SPEED, -turn_rate)

def identifica_cor_da_area_dois_sensores():
    setCores("nada")
    
    le_sensor_cor()
    if ve_cor(AMARELO_ESQ_MIN, AMARELO_ESQ_MAX, AMARELO_DIR_MIN, AMARELO_DIR_MAX) and getDr() and getEq(): 
        setCores("amarelo")

    elif ve_cor(VERMELHO_ESQ_MIN, VERMELHO_ESQ_MAX, VERMELHO_DIR_MIN, VERMELHO_DIR_MAX) and getDr() and getEq():
        setCores("vermelho")

    elif ve_cor(AZUL_ESQ_MIN, AZUL_ESQ_MAX, AZUL_DIR_MIN, AZUL_DIR_MAX) and getDr() and getEq():
        setCores("azul")

    ev3.speaker.beep()
    print('eu vi a cor',getCores())
    return getCores()
