import random
nume = random.randint(0, 5)
num = int(input('escolha um numero de 0 a 5:'))

if num == nume:
    print('PARABENS VOCE ACERTOU!')
else:
    print('VOCE ERROU!')
print(nume)
