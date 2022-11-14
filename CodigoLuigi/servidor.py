from declaracoes import *
from pybricks.messaging import *

client = BluetoothMailboxClient()
MboxConfirmacao = TextMailbox('alphaluigi', client)
MboxCores = TextMailbox('alphaluigi2', client)
MboxCoresDevolve = TextMailbox('alphaluigi3', client)
MboxPodeComecar = LogicMailbox('alphaluigi4', client)

def conecta_alpha_luigi():
    # This is the name of the remote EV3 or PC we are connecting to.
    SERVER = 'ev3dev'

    print('establishing connection...')
    client.connect(SERVER)
    print('connected!')

        # In this program, the client sends the first message and then waits for the
        # server to reply.
    # MboxConfirmacao.send('hello!')
    # MboxConfirmacao.wait()
    print(MboxCores.read())
    #MboxCores.wait()
    

    #print(MboxConfirmacao.read())


    