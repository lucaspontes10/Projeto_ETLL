'''   print('O carro foi mutado')
else:
    print('A velocidade do carro não passou do radar 1')
    print('O carro Não foi mutado')'''

velocidade = 62 #velocidade atual do carro
local_carro = 90 # local em que o carro esta na estrada 

RADAR_1 = 60 # velocidade maxima do radar 1 
LOCAL_1 = 100 # local onde o rada 1 esta 
RADAR_RANGE = 1 # A distância onde o radar pega  

if velocidade > RADAR_1:
    print('Velocidade Carro passou do radar 1 ')
 
if local_carro >=(LOCAL_1 + RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
    print('O carro foi mutado')

