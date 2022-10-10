from declaracoes import *

def le_sensor_cor(): #TODO como que esse valor é lido? ele é um inteiro normal? Como que eu sei qual cor que está?!

    setValorCorEsquerda(luzEsquerda.rgb()) # é uma lista de 3 valores RGB
    setValorCorDireita(luzDireita.rgb())

    # print("[LE SENSOR] Valor na Esquerda é:", getValorCorEsquerda(), "E na direita é", getValorCorDireita())

    return

def valor_no_intervalo_ve_cor(min, max, valor):
    pos0_fora = min[0] <= valor[0] <= max[0]
    pos1_fora = min[0] <= valor[0] <= max[0]
    pos2_fora = min[0] <= valor[0] <= max[0]
    print('borda:', pos0_fora)
    print('borda:', pos1_fora)
    print('borda:', pos2_fora)
    return pos0_fora and pos1_fora and pos2_fora


def ve_cor(eq_min, eq_max, dr_min, dr_max):
    valorEsquerdo = getValorCorEsquerda()
    valorDireito = getValorCorDireita()
    
    if valor_no_intervalo_ve_cor(eq_min, eq_max, valorEsquerdo):
        setEq(True)
    if valor_no_intervalo_ve_cor(dr_min, dr_max, valorDireito):
        setDr(True)
        
    return getEq() or getDr()



def valor_fora_do_intervalo(min, max, val):
    pos0_fora = min[0] > val[0] or val[0] > max[0]
    pos1_fora = min[1] > val[1] or val[1] > max[1]
    pos2_fora = min[2] > val[2] or val[2] > max[2]
    print(pos0_fora)
    print(pos1_fora)
    print(pos2_fora)
    return pos0_fora or pos1_fora or pos2_fora

def valor_no_intervalo(min, max, val):
    pos0_fora = min[0] < val[0] < max[0]
    pos1_fora = min[1] < val[1] < max[1]
    pos2_fora = min[2] < val[2] < max[2] 
    print(pos0_fora)
    print(pos1_fora)
    print(pos2_fora)
    return pos0_fora or pos1_fora or pos2_fora

def alinha_robo(eq_min, eq_max, dr_min, dr_max):
    valorEsquerdo = getValorCorEsquerda()
    valorDireito = getValorCorDireita()
    corEsquerda = luzEsquerda.rgb()

    # RAMPA_DIREITO_MIN_ = [2, 9, 3]
    # RAMPA_DIREITO_MAX = [15, 22, 15] 

    print('esta alinhando, esq: ',valorEsquerdo)
    
    if(valor_no_intervalo(eq_min, eq_max, valorEsquerdo)):
        print("entrei no if do valor no intervalo")
        while(valor_fora_do_intervalo(dr_min, dr_max, valorDireito)):
            rodas.drive(15,-30) #direita
            setValorCorDireita(luzDireita.rgb())
            valorDireito = getValorCorDireita()
            print('lendoSensorCorDir: ',valorDireito)

    if (valor_no_intervalo(dr_min, dr_max, valorDireito)):
        print("entrei no if do valor no intervalo")
        #dir vendo_preto
        while valor_fora_do_intervalo(eq_min, eq_max, valorEsquerdo):
            rodas.drive(15,30) #esquerda
            #le_sensor_cor()
            setValorCorEsquerda(luzEsquerda.rgb())
            valorEsquerdo = getValorCorEsquerda()
            print('lendoSensorCorEsq: ',valorEsquerdo)

    # if  eq_min[0] < valorEsquerdo[0] > eq_max[0] and eq_min[1] < valorEsquerdo[1] > eq_max[1] and eq_min[2] < valorEsquerdo[2] > eq_max[2]: #esq não vendo borda
    #     while  eq_min[0] < valorEsquerdo[0] > eq_max[0] and eq_min[1] < valorEsquerdo[1] > eq_max[1] and eq_min[2] < valorEsquerdo[2] > eq_max[2]: #TODO ValorCorEsquerda se for maior que o mínimo e maior que o máximo?!
    #         rodas.drive(15,30) #direita
    #         setValorCorEsquerda(luzEsquerda.rgb())
    #         valorEsquerdo = getValorCorEsquerda()
    #         print('corEsquerda: ',corEsquerda)
    #         print('lendoSensorCorEsq: ',valorEsquerdo)

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
            print("Valor na Esquerda é:", valorEsquerdo, "E na direita é", valorDireito)

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
            rodas.drive(15,30) #direita
            setValorCorDireita(luzDireita.rgb())
            valorDireito = getValorCorDireita()
            print('em ALINHA PRETO FRENTE lendoSensorCorDireita: ',valorDireito)

    if (valor_no_intervalo(eq_min, eq_max, valorDireito)):
        print("AlinhaPretoFrente entrei no if do valor no intervalo")
        #dir vendo_preto
        while valor_fora_do_intervalo(eq_min, eq_max, valorEsquerdo):
            rodas.drive(15,-30) #esquerda
            #le_sensor_cor()
            setValorCorEsquerda(luzEsquerda.rgb())
            valorEsquerdo = getValorCorEsquerda()
            print('em ALINHA PRETO FRENTE lendoSensorCorEsq: ',valorEsquerdo)

    rodas.stop()
    return True

def segue_linha_sensor_esquerdo_prop(DRIVE_SPEED):
    PRETO = 8
    
    threshold = 50
    PROPORTIONAL_GAIN = 1.5

    leitura_sensor = luzEsquerda.reflection()
    #print(leitura_sensor)
    
    deviation =  threshold - leitura_sensor 
    turn_rate = PROPORTIONAL_GAIN * deviation
    rodas.drive(DRIVE_SPEED, turn_rate)

def segue_linha_sensor_direito_prop(DRIVE_SPEED):
    PRETO = 15
    
    threshold = 75
    PROPORTIONAL_GAIN = 1

    leitura_sensor = luzDireita.reflection()
    #print(leitura_sensor)
    
    deviation =  leitura_sensor - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    rodas.drive(DRIVE_SPEED, turn_rate)



