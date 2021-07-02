#CONDIÇÕES

#if ***:
#    ***
#elif ***:
#    ***
#else:
#    ***

#EXEMPLO 1

tempo = int(input('Quantos anos seu carro tem?'))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')

print('carro novo' if tempo <=3 else 'carro velho')
print ( '__FIM__' )

#EXEMPLO 2

nome = str(input('Qual é o seu nome?')).strip()
if nome == 'Gustavo':
    print('Que nome magestoso!')
else:
    print('Seu nome é tão normal')
print('Bom dia, {}'.format(nome))

#EXEMPLO 3

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
print('Parabéns' if m>=6 else "Estude mais!")

# ----------DESAFIOS-------------------------------------
# 028 - usuário testa se consegue acertar o número do computador de 1 - 5
import random
num = random.randint(0,5)
numusu = int(input('Tente adivinhar o número que o computador escolheu, escolha um número de 0 à 5: '))
print("Você venceu!" if numusu == num else "Você perdeu!")
print("O número era {}".format(num))

# 029 - Ler velocidade do carro se passar de 80kmh diz que foi multado e apresenta o valor 7 reais a cada km acima
velocidade = float(input('Digite a velocidade do seu carro: '))
if velocidade > 80:
    multa = ((velocidade-80)*7)
    print('Você foi multado, irá pagar {} reais.'.format(multa))
else:
    print('Você não foi multado. Tenha um bom dia, e dirija com segurança!')

# 030 - usuário da numero int e mostra se é par ou ímpar
num30 = int(input('Digite um número inteiro: '))
a30 = (num30%2)
print("É um número Par." if a30 == 0 else "É um número ímpar")

# 031 - pergunte a distância da viagem e cobre 0,50 por km até 200km e 0,45 para mais de 200km
distancia = int(input('Digite a distância de sua viagem: '))
preco31 = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da sua passagem é R$', preco31)
#a linha 63 faz:
#if distancia <=200:
#   preco31 = distancia*0.50
#else:
#    preco31 = distancia*0.45

# 032 - usuário diz o ano e programa responde se é bissexto
from datetime import date
ano32 = int(input('Digite o ano para verificar se é bissexto: \n Digite 0 para verificar o ano atual. '))
ano32 = date.today().year if ano32 == 0 else ano32
print("É um ano bissexto." if ano32 % 4 == 0  and ano32 % 100 != 0 or ano32 % 400 == 0 else "Não é bissexto")

# 033 - ler 3 números e ver qual é o maior e o menor
num133 = int(input('Digite um número inteiro: '))
num233 = int(input('Digite um número inteiro: '))
num333 = int(input('Digite um número inteiro: '))
menor= num133
menor = num233 if num233 < num133 and num233 < num333 else num133
menor = num333 if num333 < num133 and num333 < num233  else num133
maior = num133
maior = num233 if num233 > num133 and num233 > num333 else num133
maior = num333 if num333 > num133 and num333 > num233  else num133
print('O maior número é ', maior, '\ne o menor é ', menor, '.')

# 034 - aumentar 10% do salário de quem ganha mais de R$ 1.250,00 e aumentar 15% para salários iguais ou menores que R$ 1.250,00 .
salario34 = float(input('Digite seu salário: '))
if salario34 > 1250:
    aumento34 = salario34/10
else:
    aumento34 = (15*salario34)/100
print('Seu aumento é de {:.2f} reais.'.format(aumento34))
print('Seu salário atual é ', salario34+aumento34)

# 035 - leia o comprimento de 3 retas e diga ao usuário se elas podem formar um triângulo
print('-=--'*15)
print('Analisador de Triângulos')
print('-=--'*15)
r1 = float(input("Primeiro seguimento: "))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
print('Os seguimentos informados podem formar um triângulo' if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 else "Os seguimentos informados NÃO podem formar um triângulo. ")