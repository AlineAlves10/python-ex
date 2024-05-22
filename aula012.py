nome = str(input('qual seu nome?'))
if nome == 'Aline':
    print('Que nome bonito!')
elif nome == 'maria' or nome == 'joao':
    print('que nome comum!')
else:
    print('que nome feio')
print(f'muito prazer! \003[31m{nome}')