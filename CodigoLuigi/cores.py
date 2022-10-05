from declaracoes import *

def le_sensor_cor(): #TODO como que esse valor é lido? ele é um inteiro normal? Como que eu sei qual cor que está?!
    global ValorCorEsquerda
    global ValorCorDireita

    ValorCorEsquerda = luzEsquerda.rgb() # é uma lista de 3 valores RGB
    ValorCorDireita = luzDireita.rgb()

    #print("Valor na Esquerda é:", ValorCorEsquerda, "E na direita é", ValorCorDireita)
    return

def ve_branco():    # Se está vendo branco com os dois sensores retorna True, else False
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr

    eq_min =[59, 68, 64]
    eq_max = [100,100,100]

    dr_min = [82, 76, 100]
    dr_max = [100,100,100] 
    
    eq = False
    dr = False
    
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True
    
    return eq and dr

def ve_amarelo():    # Se está vendo amarelo com os dois sensores retorna True, else False
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr
    eq_min =[60, 42, 7]
    eq_max = [72,50,11]

    dr_min = [82, 49, 23]
    dr_max = [96,54,26] 
    
    eq = False
    dr = False
    
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True
    
    return eq and dr
     
def ve_vermelho():    # Se está vendo vermelho com os dois sensores retorna True, else False
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr
    eq_min =[46, 6, 2]
    eq_max = [55,10,5]

    dr_min = [64, 9, 10]
    dr_max = [73,13,16] 
    
    eq = False
    dr = False
    
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True
    
    return eq and dr

def ve_azul():    # Se está vendo azul com os dois sensores retorna True, else False
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr
    eq_min =[2, 5, 6]
    eq_max = [6,10,13]

    dr_min = [6, 9, 28]
    dr_max = [11,15,36] 
    
    eq = False
    dr = False
    
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True
    
    return eq and dr

def ve_preto():    # Se está vendo preto com algum dois sensores retorna True, else False
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
    
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True
    
    return eq or dr

def ve_borda():
    global ValorCorEsquerda
    global ValorCorDireita
    global eq #TODO o que isso significa?! esquerda?!
    global dr #TODO o que isso significa?! direita?!

    eq_min =[0,0,0] #TODO isso aqui é tipo um filtro?!
    eq_max = [0,0,0]

    dr_min = [0,0,0]
    dr_max = [0,0,0] 
    
    eq = False
    dr = False
    
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True
    
    return eq or dr

def ve_rampa():
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr

    eq_min =[2, 15, 0]
    eq_max = [6, 20, 3]

    dr_min = [2, 12, 6]
    dr_max = [8, 16, 14] 
    
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

    nao_ve_borda_sensor_esquerdo = 0
    nao_ve_borda_sensor_direita = 0


    for minEsq, maxEsq in zip (eq_min, eq_max):
        if minEsq > ValorCorEsquerda > maxEsq:
            nao_ve_borda_sensor_esquerdo += 1    

    for minDir, maxDir in zip(dr_min, dr_max):
        if minDir > ValorCorDireita > maxDir:
            nao_ve_borda_sensor_direita += 1

    
    if(nao_ve_borda_sensor_esquerdo == 3):
        while (nao_ve_borda_sensor_esquerdo == 3): 
            rodas.drive(8,15) #direita
            ValorCorEsquerda = luzEsquerda.rgb() #TODO porque aqui não usa a função de le_sensor_cor() ??
            ValorCorDireita = luzDireita.rgb()
    elif (nao_ve_borda_sensor_direita == 3):
        while(nao_ve_borda_sensor_direita == 3):
            rodas.drive(8,-15) #esquerda
            ValorCorEsquerda = luzEsquerda.rgb()
            ValorCorDireita = luzDireita.rgb()
    rodas.stop()


 #   if eq_min[0] > ValorCorEsquerda[0] > eq_max[0] and eq_min[1] < ValorCorEsquerda[1] > eq_max[1] and eq_min[2] < ValorCorEsquerda[2] > eq_max[2]: #esq não vendo borda
  #      while eq_min[0] < ValorCorEsquerda[0] > eq_max[0] and eq_min[1] < ValorCorEsquerda[1] > eq_max[1] and eq_min[2] < ValorCorEsquerda[2] > eq_max[2]: #TODO ValorCorEsquerda se for maior que o mínimo e maior que o máximo?!
   #         rodas.drive(8,15) #direita
    #        ValorCorEsquerda = luzEsquerda.rgb() #TODO porque aqui não usa a função de le_sensor_cor() ??
     #       ValorCorDireita = luzDireita.rgb()

#    elif dr_min[0] < ValorCorDireita[0] > dr_max[0] and dr_min[1] < ValorCorDireita[1] > dr_max[1] and dr_min[2] < ValorCorDireita[2] > dr_max[2]: #dir vendo_preto
 #       while dr_min[0] < ValorCorDireita[0] > dr_max[0] and dr_min[1] < ValorCorDireita[1] > dr_max[1] and dr_min[2] < ValorCorDireita[2] > dr_max[2]:
  #          rodas.drive(8,-15) #esquerda
   #         ValorCorEsquerda = luzEsquerda.rgb()
    #        ValorCorDireita = luzDireita.rgb()
    #rodas.stop()

    return True


def alinha_preto_re():
    rodas.stop()
    leitura_esq = luzEsquerda.reflection()
    leitura_dir = luzDireita.reflection()

    if leitura_esq > 20: 
        while leitura_esq > 20:
            rodaEsquerda.run(-30)
            leitura_esq = luzEsquerda.reflection()

    elif leitura_dir > 20: 
        while leitura_dir > 20:
            rodaDireita.run(-30)
            leitura_dir = luzDireita.reflection()
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
            rodas.drive(8,15) #direita
            ValorCorEsquerda = luzEsquerda.rgb()
            ValorCorDireita = luzDireita.rgb()

    elif dr_min[0] < ValorCorDireita[0] > dr_max[0] and dr_min[1] < ValorCorDireita[1] > dr_max[1] and dr_min[2] < ValorCorDireita[2] > dr_max[2]: #dir vendo_preto
        while dr_min[0] < ValorCorDireita[0] > dr_max[0] and dr_min[1] < ValorCorDireita[1] > dr_max[1] and dr_min[2] < ValorCorDireita[2] > dr_max[2]:
            rodas.drive(8,-15) #esquerda
            ValorCorEsquerda = luzEsquerda.rgb()
            ValorCorDireita = luzDireita.rgb()
    rodas.stop()

    return True

def identifica_cor_area():
    global cor_area 
    global valorCorEsquerda
    global valorCorDireita

    if ve_amarelo():
        cor_da_area = "amarelo"

    elif ve_vermelho():
        cor_da_area = "vermelho"

    elif ve_azul():
        cor_da_area = "azul"
    
    return cor_area

def valida_cor_area():
    global cor_area 
    global valorCorEsquerda
    global valorCorDireita
    angulos = [45,-45,-45]

    cores_lidas = []

    for i in range(3):
        rodas.turn(angulos[i])
        le_sensor_cor()
        cores_lidas.append(identifica_cor_area())

    for i in range(len(cores_lidas)):
        if cores_lidas[0] != cores_lidas[i]:
            cor_lida =  False
    
    return True


