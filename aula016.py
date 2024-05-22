#TUPLAS ()
#tuplas sao imutaveis!

lanche = 'Hamburguer', 'suco', 'pudim', 'bolo'
print(sorted(lanche)) #mostra o lanche em ordem

for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posiçao {pos}') #outra forma de mostrar a posição

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}') #da para mostrar a posição

#MESMO QUE:

for c in lanche:
    print(f'Eu vou comer {c}')
print('Comi pra caramba!')

#OUTRO EXEMPLO COM TUPLAS DIFERENTES
a = (1, 3, 8, 6)
b = (8, 6, 5)
c = a + b
print(resultado= (1, 3, 8, 6, 8, 6, 5))
print(c.count(6)) #vai mostrar quantas vezes o 6 aparece
print(c.index(8)) #vai mostrar em qual posiçao esta o 8

#OUTRO JEITO
pessoa = ('Aline', 20, 'F', 43,3)
del(pessoa) #para apagar da memoria
