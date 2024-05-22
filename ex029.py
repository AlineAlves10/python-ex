v = int(input('qual a velocidade desse carro?'))
m = (v - 80) * 7
if v > 80:
    print(f'MULTADO! VALOR R$ {m},00')
else:
    print('De boa, pó passar')
