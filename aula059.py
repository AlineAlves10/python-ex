primeiro = int(input('primerio valor: '))
segundo = int(input('Segundo valor: '))

c = 1
while c != 5:
    print('''-------------------
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
    opcao = int(input('Qual a sua opção?'))
    c = opcao

    if opcao == 1:
        soma = primeiro + segundo
        print(f'A soma desses 2 numeros são {soma}')
    elif opcao == 2:
        mult = primeiro * segundo
        print(f'A multiplcação desses 2 numeros são {mult}')
    elif opcao == 3:
        if primeiro < segundo:
            print(f'O número {segundo} é maior')
        else:
            print(f'O número {primeiro} é maior')
print('fim')
