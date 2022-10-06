from declaracoes import *

def le_sensor_cor():
    global ValorCorEsquerda
    global ValorCorDireita

    ValorCorEsquerda = luzEsquerda.rgb()
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

    dr_min = [82, 46, 23]
    dr_max = [96,54,30] 
    
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
    eq_max = [9,13,5]

    dr_min = [7, 12, 13]
    dr_max = [15,19,20] 
    
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
    global eq
    global dr

    eq_min =[0,0,0]
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

    eq_min =[0, 14, 0]
    eq_max = [6, 20, 3]

    dr_min = [1, 12, 6]
    dr_max = [8, 17, 14] 
    
    eq = False
    dr = False
    
    if eq_min[0] <= ValorCorEsquerda[0] <= eq_max[0] and eq_min[1] <= ValorCorEsquerda[1] <= eq_max[1] and eq_min[2] <= ValorCorEsquerda[2] <= eq_max[2]:
        eq = True
    if dr_min[0] <= ValorCorDireita[0] <= dr_max[0] and dr_min[1] <= ValorCorDireita[1] <= dr_max[1] and dr_min[2] <= ValorCorDireita[2] <= dr_max[2]:
        dr = True

    return eq or dr

def alinha_borda():
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr

    eq_min =[0,0,0]
    eq_max = [0,0,0]

    dr_min = [0,0,0]
    dr_max = [0,0,0] 

    if eq_min[0] > ValorCorEsquerda[0] > eq_max[0] and eq_min[1] > ValorCorEsquerda[1] > eq_max[1] and eq_min[2] > ValorCorEsquerda[2] > eq_max[2]: #esq não vendo preto
        while eq_min[0] > ValorCorEsquerda[0] > eq_max[0] and eq_min[1] > ValorCorEsquerda[1] > eq_max[1] and eq_min[2] > ValorCorEsquerda[2] > eq_max[2]:
            rodas.drive(8,15) #direita
            ValorCorEsquerda = luzEsquerda.rgb()
            ValorCorDireita = luzDireita.rgb()

    elif dr_min[0] > ValorCorDireita[0] > dr_max[0] and dr_min[1] > ValorCorDireita[1] > dr_max[1] and dr_min[2] > ValorCorDireita[2] > dr_max[2]: #dir vendo_preto
        while dr_min[0] < ValorCorDireita[0] > dr_max[0] and dr_min[1] < ValorCorDireita[1] > dr_max[1] and dr_min[2] < ValorCorDireita[2] > dr_max[2]:
            rodas.drive(8,-15) #esquerda
            ValorCorEsquerda = luzEsquerda.rgb()
            ValorCorDireita = luzDireita.rgb()
    rodas.stop()


    return True

def alinha_rampa():
    global ValorCorEsquerda
    global ValorCorDireita
    global eq
    global dr

    eq_min =[2, 15, 0]
    eq_max = [6, 20, 3]

    dr_min = [2, 12, 6]
    dr_max = [8, 16, 14] 


    if eq_min[0] > ValorCorEsquerda[0] > eq_max[0] and eq_min[1] > ValorCorEsquerda[1] > eq_max[1] and eq_min[2] > ValorCorEsquerda[2] > eq_max[2]: #esq não vendo preto
        while eq_min[0] > ValorCorEsquerda[0] > eq_max[0] and eq_min[1] > ValorCorEsquerda[1] > eq_max[1] and eq_min[2] > ValorCorEsquerda[2] > eq_max[2]:
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
            rodas.drive(-8,-15) #direita
            ValorCorEsquerda = luzEsquerda.rgb()
            ValorCorDireita = luzDireita.rgb()

    elif dr_min[0] < ValorCorDireita[0] > dr_max[0] and dr_min[1] < ValorCorDireita[1] > dr_max[1] and dr_min[2] < ValorCorDireita[2] > dr_max[2]: #dir vendo_preto
        while dr_min[0] < ValorCorDireita[0] > dr_max[0] and dr_min[1] < ValorCorDireita[1] > dr_max[1] and dr_min[2] < ValorCorDireita[2] > dr_max[2]:
            rodas.drive(-8,-15) #esquerda
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

def identifica_cor_da_area():
    global cor_da_area 
    global ValorCorEsquerda
    global ValorCorDireita
 
    if ve_amarelo(): 
        cor_da_area = "amarelo"

    if ve_vermelho():
        cor_da_area = "vermelho"

    if ve_azul():
        cor_da_area = "azul"
    
    return cor_da_area



