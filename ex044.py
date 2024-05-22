print('{:^40}'.format('BEM VINDA A NOSSA LOJA'))
pn = float(input('Preço das compras R$'))
print('''Qual vai ser a forma de pagamento:
      [ 1 ] Dinheiro/PIX (10% de desconto)
      [ 2 ] Cartão a vista (5% de desconto)
      [ 3 ] Cartão parcelado em 2x (Sem desconto)
      [ 4 ] Cartão parcelado em 3x ou mais (20% de juros)''')
cp = input('Informe o número de acordo com a forma de pagamento:')

if cp == '1':
    a = pn - ((10 / 100) * pn)
    print(f'Ganhou 10% de desconto! seu produto tem o valor de R${a}')
elif cp == '2':
    b = pn - ((5 / 100)* pn)
    print(f'Ganhou 5% de desconto! seu produto tem o valor de R${b}')
elif cp == '3':
    print(f'Seu produto tem o valor de R${pn}')
elif cp == '4':
    c = pn + ((20 / 100)* pn)
    print(f'Seu produto ficou com 20% de juros, ficou com o valor de R${c}')