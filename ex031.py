dist = int(input('qual a distancia ate seu destino?'))

if dist >= 200:
    c1 = dist * 0.45
    print('valor da viagem:', c1)
if dist < 200:
    c2 = dist * 0.50
    print('valor da viagem:', c2)
