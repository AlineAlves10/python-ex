from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('os valores sorteados foram:')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nmaior valor sorteado foi {max(numeros)}')
print(f'menor valor sorteado foi {min(numeros)}')
