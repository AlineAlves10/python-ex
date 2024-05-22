#style = 0(sem estilo), 1(negrito), 4(sublinhado), 7(inverter confg)
#text=30(branco),31(vermelho),32(verde),33(amarelo),34(azul),35(roxo),36(marinho),37(cinza)
#back = mesma cor dos text mas do 40 ao 47

#print('\033[0;30;41mOlá, mundo!\033[m')
#print('\033[4;33;44mOlá, mundo!\033[m')
#print('\033[1;35;43mOlá, mundo!\033[m')
#print('\033[0;30;42mOlá, mundo!\033[m')
#print('\033[mOlá, mundo!\033[m')
#print('\033[7;30;41mOlá, mundo!\033[m')

di = input('digite um numero:')
cores = {'azul';'\033[33m'
         'vermelho';'\033[31m'}
print('seu numero tem cheiro da cor {}{}'.format(cores['azul'], di))

