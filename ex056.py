s = 0
b = 0
mh = 0
nomev = ''
for c in range(1, 5):
    print(f'-----------{c}° PESSOA----------')
    nome = input('Nome:')
    idade = int(input('Idade:'))
    sexo = input('Sexo(F/M):')
    s += idade
    if sexo in 'Ff'and idade < 20:
        b += 1
    elif sexo in 'Mm'and c == 1:
        mh = idade
        nomev = nome
    elif sexo in 'Mm' and idade > mh:
        mh = idade
        nomev = nome
print('----------------------')
print(f'A media da idade do grupo é {s / 4}')
print(f'O nome do homem mais velho tem {mh} e seu nome é {nomev}')
print(f'Tem {b} mulheres com menos de 20 anos')