from declaracoes import *

server = BluetoothMailboxServer()
MboxAlphaBeta = TextMailbox('alphabeta', server)
MboxAlphaBetaLuz = NumericMailbox('alphabetaluz', server)
MboxAlphaBetaUltrassom =  NumericMailbox('alphabetaultrassom', server)
MboxAlphaLuigiConfirmacao = TextMailbox('alphaluigi', server)
MboxAlphaLuigiCores = TextMailbox('alphaluigi2',server)

def conecta_alpha_beta():

    # The server must be started before the client!
    print('waiting for connection...')
    server.wait_for_connection()
    print('connected!')

    # In this program, the server waits for the client to send the first message
    # and then sends a reply.
    MboxAlphaBeta.wait()
    print(MboxAlphaBeta.read())
    MboxAlphaBeta.send('hello to you!')


def conecta_alpha_luigi():

        # The server must be started before the client!
    print('waiting for connection...')
    server.wait_for_connection()
    print('connected!')

    # In this program, the server waits for the client to send the first message
    # and then sends a reply.
    MboxAlphaLuigiConfirmacao.wait()
    print(MboxAlphaLuigiConfirmacao.read())
    MboxAlphaLuigiConfirmacao.send('hello to you!')
    MboxAlphaLuigiCores.send('Nada')

def conecta_nos_dois():
    print('waiting for connection...')
    server.wait_for_connection(2)
    print('connected')
    MboxAlphaLuigiCores.send('Nada')



def manda_mensagem_Luigi(tubo_para_entregar = 15, tubo_para_devolver = 'Nada'):
    if tubo_para_entregar == 10:
        tubo_para_entregar = 'amarelo'
    elif tubo_para_entregar == 15:
        tubo_para_entregar = 'vermelho'
    elif tubo_para_entregar == 20:
        tubo_para_entregar = 'azul'


    if tubo_para_devolver == 10:
        tubo_para_devolver = 'amarelo'
    elif tubo_para_devolver == 15:
        tubo_para_devolver = 'vermelho'
    elif tubo_para_devolver == 20:
        tubo_para_devolver = 'azul'
        
    MboxAlphaLuigiCores.send([tubo_para_entregar, tubo_para_devolver])


def manda_nada_luigi():
    MboxAlphaLuigiCores.send('Nada')

def manda_confirmacao_luigi():
    MboxAlphaLuigiConfirmacao.send('Tubo Pego')

def manda_confirmacao_devolucao_luigi():
    MboxAlphaLuigiConfirmacao.send('Tubo Devolvido')

def manda_nada_confirmacao_luigi():
    MboxAlphaLuigiConfirmacao.send('Nada')

def posso_pegar_tubo():
    leitura = MboxAlphaLuigiConfirmacao.read()
    if leitura == 'Tubo entregue':
        return True
    else:
        return False