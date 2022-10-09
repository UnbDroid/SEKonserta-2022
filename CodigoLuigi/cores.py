from declaracoes import *

def le_sensor_cor(): #TODO como que esse valor é lido? ele é um inteiro normal? Como que eu sei qual cor que está?!

    setValorCorEsquerda(luzEsquerda.rgb()) # é uma lista de 3 valores RGB
    setValorCorDireita(luzDireita.rgb())

    print("Valor na Esquerda é:", getValorCorEsquerda(), "E na direita é", getValorCorDireita())

    return


def ve_cor(eq_min, eq_max, dr_min, dr_max):
    valorEsquerdo = getValorCorEsquerda()
    valorDireito = getValorCorDireita()
    
    if eq_min[0] <= valorEsquerdo[0] <= eq_max[0] and eq_min[1] <= valorEsquerdo[1] <= eq_max[1] and eq_min[2] <= valorEsquerdo[2] <= eq_max[2]:
        setEq(True)
    if dr_min[0] <= valorDireito[0] <= dr_max[0] and dr_min[1] <= valorDireito[1] <= dr_max[1] and dr_min[2] <= valorDireito[2] <= dr_max[2]:
        setDr(True)
        
    return getEq() or getDr()



def alinha_robo(eq_min, eq_max, dr_min, dr_max):
    valorEsquerdo = getValorCorEsquerda()
    valorDireito = getValorCorDireita()
    corEsquerda = luzEsquerda.rgb()

    print('esta alinhando, esq: ',valorEsquerdo)

    if (eq_min[0] > valorEsquerdo[0]  or  valorEsquerdo[0] > eq_max[0]) and (eq_min[1] > valorEsquerdo[1]  or  valorEsquerdo[1] > eq_max[1]) and (eq_min[2] > valorEsquerdo[2]  or  valorEsquerdo[2] > eq_max[2]): #esq não vendo borda
        while (eq_min[0] > valorEsquerdo[0]  or  valorEsquerdo[0] > eq_max[0]) and (eq_min[1] > valorEsquerdo[1]  or  valorEsquerdo[1] > eq_max[1]) and (eq_min[2] > valorEsquerdo[2]  or  valorEsquerdo[2] > eq_max[2]): #TODO ValorCorEsquerda se for maior que o mínimo e maior que o máximo?!
            rodas.drive(15,30) #direita
            corEsquerda = luzEsquerda.rgb()
            setValorCorDireita(corEsquerda)
            valorEsquerdo = getValorCorEsquerda()
            print('corEsquerda: ',corEsquerda)
            print('lendoSensorCorEsq: ',valorEsquerdo)


    elif  (eq_min[0] > valorDireito[0]  or  valorDireito[0] > eq_max[0]) and (eq_min[1] > valorDireito[1]  or  valorDireito[1] > eq_max[1]) and (eq_min[2] > valorDireito[2]  or  valorDireito[2] > eq_max[2]): #dir vendo_preto
        while (eq_min[0] > valorDireito[0]  or  valorDireito[0] > eq_max[0]) and (eq_min[1] > valorDireito[1]  or  valorDireito[1] > eq_max[1]) and (eq_min[2] > valorDireito[2]  or  valorDireito[2] > eq_max[2]):
            rodas.drive(15,-30) #esquerda
            #le_sensor_cor()
            setValorCorDireita(luzDireita.rgb())
            valorDireito = getValorCorDireita()
            print('lendoSensorCorDir: ',valorDireito)

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

    
    if eq_min[0] < valorEsquerdo[0] > eq_max[0] and eq_min[1] < valorEsquerdo[1] > eq_max[1] and eq_min[2] < valorEsquerdo[2] > eq_max[2]: #esq não vendo preto
        while eq_min[0] < valorEsquerdo[0] > eq_max[0] and eq_min[1] < valorEsquerdo[1] > eq_max[1] and eq_min[2] < valorEsquerdo[2] > eq_max[2]:
            rodas.drive(15,30) #direita
            #le_sensor_cor()
            setValorCorEsquerda(luzEsquerda.rgb())
            valorEsquerdo = getValorCorEsquerda()
            print('em ALINHA PRETO FRENTE lendoSensorCorEsq: ',valorEsquerdo)

    elif dr_min[0] < valorDireito[0] > dr_max[0] and dr_min[1] < valorDireito[1] > dr_max[1] and dr_min[2] < valorDireito[2] > dr_max[2]: #dir vendo_preto
        while dr_min[0] < valorEsquerdo[0] > dr_max[0] and dr_min[1] < valorEsquerdo[1] > dr_max[1] and dr_min[2] < valorEsquerdo[2] > dr_max[2]:
            rodas.drive(15,-30) #esquerda
            #le_sensor_cor()
            setValorCorDireita(luzEsquerda.rgb())
            valorDireito = getValorCorDireita()
            print('em ALINHA PRETO FRENTE lendoSensorCorEsq: ',valorDireito)

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



