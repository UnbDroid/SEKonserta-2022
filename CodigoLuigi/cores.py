from declaracoes import *

def le_sensor_cor(): #TODO como que esse valor é lido? ele é um inteiro normal? Como que eu sei qual cor que está?!
    global ValorCorEsquerda
    global ValorCorDireita

    ValorCorEsquerda = luzEsquerda.rgb() # é uma lista de 3 valores RGB
    ValorCorDireita = luzDireita.rgb()

    #print("Valor na Esquerda é:", ValorCorEsquerda, "E na direita é", ValorCorDireita)
    return


def ve_cor(eq_min, eq_max, dr_min, dr_max):
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr
    
    eq = False
    dr = False
    
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True
    
    return eq or dr



def alinha_robo(eq_min, eq_max, dr_min, dr_max):
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr

    print(ValorCorEsquerda)
    if (eq_min[0] > ValorCorEsquerda[0]  or  ValorCorEsquerda[0] > eq_max[0]) and (eq_min[1] > ValorCorEsquerda[1]  or  ValorCorEsquerda[1] > eq_max[1]) and (eq_min[2] > ValorCorEsquerda[2]  or  ValorCorEsquerda[2] > eq_max[2]): #esq não vendo borda
        while (eq_min[0] > ValorCorEsquerda[0]  or  ValorCorEsquerda[0] > eq_max[0]) and (eq_min[1] > ValorCorEsquerda[1]  or  ValorCorEsquerda[1] > eq_max[1]) and (eq_min[2] > ValorCorEsquerda[2]  or  ValorCorEsquerda[2] > eq_max[2]): #TODO ValorCorEsquerda se for maior que o mínimo e maior que o máximo?!
            rodas.drive(15,30) #direita
            le_sensor_cor()

    elif  (eq_min[0] > ValorCorDireita[0]  or  ValorCorDireita[0] > eq_max[0]) and (eq_min[1] > ValorCorDireita[1]  or  ValorCorDireita[1] > eq_max[1]) and (eq_min[2] > ValorCorDireita[2]  or  ValorCorDireita[2] > eq_max[2]): #dir vendo_preto
        while (eq_min[0] > ValorCorDireita[0]  or  ValorCorDireita[0] > eq_max[0]) and (eq_min[1] > ValorCorDireita[1]  or  ValorCorDireita[1] > eq_max[1]) and (eq_min[2] > ValorCorDireita[2]  or  ValorCorDireita[2] > eq_max[2]):
            rodas.drive(15,-30) #esquerda
            le_sensor_cor()

    rodas.stop()

    return True

def alinha_preto_re():
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr

    eq_min =[4, 6, 3]
    eq_max = [6,8,5]

    dr_min = [9, 12, 13]
    dr_max = [12,14,20] 
    
    eq = False
    dr = False
    
    if eq_min[0] < ValorCorEsquerda[0] > eq_max[0] and eq_min[1] < ValorCorEsquerda[1] > eq_max[1] and eq_min[2] < ValorCorEsquerda[2] > eq_max[2]: #esq não vendo preto
        while eq_min[0] < ValorCorEsquerda[0] > eq_max[0] and eq_min[1] < ValorCorEsquerda[1] > eq_max[1] and eq_min[2] < ValorCorEsquerda[2] > eq_max[2]:
            rodas.drive(-15,-30) #direita
            ValorCorEsquerda = luzEsquerda.rgb()
            ValorCorDireita = luzDireita.rgb()

    elif dr_min[0] < ValorCorDireita[0] > dr_max[0] and dr_min[1] < ValorCorDireita[1] > dr_max[1] and dr_min[2] < ValorCorDireita[2] > dr_max[2]: #dir vendo_preto
        while dr_min[0] < ValorCorDireita[0] > dr_max[0] and dr_min[1] < ValorCorDireita[1] > dr_max[1] and dr_min[2] < ValorCorDireita[2] > dr_max[2]:
            rodas.drive(-15,30) #esquerda
            ValorCorEsquerda = luzEsquerda.rgb()
            ValorCorDireita = luzDireita.rgb()
    rodas.stop()

    return True

def alinha_preto_frente():
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr

    eq_min =[4, 6, 3]
    eq_max = [6,8,5]

    dr_min = [9, 12, 13]
    dr_max = [12,14,20] 
    
    eq = False
    dr = False
    
    if eq_min[0] < ValorCorEsquerda[0] > eq_max[0] and eq_min[1] < ValorCorEsquerda[1] > eq_max[1] and eq_min[2] < ValorCorEsquerda[2] > eq_max[2]: #esq não vendo preto
        while eq_min[0] < ValorCorEsquerda[0] > eq_max[0] and eq_min[1] < ValorCorEsquerda[1] > eq_max[1] and eq_min[2] < ValorCorEsquerda[2] > eq_max[2]:
            rodas.drive(15,30) #direita
            ValorCorEsquerda = luzEsquerda.rgb()
            ValorCorDireita = luzDireita.rgb()

    elif dr_min[0] < ValorCorDireita[0] > dr_max[0] and dr_min[1] < ValorCorDireita[1] > dr_max[1] and dr_min[2] < ValorCorDireita[2] > dr_max[2]: #dir vendo_preto
        while dr_min[0] < ValorCorDireita[0] > dr_max[0] and dr_min[1] < ValorCorDireita[1] > dr_max[1] and dr_min[2] < ValorCorDireita[2] > dr_max[2]:
            rodas.drive(15,-30) #esquerda
            ValorCorEsquerda = luzEsquerda.rgb()
            ValorCorDireita = luzDireita.rgb()
    rodas.stop()

    return True

def identifica_cor_da_area():
    global cor_da_area 
    global ValorCorEsquerda
    global ValorCorDireita
 
    if ve_cor(AMARELO_ESQ_MIN, AMARELO_ESQ_MAX, AMARELO_DIR_MIN, AMARELO_DIR_MAX): 
        cor_da_area = "amarelo"

    if ve_cor(VERMELHO_ESQ_MIN, VERMELHO_ESQ_MAX, VERMELHO_DIR_MIN, VERMELHO_DIR_MAX):
        cor_da_area = "vermelho"

    if ve_cor(AZUL_ESQ_MIN, AZUL_ESQ_MAX, AZUL_DIR_MIN, AZUL_DIR_MAX):
        cor_da_area = "azul"
    
    return cor_da_area



