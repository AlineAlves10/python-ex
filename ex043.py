peso = float(input('Quanto voce pesa?'))
alt = float(input('Qual sua altura?'))

imc = peso/(alt * alt)

if imc < 18.5:
    print('Seu IMC é {:.1f} voce está na categoria ABAIXO DO PESO'.format(imc))
elif imc >= 18.5 and imc < 25:
     print('Seu IMC é {:.1f} voce está na categoria PESO IDEAL'.format(imc))
elif imc >= 25 and imc < 30:
     print('Seu IMC é {:.1f} voce está na categoria SOBREPESO'.format(imc))
elif imc >= 30 and imc < 40:
     print('Seu IMC é {:.1f} voce está na categoria OBESIDADE'.format(imc))
else:
     print('Seu IMC é {:.1f} voce está na categoria OBESIDADE MORBIDA'.format(imc))