from declaracoes import *

tamanho_lista_leituras_cor = 50
lista_ultimasLeiturasDireita = tamanho_lista_leituras_cor * [3]
lista_ultimasLeiturasEsquerda = tamanho_lista_leituras_cor * [3]


#Cores em RGB:

#Branco: Esquerdo (31-37, 40-45, 40-43)  Direito (18-21, 28-31, 38-42)
#Verde (Saindo do Branco): Esquerdo (0-2, 5-7, 0-1) Direita (0-1, 4-6, 0-1)
#Preto Esquerdo (3,3,2-3) Direita ()

#ValorCorEsquerda = 0
#ValorCorDireita = 0

def le_sensor_cor():
    global ValorCorEsquerda
    global ValorCorDireita
    global lista_ultimasLeiturasDireita
    global lista_ultimasLeiturasEsquerda
    ValorCorEsquerda = SensorCorEsquerda.reflection()
    ValorCorDireita = SensorCorDireita.reflection()
    lista_ultimasLeiturasDireita.pop(0)
    lista_ultimasLeiturasDireita.append(ValorCorDireita)
    lista_ultimasLeiturasEsquerda.pop(0)
    lista_ultimasLeiturasEsquerda.append(ValorCorEsquerda)  
    return


def viu_verde():
    global lista_ultimasLeiturasDireita
    global lista_ultimasLeiturasEsquerda
    verde_eq = [4,5]
    verde_dr = [3,4]
    num_identifica_verde = 2
    contador_dr = 0
    contador_eq = 0
    for i in lista_ultimasLeiturasDireita[-num_identifica_verde:]:
        if i in verde_dr:
            contador_dr +=1
        else:
            break
    for j in lista_ultimasLeiturasEsquerda[-num_identifica_verde:]:
        if j in verde_eq:
            contador_eq +=1
        else:
            break
    
    if contador_dr == num_identifica_verde and contador_eq == num_identifica_verde:
        return [True, 'Ambos']#, lista_ultimasLeiturasDireita[-num_identifica_verde:],lista_ultimasLeiturasEsquerda[-num_identifica_verde:]]
    elif contador_dr == num_identifica_verde:
        return [True, 'D'] 
    elif contador_eq == num_identifica_verde:
        return [True, 'E'] 
    else: 
        return [False, '']


def viu_azul():
    global lista_ultimasLeiturasDireita
    global lista_ultimasLeiturasEsquerda
    azul_eq = [2,3]
    azul_dr = [1,2]
    num_identifica_azul = 2
    contador_dr = 0
    contador_eq = 0
    for i in lista_ultimasLeiturasDireita[-num_identifica_azul:]:
        if i in azul_dr:
            contador_dr +=1
        else:
            break
    for j in lista_ultimasLeiturasEsquerda[-num_identifica_azul:]:
        if j in azul_eq:
            contador_eq +=1
        else:
            break
    
    if contador_dr == num_identifica_azul and contador_eq == num_identifica_azul:
        return [True, 'Ambos']#, lista_ultimasLeiturasDireita[-num_identifica_azul:],lista_ultimasLeiturasEsquerda[-num_identifica_azul:]]
    elif contador_dr == num_identifica_azul:
        return [True, 'D'] 
    elif contador_eq == num_identifica_azul:
        return [True, 'E'] 
    else: 
        return [False, '']

def viu_branco():
    global lista_ultimasLeiturasDireita
    global lista_ultimasLeiturasEsquerda
    branco_eq = [30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
    branco_dr = [23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43]
    num_identifica_branco = 2
    contador_dr = 0
    contador_eq = 0
    for i in lista_ultimasLeiturasDireita[-num_identifica_branco:]:
        if i in branco_dr:
            contador_dr +=1
        else:
            break
    for j in lista_ultimasLeiturasEsquerda[-num_identifica_branco:]:
        if j in branco_eq:
            contador_eq +=1
        else:
            break
    
    if contador_dr == num_identifica_branco and contador_eq == num_identifica_branco:
        return [True, 'Ambos']#, lista_ultimasLeiturasDireita[-num_identifica_branco:],lista_ultimasLeiturasEsquerda[-num_identifica_branco:]]
    elif contador_dr == num_identifica_branco:
        return [True, 'D'] 
    elif contador_eq == num_identifica_branco:
        return [True, 'E'] 
    else: 
        return [False, '']

def viu_beirada():
    global lista_ultimasLeiturasDireita
    global lista_ultimasLeiturasEsquerda
    beirada_eq = [0]
    beirada_dr = [0]
    num_identifica_beirada = 1
    contador_dr = 0
    contador_eq = 0
    for i in lista_ultimasLeiturasDireita[-num_identifica_beirada:]:
        if i in beirada_dr:
            contador_dr +=1
        else:
            break
    for j in lista_ultimasLeiturasEsquerda[-num_identifica_beirada:]:
        if j in beirada_eq:
            contador_eq +=1
        else:
            break
    
    if contador_dr == num_identifica_beirada and contador_eq == num_identifica_beirada:
        return [True, 'Ambos']#, lista_ultimasLeiturasDireita[-num_identifica_beirada:],lista_ultimasLeiturasEsquerda[-num_identifica_beirada:]]
    elif contador_dr == num_identifica_beirada:
        return [True, 'D'] 
    elif contador_eq == num_identifica_beirada:
        return [True, 'E'] 
    else: 
        return [False, '']

def viu_preto():
    global lista_ultimasLeiturasDireita
    global lista_ultimasLeiturasEsquerda
    preto_eq = [5]
    preto_dr = [4]
    num_identifica_preto = 3
    contador_dr = 0
    contador_eq = 0
    for i in lista_ultimasLeiturasDireita[-num_identifica_preto:]:
        if i in preto_dr:
            contador_dr +=1
        else:
            break
    for j in lista_ultimasLeiturasEsquerda[-num_identifica_preto:]:
        if j in preto_eq:
            contador_eq +=1
        else:
            break
    
    if contador_dr == num_identifica_preto and contador_eq == num_identifica_preto:
        return [True, 'Ambos']#, lista_ultimasLeiturasDireita[-num_identifica_preto:],lista_ultimasLeiturasEsquerda[-num_identifica_preto:]]
    elif contador_dr == num_identifica_preto:
        return [True, 'D'] 
    elif contador_eq == num_identifica_preto:
        return [True, 'E'] 
    else: 
        return [False, '']

def teste():
    global ValorCorEsquerda
    global ValorCorDireita
    azul = viu_azul()
    le_sensor_cor()
    print(azul)
    while azul[0]:
        le_sensor_cor()
        print("Valor na Esquerda é:", ValorCorEsquerda, "E na direita é", ValorCorDireita)
        azul = viu_azul()
        print(azul)
        robot.drive(100,0)
    print("acabou")
