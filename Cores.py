# ANSI
# \033[m
# \033[style;text;backm
#Style: 0(none) 1(bold) 4(underline) 7(negative)
#Text: 30(branco) 31(vermelho) 32(verde) 33(amarelo) 34(azul) 35(roxo) 36(anil) 37(cinza)
#Back: 40(branco) 41(vermelho) 42(verde) 43(amarelo) 44(azul) 45(roxo) 46(anil) 47(cinza)



#text   cor  background

#30   preto        40
#31   vermelho     41
#32   verde        42
#33   amarelo      43
#34   azul         44
#35   Magenta      45
#36   ciano        46
#37   cinza        47
#97   branco       107

#Exemplos
print('\033[0;30;41mTeste')
print('\033[4;33;44mTeste')
print('\033[1;35;43mTeste')
print('\033[30;42mTeste')
print('\033[mTeste')
print('\033[7;30mTeste')
print('\033[1;31;43mOlá, Mundo!')
print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[30mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')
a = 88
b= 567
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!'.format(a,b))
nome = 'Gabi'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7:30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome,'\033[m'))
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))

