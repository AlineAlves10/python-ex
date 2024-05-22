num1 = int(input('Digite um numero inteiro:'))
num2 = int(input('Digite outro numero inteiro:'))

if num1 > num2:
    print(f'Número {num1} é maior')
elif num2 > num1:
    print(f'numero {num2} é maior')
elif num1 == num2:
    print('Os dois são iguais')