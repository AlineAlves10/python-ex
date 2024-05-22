num = int(input('Digite um número inteiro:'))
print('''Digite:
      [1] para binário
      [2] para octal
      [3] para hexadecimal''')
base = input('Escolha uma base de conversão:')

if base == '1':
    print('Seu número em binário é:{}'.format(bin(num)[2:]))
elif base == '2':
    print('Seu número em octal é:{}'.format(oct(num)[2:]))
elif base == '3':
    print('Seu número em hexadecimal é:{}'.format(hex(num)[2:]))
else:
    print('Opção invalida!')
