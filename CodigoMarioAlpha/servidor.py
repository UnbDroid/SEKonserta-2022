from declaracoes import *

server = BluetoothMailboxServer()
MboxAlphaBeta = TextMailbox('greeting', server)
MboxAlphaBeta2 = TextMailbox('greeting2', server)


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
