from declaracoes import *
from pybricks.messaging import *

client = BluetoothMailboxClient()
MboxAlphaLuigi = TextMailbox('alphaluigi', client)

def conecta_alpha_luigi():
    # This is the name of the remote EV3 or PC we are connecting to.
    SERVER = 'ev3dev'


    print('establishing connection...')
    client.connect(SERVER)
    print('connected!')

        # In this program, the client sends the first message and then waits for the
        # server to reply.
    MboxAlphaLuigi.send('hello!')
    MboxAlphaLuigi.wait()
    print(MboxAlphaLuigi.read())