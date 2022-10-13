#Nomes com espaço, repetição...
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!' .format(nome))
print('Prazer em te conhecer {:<20}!' .format(nome))
print('Prazer em te conhecer {:>20}!' .format(nome))
print('Prazer em te conhecer {:^20}!' .format(nome))
print('Prazer em te conhecer {:=^20}!' .format(nome))

#Operadores matemáticos em função:
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2
print('A soma vale: {}'.format(s))
m = n1*n2
print('A multiplicação vale: {}'.format(m))
d = n1/n2
print('A divisão vale: {:.3f}'.format(d))
di = n1//n2
print('A divisão inteira vale: {}'.format(di))
e = n1**n2
print('A elevação vale: {}'.format(e))

#Uma linha de print para tudo end=' ' e uma quebra \n:
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} \n e potência {}'.format(di, e))
#Desafio 005, Sucessor e antecessor de um número:
a = int(input('Digite um número: '))
b = a-1
c = a+1
print('O antecessor de {} é {}, e seu sucessor é {}. '.format(a, b, c))
#Desafio 006, dobro triplo e raiz quadrada:
d1 = int(input('Digite um número: '))
f = d1*2
g = d1*3
h = d1**(1/2)
print(' O dobro do numero digitado é {}, seu triplo é {}'.format(f, g), end=' ')
print('e sua raiz quadrada é {}'.format(h))
#Desafio 007, média de duas notas:
i = float(input('Digite a nota1: '))
j = float(input('Digite a nota2: '))
k = (i+j)/2
print('A média das duas notas é', k)
#Desafio 008, m para cm e mm :
l = int(input('Digite um número em metros para converter para centímetro e milímetro: '))
n = l*100
o = l*1000
print('O valor {} em metros fica {} centímetros e {} milimetros. '.format(l, n, o))
#Desafio 009, tabuada de número qualquer:
p = int(input('Digite um número para descobrir sua tabuada: '))
print('1 x {} = {}'.format(p, p))
q = 2*p
r = 3*p
s = 4*p
t = 5*p
u = 6*p
v = 7*p
w = 8*p
x = 9*p
y = 10*p
print('-' * 12)
print('2 x {:2} = {}'.format(p, q))
print('3 x {:2} = {}'.format(p, r))
print('4 x {:2} = {}'.format(p, s))
print('5 x {:2} = {}'.format(p, t))
print('6 x {:2} = {}'.format(p, u))
print('7 x {:2} = {}'.format(p, v))
print('8 x {:2} = {}'.format(p, w))
print('9 x {:2} = {}'.format(p, x))
print('10 x {:2} = {}'.format(p, y))
print('-' * 12)
#Desafio 010, quanto de dólar pode comprar:
z = float(input('Digite o número em reais que você tem '))
a1 = z/3.27
print('Você pode comprar {:.2f} dólares ($3,27)'.format(a1))
#Desafio 011, area da parede e quanto de tinta 1l=2m^2:
a2 = float(input('Digite altura da parede em metros: '))
a3 = float(input('Digite largura da parede em metros: '))
a4 = a2*a3
a5 = a4/2
print('Sabendo que a área da parede corresponde a {} metros quadrados \ne que 1 litro de tinta pinta 2 metros quadrados, precisaremos de {} litros de tinta para pinta-la.'.format(a4, a5))
#Desafio 012, preço e 5% de desconto:
a6 = float(input('Digite o preço do produto: '))
a7 = (a6*95)/100
print('Com 5% de desconto, o preço de seu produto vai de {} reais, para {} reais'.format(a6, a7))
#Desafio 013, salário e 15% de aumento:
a8 = float(input('Digite o salário do funcionário em questão: '))
a9 = (a8*115)/100
print('Com 15% de aumento, o salário do funcionário vai de {} reais, para {} reais'.format(a8, a9))
#Desafio 014, celsius para fahrenheit:
aa = float(input('Qual a temperatura em Celsius que deseja transformar: '))
ab = ((9 * aa) / 5) + 32
print('A temperatura {} em Celsius fica {} em Fahrenheit.'.format(aa, ab))
#Desafio 015,  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
ac = int(input('Digite por quantos dias o carro foi alugado: '))
ad = float(input('Digite quantos km foram andados: '))
ae = (ac*60) + (ad*0.15)
print('Sabendo que o custo diario da locação custa R$60,00 e que cada km rodado custa R$0,15 o custo da locação é de ', ae)







