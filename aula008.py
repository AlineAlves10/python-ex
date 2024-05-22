import math
#ceil (arredondamento para cima)
#floor (arredondamento para baixo)
#trunc (eliminar da , pra frente)
#pow (potencia, semelhante aos **)
#sqrt (calcular raizes quadrada)
#factorial (calcular fatorial de um numero)

#FROM MATH IMPORT SQRT, CEIL

num = int(input('digite um numero:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
