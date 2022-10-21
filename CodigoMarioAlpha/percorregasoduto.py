from declaracoes import *
from servidor import *
from pegatubo import *
from cores import *
from movimentacao import *

tamanho_media = 1  #Quantos valores são considerados para fazer a média das últimas n medições do ultrassom
ListaDistanciaUltrassomEsquerda = tamanho_media * [0]
ValorLuzEsquerda = 0                                                                         
DistanciaUltrassomEsquerda = 0
DistanciaUltrassomFrente = 0
valor_minimo = 5
valor_maximo = 65
tamanho_do_tubo_na_garra = 15  #Mudar para 0
lista_de_gaps = []
FIM_DO_PROGRAMA = False
TUBO_ENTREGUE = False
MEDIR_DENOVO = True

def fim_programa():   #Função feita pq não entendo ainda como funcionam as variáveis globais entre arquivos kk
    global FIM_DO_PROGRAMA
    return FIM_DO_PROGRAMA

def tubo_foi_entregue():
    global TUBO_ENTREGUE
    return TUBO_ENTREGUE

def precisa_medir():
    global MEDIR_DENOVO
    return MEDIR_DENOVO

def le_valores_percorrimento_esquerda():
    global ValorLuzEsquerda                                                                           
    global DistanciaUltrassomEsquerda
    global DistanciaUltrassomFrente
    global ValorCorEsquerda
    global ValorCorDireita
    ValorLuzEsquerda = MboxAlphaBetaLuz.read()                                                                            
    #DistanciaUltrassomEsquerda = MboxAlphaBetaUltrassom.read()
    DistanciaUltrassomEsquerda = UltrassomEsquerda.distance()
    DistanciaUltrassomFrente = UltrassomFrente.distance()
    le_sensor_cor()

def adiciona_lista_ultrassom_esquerda():
    global DistanciaUltrassomEsquerda
    if not DistanciaUltrassomEsquerda == 772550: #2550 é o valor máx e as vezes buga nele, então para elimiar ele (esse 772550 é um valor q nunca chega)
        ListaDistanciaUltrassomEsquerda.pop(0)
        ListaDistanciaUltrassomEsquerda.append(DistanciaUltrassomEsquerda)   


def checa_distancia_ultrassom_esquerda():  # Retorna True se não foi visto tubo na esquerda
    global tamanho_media
    global ListaDistanciaUltrassomEsquerda
    if (sum(ListaDistanciaUltrassomEsquerda))/tamanho_media > 150:
        return True
    else:
        return False

def checa_distancia_ultrassom_frente():
    global DistanciaUltrassomFrente
    # if DistanciaUltrassomFrente <= 140:
    if DistanciaUltrassomFrente <= 130:
        return True
    else:
        return False

def checa_luz_esquerda(a):
    global valor_minimo
    global valor_maximo
    global ValorLuzEsquerda
    if a == 'min':
        if ValorLuzEsquerda < valor_minimo:
            return True
        return False
    elif a  == 'max':
        if ValorLuzEsquerda > valor_maximo:
            return True
        return False

def le_valores_max_min():
    global valor_maximo
    global valor_minimo
    MboxAlphaBetaLuz.wait()  # Esperando o valor mínimo
    valor_minimo = MboxAlphaBetaLuz.read()  
    print(valor_minimo)    
    MboxAlphaBetaLuz.wait() # Esperando o valor máximo
    valor_maximo = MboxAlphaBetaLuz.read()  
    print(valor_minimo)

def define_tamanho_gap():
    global distancia_percorrida
    if distancia_percorrida <= 50: #Não é GAP, só um buraquinho do gasoduto msm
        return False
    elif distancia_percorrida <= 101: # GAP - 10 cm 110
        print("É um buraco de 10 cm!, Foi Medido:", distancia_percorrida)
        ev3.speaker.beep(200, 700)
        return 10
    elif distancia_percorrida <= 151: #GAP - 15 cm  160
        print("É um buraco de 15 cm!, Foi Medido:", distancia_percorrida)
        ev3.speaker.beep(500, 700)
        wait(300)
        ev3.speaker.beep(500, 700)
        return 15
    elif distancia_percorrida <= 240:# GAP - 20 cm 225
        print("É um buraco de 20 cm!, Foi Medido:", distancia_percorrida)
        ev3.speaker.beep(800, 700)
        wait(300)
        ev3.speaker.beep(800, 700)
        wait(300)
        ev3.speaker.beep(800, 700)
        return 20
    return False

