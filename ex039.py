from datetime import date
atual = date.today().year
idade = int(input('Digite o ano de seu nascimento:'))
id = atual-idade
id1 = id - 18
id2 = 18 - id
if id < 18:
    print(f'Você terá que se alistar daqui {id2} anos')
elif id == 18:
    print('Hora de se alistar ein')
else:
    print(f'Ja passou {id1} anos que voce deveria ter se alistado')