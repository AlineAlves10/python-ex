numero = int(input('me diga um numero aleatorio:'))

conta = numero %2
if conta == 0:
    print(numero, 'é PAR!')
else:
    print(numero, 'é IMPAR!')
