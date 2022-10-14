from declaracoes import *

client = BluetoothMailboxClient()
MboxAlphaBeta = TextMailbox('alphabeta', client)
MboxAlphaBetaLuz = NumericMailbox('alphabetaluz', client)
MboxAlphaBetaUltrassom =  NumericMailbox('alphabetaultrassom', client)

def conecta_alpha_beta():
        
    # This is the name of the remote EV3 or PC we are connecting to.
    SERVER = 'ev3dev'


    print('establishing connection...')
    client.connect(SERVER)
    print('connected!')

    # In this program, the client sends the first message and then waits for the
    # server to reply.
    MboxAlphaBeta.send('hello!')
    MboxAlphaBeta.wait()
    print(MboxAlphaBeta.read())