def coloca_tubo(tamanho):
    global distancia_percorrida
    global condition
    robot.stop()
    if False: #condition:  #Se a condição é verdadeira, ele parou de ler o buraco durante a curva
            pass

    else:
        watch.reset()
        if tamanho == 10:
            while watch.time()<1500:
                robot.drive(-55, -60)     #-48, 60
        elif tamanho == 15:
            while watch.time()<1500:
                robot.drive(-81, -60)      # -81, -60
        elif tamanho == 20:
            while watch.time()<1500:
                robot.drive(-104, -60)    # -96, -60
        robot.stop()
        posiciona_gasoduto()
        devolve_tubo(tamanho)

def anda_re_gasoduto():
    global valor_minimo
    global valor_maximo
    robot.stop()
    #ev3.speaker.beep(700,6000)
    while checa_distancia_ultrassom_esquerda():
        print('entrei')
        le_valores_percorrimento_esquerda()
        adiciona_lista_ultrassom_esquerda()
        if checa_luz_esquerda('max'):
            robot.drive(-20, 2)
        elif checa_luz_esquerda('min'):
            robot.drive(-20,-2)
        else:
            robot.drive(-20,0)
    robot.stop()
    #ev3.speaker.beep(700,6000)


def virada_gasoduto_esquerda():
    global MEDINDO
    if MEDINDO:
        robot.drive(40, -14)
    else:
        robot.drive(50, -16)         #50,-16
        # robot.drive(100, -34)
        # robot.drive(75, -25)

def virada_gasoduto_direita():
    global MEDINDO
    if MEDINDO:
        robot.drive(40,16)
    else:
        robot.drive(50, 20)       #50,20
        # robot.drive(100,40)
        # robot.drive(75,30)

def segue_reto_gasoduto():
    global MEDINDO
    if MEDINDO:
        robot.drive(40,0)
    else:
        robot.drive(50,0)    #50,0
        # robot.drive(75,0)
        # robot.drive(100,0)
    

def virada_ultrassom_frente():
    robot.stop()
    watch.reset()
    # while watch.time()<3000:
    #     robot.drive(4, 29)   #5, 29  - 3 segundos
    # while watch.time() < 1500:
    #     robot.drive(8, 59)        
    while watch.time() < 1500:
        robot.drive(4,59)


def virada_ultrassom_frente_medindo_gap(): #Faz a virada mas continua medindo o tamanho do GAP 
    global condition
    global distancia_percorrida
    global distancia_na_curva
    global distancia_da_re
    robot.stop()
    print("Distância (parou na curva):", robot.distance(), "Distancia na curva:", distancia_na_curva)
    ev3.speaker.beep(50,100)
    wait(100)
    ev3.speaker.beep(500,100)
    wait(100)
    ev3.speaker.beep(950,100)
    wait(100)
    distancia = UltrassomFrente.distance()
    distancia_auxiliar = robot.distance()
    while distancia >= 40 and checa_distancia_ultrassom_esquerda() :
        distancia = UltrassomFrente.distance()
        le_valores_percorrimento_esquerda()
        adiciona_lista_ultrassom_esquerda()
        print(distancia)
        robot.drive(30,0)
    robot.stop()
    distancia_percorrida = robot.distance()
    condition = True
    distancia_auxiliar -= robot.distance()
    distancia_da_re = distancia_auxiliar # ele só vai dar essa ré depois que devolver o tubo, caso ele precise
    #robot.straight(distancia_auxiliar)
    robot.stop()
    ev3.speaker.beep(50,500)
    #virada_ultrassom_frente()
    robot.stop()
    le_valores_percorrimento_esquerda()
    #watch.reset()

    # condition = False
    # while watch.time()<3000:
    #     robot.drive(5, 29)
    #     if not (checa_distancia_ultrassom_esquerda() and condition): #Se ele parar de ver o cano no meio da curva

    #         print("Distância (parou na curva):", robot.distance(), "Distancia na curva:", distancia_na_curva)
    #         distancia_percorrida = robot.distance()
    #         robot.stop()
    #         ev3.speaker.beep(50,900)
    #         condition = True

