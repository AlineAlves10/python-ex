s = str(input('informe seu sexo: [M/F]')).upper().strip()
i = str(input('qual sua idade: '))


while s not in 'MmFf':
    s= str(input('Dados invalidos. Por favor, informe seu sexo: ')).upper()

print(f'sexo {s} registrado com sucesso')
