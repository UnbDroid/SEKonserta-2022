#!/usr/bin/env pybricks-micropython 

from declaracoes import *
from pegaTubo import *
from servidor import *
from andaPista import *
from cores import *




'''rodas.straight(-300)


le_sensor_cor()
while not (ve_cor(PRETO_ESQ_MIN, PRETO_ESQ_MAX, PRETO_DIR_MIN, PRETO_DIR_MAX) or ve_cor(RAMPA_ESQ_MIN, RAMPA_ESQ_MAX, RAMPA_DIREITO_MIN_, RAMPA_DIREITO_MAX)):
    le_sensor_cor()
    rodas.drive(100,0)

rodas.stop()

print('ACHEI')
le_sensor_cor()'''

vai_pro_ponto_inicial()
#rodas.straight(1000)


'''while luzEsquerda.reflection() < 60:
    rodas.drive(50,0)
rodas.stop()


while not ve_cor(BORDA_ESQ_MIN, BORDA_ESQ_MAX, BORDA_DIR_MIN, BORDA_DIR_MAX): 
    le_sensor_cor()
    segue_linha_sensor_esquerdo_prop()'''

#print(luzEsquerda.reflection())