def mede_tamanho_gap():
    global distancia_percorrida
    global distancia_na_curva
    global condition
    global MEDINDO
    condition = False # Essa condição só se torna verdadeira quando o robô para de ler a ausência de tubo durante a curva
    MEDINDO = True
    distancia_auxiliar = 0
    distancia_na_curva = 0 # Se a maior parte da distancia lida foi em uma curva, significa q n era um gap mas sim um joelho mal colocado
    robot.reset()
    while checa_distancia_ultrassom_esquerda():
        le_valores_percorrimento_esquerda()
        adiciona_lista_ultrassom_esquerda()
        if checa_luz_esquerda('max'): # Modo Luz Ambient -> max     Reflection -> min
            distancia_auxiliar = robot.distance()
            virada_gasoduto_esquerda()
            #segue_reto_gasoduto()
            distancia_na_curva += robot.distance() - distancia_auxiliar
        elif checa_distancia_ultrassom_frente():
            virada_ultrassom_frente_medindo_gap()
            break
        elif checa_luz_esquerda('min'): # Modo Luz Ambient -> min        Reflection -> max
            virada_gasoduto_direita()
            #segue_reto_gasoduto()
        else:
            segue_reto_gasoduto()
    if not condition:
        print("Distancia: ",robot.distance(), "Distancia na curva:", distancia_na_curva)
        #ev3.speaker.beep(200)
        distancia_percorrida = robot.distance()
        robot.stop()

def mede_tamanho_gap_com_re():
    global distancia_percorrida
    global distancia_na_curva
    global condition
    global MEDINDO
    condition = False # Essa condição só se torna verdadeira quando o robô para de ler a ausência de tubo durante a curva
    MEDINDO = True
    distancia_auxiliar = 0
    distancia_na_curva = 0 # Se a maior parte da distancia lida foi em uma curva, significa q n era um gap mas sim um joelho mal colocado
    anda_re_gasoduto()
    robot.reset()
    robot.straight(50)
    while checa_distancia_ultrassom_esquerda():
        le_valores_percorrimento_esquerda()
        adiciona_lista_ultrassom_esquerda()
        if checa_luz_esquerda('max'): # Modo Luz Ambient -> max     Reflection -> min
            distancia_auxiliar = robot.distance()
            virada_gasoduto_esquerda()
            #segue_reto_gasoduto()
            distancia_na_curva += robot.distance() - distancia_auxiliar
        elif checa_distancia_ultrassom_frente():
            virada_ultrassom_frente_medindo_gap()
        elif checa_luz_esquerda('min'): # Modo Luz Ambient -> min        Reflection -> max
            virada_gasoduto_direita()
            #segue_reto_gasoduto()
        else:
            segue_reto_gasoduto()
    if not condition:
        print("Distancia: ",robot.distance(), "Distancia na curva:", distancia_na_curva)
        #ev3.speaker.beep(200)
        distancia_percorrida = robot.distance()
        robot.stop()

