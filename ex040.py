nota1 = float(input('Digite sua nota:'))
nota2 = float(input('Digite sua nota:'))
media = (nota1 + nota2)/ 2

cores = {'verde':'\033[32m',
    'vermelho':'\033[31m',
    'amarelo': '\033[33m'}

if media < 5.0:
    print('Sua nota foi abaixo de 5, {}Reprovado!'.format(cores['vermelho']))
elif media > 5.0 and media < 6.9:
    print('Sua media foi {}, está de {}Recuperação'.format(media, cores['amarelo']))
elif media > 7.0:
    print('Sua média foi maior que 7, {}Aprovado!'.format(cores['verde']))