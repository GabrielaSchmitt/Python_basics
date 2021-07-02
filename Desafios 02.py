import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

from math import sqrt, floor

num1 = int(input('Digite um número: '))
raiz1 = sqrt(num1)
print('A raiz de {} é igual a {}'.format(num1, floor(raiz1)))

import random

num2 = random.random()
num3 = random.randint(1, 10)
# randINT número aleatório inteiro (1, 10) = de um até 10
print('Random is ', num2)
print('Random is ', num3)

import emoji

print(emoji.emojize('Olá Mundo :earth_americas:', use_aliases=True))

#AULA DE MÓDULOS MATEMÁTICOS ref: https://docs.python.org/3/library/math.html

#Desafio 016 random mostrar a parte inteira:
import math
num6 = float(input('Digite um número: '))
print('O número {} tem a parte interia {}'.format(num6, math.floor(num6)))
#ou pode colocar o math.trunc(num6) ou simplesemnte int(num6)

#Desafio 017 mostrar a hipotenusa:
co = int(input('Digite o cateto oposto: '))
ca = int(input('Digite o cateto adjacente: '))
h = math.sqrt((co*co)+(ca*ca))
#Elevado pode ser feito também com ca ** 3 = ca*ca*ca. Nesse caso outra alternativa seria (ca**2 + co**2)**(1/2)
#também daria para simplificar a fórmula por math.hypot(co,ca)
print("A hipotenusa vale", h)

#Desafio 018 ANGULO e mostrar seno cosseno e tangente:
import math
an = int(input('Digite um ângulo: '))
sen = math.sin(an)
cos = math.cos(an)
tan = math.tan(an)
print('Sendo assim, o seno é {}, o cosseno é {} e a tangente é {}'.format(sen, cos, tan))

#Desafio 019 Sorteio de 4 nomes dado pelo usuario:
import random
a1 = input("Digite o nome do aluno: ")
a2 = input("Digite o nome do aluno: ")
a3 = input("Digite o nome do aluno: ")
a4 = input("Digite o nome do aluno: ")
alunos = [a1,a2,a3,a4]
sort = random.sample(alunos, 1)
#ou random.choice(sort)
print("O aluno sorteado hojé é: ", sort)

#Desafio 020 sorteando uma ordem para a lista:
import random
c1 = str(input("Nome do primeiro candidato: "))
c2 = str(input("Nome do segundo candidato: "))
c3 = str(input("Nome do terceiro candidato: "))
c4 = str(input("Nome do quarto candidato: "))
lista = [c1, c2, c3, c4]
random.shuffle(lista)
print("A ordem será: ", lista)

#Desafio 021 abra e reproduza mp3:
#o arquivo mp3 deve estar na mesma pasta que o seu código.

from pygame import mixer
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()
input()