def percorre_gasoduto_esquerda(modo = 'ignorar'):  #Percorre o gasoduto do modo sem varredura completa

    #IF modo ==  'ignorar' -> Percorrer o gasoduto até o final medindo os GAPs mas "ignorando" eles
    #IF modo ==  'medir' -> Percorrer o gasoduto até o primeiro GAP, e após achá-lo, ir buscar o tubo
    #IF modo == 'entregar' -> Percorrer o gasoduto até o primeiro GAP, e após achá-lo, colocar ele no local e após isso continuar o percorrimento do modo 'medir'
    global ValorLuzEsquerda                                                                           
    global DistanciaUltrassomEsquerda
    global DistanciaUltrassomFrente
    global ValorCorEsquerda
    global ValorCorDireita
    global valor_minimo
    global valor_maximo
    global distancia_percorrida
    global distancia_na_curva
    global condition
    global tamanho_do_tubo_na_garra
    global tamanho_do_tubo_espera
    global distancia_da_re
    global FIM_DO_PROGRAMA
    global TUBO_ENTREGUE
    global MEDIR_DENOVO
    global MEDINDO
    TUBO_ENTREGUE = False
    primeira_vez = True #Esse valor só deixa de ser True quando o Mario passa por um gap de um tamanho diferente do tamanho do tubo que está na garra
    MEDIR_DENOVO = True # Só se torna False quando o Mario está com um tubo na garra, passa por um gap de tamanho diferente x, segue o gasoduto e acha um gap do tamanho do tubo e o entrega. após isso ele já vai buscar um tubo de tamanho x portanto não precisa medir o gasoduto novamente
    DEU_RE = False # Robô dar ré uma vez quando ve um tubo, e depois que der a ré muda para True, para não dar ré infinita
    print('entrei no percorrimento')
    MboxAlphaBeta.send("PercorrimentoGasodutoEsquerda")
    print('mandei')
    #tamanho_do_tubo_espera = 0 ############################# teste ################################
    le_valores_max_min()
    valor_minimo = 14 #De manhã deu 58, 12h deu 75 --- 48
    valor_maximo = 22  #De manhã deu 72, 12h deu 88 -- 58
    MboxAlphaBetaLuz.wait()
    #watch_re.reset()
    watch_medida.reset()
    while True:
        MEDINDO = False
        manda_nada_luigi()
        le_valores_percorrimento_esquerda()
        adiciona_lista_ultrassom_esquerda()
        # if watch_re.time() < 3000: # Pra ele andar devagar logo depois de dar ré
        #     MEDINDO = True
        #print('Luz Esq',ValorLuzEsquerda, 'Ult Esq', DistanciaUltrassomEsquerda, 'ult frente', DistanciaUltrassomFrente)
        if viu_beirada():
            robot.stop()
            ev3.speaker.beep(900, 1000)
            robot.stop()
            if modo == 'medir' or (modo == 'entregar' and not tamanho_do_tubo_espera):
                FIM_DO_PROGRAMA = True  #Se ele estiver medindo e chegar até o fim do gasoduto, finalizar o programa
                print(FIM_DO_PROGRAMA)
            if modo == 'entregar': # Se ele chegar ao fim do programa com um tubo para ser entregue, devolver o tubo ao Luigi
                alinha_beirada()
                robot.stop()
                manda_mensagem_luigi(tamanho_do_tubo_espera, tamanho_do_tubo_na_garra)
                devolve_tubo_ao_Luigi(tamanho_do_tubo_na_garra, tamanho_do_tubo_espera)
                tamanho_do_tubo_na_garra = tamanho_do_tubo_espera
            break
        elif checa_luz_esquerda('max'): # Modo Luz Ambient -> max       Reflection -> min (ambient de dia, reflection de noite)
            virada_gasoduto_esquerda()
           # segue_reto_gasoduto()
        elif checa_distancia_ultrassom_frente():
            virada_ultrassom_frente()
        elif checa_distancia_ultrassom_esquerda() and watch_medida.time() > 1500:
            ev3.speaker.beep(50)
            # if watch_re.time() > 3000: # Ele só da ré se não tiver dado ré nos últimos x milisegundos
            #     anda_re_gasoduto()
            #     watch_re.reset()
            mede_tamanho_gap()
            tamanho_gap = define_tamanho_gap()
            if tamanho_gap: #Se foi realmente visto um gap, ou era só uma aberturazinha
                robot.stop()
                if modo == 'ignorar':
                    pass
                elif modo == 'medir':
                    manda_mensagem_luigi(tamanho_gap, 'Nada')
                    busca_tubo_em_cima(tamanho_gap)
                    tamanho_do_tubo_na_garra = tamanho_gap
                    break
                elif modo == 'entregar':
                    print('o tamanho do gap é:', tamanho_gap, 'o tamanho do tubo na garra é:',tamanho_do_tubo_na_garra)
                    if tamanho_gap == tamanho_do_tubo_na_garra:  # Se o tamanho do GAP encontrado for igual ao do tubo que está na garra
                        coloca_tubo(tamanho_gap)
                        reposiciona_gasoduto()
                        tamanho_do_tubo_na_garra = 0
                        TUBO_ENTREGUE = True
                        if not primeira_vez: # Se ele já tinha passado por um gap de outro tamanho antes de entregar, ele vai buscar um tubo desse tamanho
                            manda_mensagem_luigi(tamanho_do_tubo_espera, 'Nada')
                            print('cheguei aqui')
                            busca_tubo_em_cima(tamanho_do_tubo_espera)
                            tamanho_do_tubo_na_garra = tamanho_do_tubo_espera   
                            MEDIR_DENOVO = False
                            robot.stop()
                            gasoduto_apos_pegar_tubo()
                            TUBO_ENTREGUE =  False # ele já buscou outro e vai entregar
                        break
                    else:
                        if primeira_vez:
                            tamanho_do_tubo_espera = tamanho_gap # Esse vai ser o tamanho do próximo tubo a ser pego pelo Mario
                            primeira_vez = False
                        pass # Se o tamanho do GAP encontrada for diferente ao do tubo que está na garra
            
            if condition: #girar os 90° caso ele termine de ver o gap na curva/dar a ré depois
                robot.straight(2*distancia_da_re)
                # virada_ultrassom_frente()
        elif checa_luz_esquerda('min'):# Modo Luz Ambient -> min        Reflection -> max
            virada_gasoduto_direita()
            #segue_reto_gasoduto()
        else:
            segue_reto_gasoduto()

