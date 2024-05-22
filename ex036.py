casa = int(input('Qual o valor da casa? R$'))
sal = int(input('Qual seu salario? R$'))
anos = int(input('Quantos anos você pretende pagar a casa?'))

am = anos * 12
p = casa / am
s = (sal * 30)/ 100

if p > s:
    print('Empréstimo negado!')
else:
    print('ok, empréstimo aceito')
2313