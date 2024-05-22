import random
from time import sleep
print('{:^40}'.format('BEM-VINDA AO JOGO DE JOKENPÔ: VOCÊ X COMPUTADOR'))
sleep(1)
print('VOCÊ ESTÁ PREPARADA?')
sleep(1)
print('''Escolha:
        -Pedra
        -Papel
        -Tesoura''')
joga = input('R:')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('='*30)
jo = ('Papel', 'Tesoura', 'Pedra')
comp = random.choice(jo)

#pedra
if (joga == 'Pedra' and comp == 'Papel'):
    print(f'A escolha do computador foi {comp}')
    print('O computador ganhou :(')
elif joga == 'Pedra' and comp == 'Tesoura':
    print(f'A escolha do computador foi {comp}')
    print('VOCE GANHOU!!!')
elif joga == 'Pedra' and comp == 'Pedra':
    print(f'A escolha do computador foi {comp}')
    print('EMPATE')

#papel
elif (joga == 'Papel' and comp == 'Tesoura'):
    print(f'A escolha do computador foi {comp}')
    print('O computador ganhou :(')
elif joga == 'Papel' and comp == 'Pedra':
    print(f'A escolha do computador foi {comp}')
    print('VOCE GANHOU !!!')
elif joga == 'Papel' and comp == 'Papel':
    print(f'A escolha do computador foi {comp}')
    print('EMPATE')

#tesoura
elif (joga == 'Tesoura' and comp == 'Pedra'):
    print(f'A escolha do computador foi {comp}')
    print('O computador ganhou :(')
elif joga == 'Tesoura' and comp == 'Papel':
    print(f'A escolha do computador foi {comp}')
    print('VOCE GANHOU !!!')
elif joga == 'Tesoura' and comp == 'Tesoura':
    print(f'A escolha do computador foi {comp}')
    print('EMPATE')
print('='*30)