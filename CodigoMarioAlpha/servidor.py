from declaracoes import *

server = BluetoothMailboxServer()
MboxAlphaBeta = TextMailbox('alphabeta', server)
MboxAlphaBetaLuz = NumericMailbox('alphabetaluz', server)
MboxAlphaBetaUltrassom =  NumericMailbox('alphabetaultrassom', server)
MboxAlphaLuigi = TextMailbox('alphaluigi', server)

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
    MboxAlphaLuigi.wait()
    print(MboxAlphaLuigi.read())
    MboxAlphaLuigi.send('hello to you!')