def percorre_gasoduto_esquerda_com_varredura_completa(modo = 'varredura'):  #Percorre o gasoduto do modo sem varredura completa

    #IF modo ==  'varredura' -> Percorrer o gasoduto até o final medindo os GAPs e adicionando na lista de GAPS
    #IF modo == 'entregar' -> Percorrer o gasoduto até o primeiro GAP, e após achá-lo, colocar ele no local e após isso continuar o percorrimento do modo 'medir'
    global ValorLuzEsquerda                                                                           
    global DistanciaUltrassomEsquerda
    global DistanciaUltrassomFrente
    global ValorCorEsquerda
    global ValorCorDireita
    global valor_minimo
    global valor_maximo
    global distancia_percorrida
    global distancia_na_curva
    global condition
    global tamanho_do_tubo_na_garra
    global tamanho_do_tubo_espera
    global FIM_DO_PROGRAMA
    global TUBO_ENTREGUE
    global MEDIR_DENOVO
    TUBO_ENTREGUE = False
    primeira_vez = True #Esse valor só deixa de ser True quando o Mario passa por um gap de um tamanho diferente do tamanho do tubo que está na garra
    MEDIR_DENOVO = True # Só se torna False quando o Mario está com um tubo na garra, passa por um gap de tamanho diferente x, segue o gasoduto e acha um gap do tamanho do tubo e o entrega. após isso ele já vai buscar um tubo de tamanho x portanto não precisa medir o gasoduto novamente
    print('entrei no percorrimento')
    MboxAlphaBeta.send("PercorrimentoGasodutoEsquerda")
    print('mandei')
    le_valores_max_min()
    valor_minimo = 777 #De manhã deu 58, 12h deu 75 --- 48
    valor_maximo = 1111 #De manhã deu 72, 12h deu 88 -- 58
    MboxAlphaBetaLuz.wait()

    while True:
        MEDINDO = True
        manda_nada_luigi()
        le_valores_percorrimento_esquerda()
        adiciona_lista_ultrassom_esquerda()
        #print('Luz Esq',ValorLuzEsquerda, 'Ult Esq', DistanciaUltrassomEsquerda, 'ult frente', DistanciaUltrassomFrente)
        if viu_beirada():
            robot.stop()
            ev3.speaker.beep(900, 1000)
            robot.stop()
            if modo == 'varredura' and not lista_de_gaps: # Se a lista_de_gaps estiver vazia
                FIM_DO_PROGRAMA = True  #Se ele estiver medindo e chegar até o fim do gasoduto, finalizar o programa
                print(FIM_DO_PROGRAMA)
            break
        elif checa_luz_esquerda('max'): # Modo Luz Ambient -> max       Reflection -> min (ambient de dia, reflection de noite)
            virada_gasoduto_esquerda()
        elif checa_distancia_ultrassom_frente():
            virada_ultrassom_frente()
        elif checa_distancia_ultrassom_esquerda():
            ev3.speaker.beep(50)
            mede_tamanho_gap()
            tamanho_gap = define_tamanho_gap()
            if tamanho_gap: #Se foi realmente visto um gap, ou era só uma aberturazinha
                if modo == 'varredura':
                    lista_de_gaps.insert(0,tamanho_gap)
                    break
                elif modo == 'entregar':
                    print('o tamanho do gap é:', tamanho_gap, 'o tamanho do tubo na garra é:',tamanho_do_tubo_na_garra)
                    if tamanho_gap == tamanho_do_tubo_na_garra:  # Se o tamanho do GAP encontrado for igual ao do tubo que está na garra
                        coloca_tubo(tamanho_gap)
                        reposiciona_gasoduto()
                        tamanho_do_tubo_na_garra = 0
                        TUBO_ENTREGUE = True
                        if not primeira_vez: # Se ele já tinha passado por um gap de outro tamanho antes de entregar, ele vai buscar um tubo desse tamanho
                            manda_mensagem_luigi(tamanho_do_tubo_espera, 'Nada')
                            print('cheguei aqui')
                            busca_tubo_em_cima(tamanho_do_tubo_espera)
                            tamanho_do_tubo_na_garra = tamanho_do_tubo_espera   
                            MEDIR_DENOVO = False
                            robot.stop()
                            ev3.speaker.beep(100,2000)
                            gasoduto_apos_pegar_tubo()
                            TUBO_ENTREGUE =  False # ele já buscou outro e vai entregar
                        break
                    else:
                        if primeira_vez:
                            tamanho_do_tubo_espera = tamanho_gap # Esse vai ser o tamanho do próximo tubo a ser pego pelo Mario
                            primeira_vez = False
                        pass # Se o tamanho do GAP encontrada for diferente ao do tubo que está na garra
        elif checa_luz_esquerda('min'):# Modo Luz Ambient -> min        Reflection -> max
            virada_gasoduto_direita()
        else:
            segue_reto_gasoduto()


    