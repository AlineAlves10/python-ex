s = 0 #acumulador
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        contador += 1
print(f'A soma de {contador} os valores solicitados é {s}')

    