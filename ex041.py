from datetime import date
atual = date.today().year
print('''BEM-VINDO(A) A ESCOLA DE NATAÇÃO
      vamos preencher sua ficha então nos informe essas informaçoes:''')
nome = input('Qual seu nome?')
idade = int(input('Qual ano você nasceu?'))
cont = atual - idade

cores = {'branco':'\033[30m',
         'amarelo':'\033[33m',
         'marinho':'\033[36m',
         'azul':'\033[34m',
         'verde':'\033[32m'}

if cont <= 9:
    print('você tem {} anos, está na categoria {}MIRIM'.format(cont, cores['branco']))
elif cont <= 14:
    print('você tem {} anos, está na categoria {}INFANTIL'.format(cont, cores['amarelo']))
elif cont <= 19:
    print('você tem {} anos, está na categoria {}JUNIOR'.format(cont, cores['marinho']))
elif cont <= 20:
    print('você tem {} anos, está na categoria {}SENIOR'.format(cont, cores['azul']))
else:
    print('você tem {} anos, está na categoria {}MASTER'.format(cont, cores['verde']))