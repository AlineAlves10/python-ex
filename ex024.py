cidade = input('digite o nome da sua cidade: ').strip()
cidade = cidade.upper()
lista = cidade.split()

b = 'SANTO' in lista[0]
print(b)
