numero = ('um', 'dois', 'tres', 'quadro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    a = int(input('Escolha um numero de 1 a 20:'))
    if a < 1 or a > 20:
        print('ESSE NÚMERO NAO TA NA SEQUENCIA, IDIOTA')
    else:
        print(numero[a-1])
        break