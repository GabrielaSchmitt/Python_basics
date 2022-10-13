#CONDIÇÕES ANINHADAS

nome = str(input('Qual é o seu nome?')).strip()
if nome == 'Gustavo':
    print('Que nome magestoso!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo' or nome == 'Gabriela':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana Jennifer':
    print('Belo nome feminino.')
else:
    print('Seu nome é tão normal.')
print ( 'Bom dia, {}'.format ( nome ) )

print('\n','-=--'*15)
print('DESAFIOS')
print('-=--'*15,'\n')

# 036 - pergunta valor da casa, salário, e quantos anos ele paga a casa. calcule a prestação mensal não excedendo 30% do salário.

salario36 = float(input('Digite seu salário: R$'))
casa36 = float(input('Digite o valor do imóvel: R$'))
anos36 = int(input('Digite o tempo de amortização em anos: '))
meses36 = anos36 * 12
prest36 = casa36 / meses36
por36 = (3 * salario36)/10
if prest36 > por36:
    print ( 'Empréstimo negado.')
else:
    print('Empréstimo concedido! A casa será paga com prestação mensal de {:.2f} reais.'.format(prest36))

# 037 - leia um número inteiro e o usúario escolhe qual a base da conversão, [1] binário [2] octal [3] hexadecimal

num37  = int(input('Digite um número: '))
base37  = int(input('Escolha a base da conversão\n [1] Binário\n [2] Octal\n [3] Hexadecimal\nOpção: '))
if base37 == 1:
    print('{} convertido para Binário é igual a {}'.format(num37, bin(num37)[2:]))
elif base37 == 2:
    print('{} convertido para Octal é igual a {}'.format(num37, oct(num37)[2:]))
elif base37 == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num37, hex(num37)[2:]))
else:
    print('Opção inválida, tente novamente.')

# 038 - comparação entre dois valores

valor38 = int(input('Digite o primeiro valor: '))
valor388= int(input('Digite o segundo valor: '))
if valor388 == valor38:
    print('Os dois valores são iguais!')
elif valor388 > valor38:
    print('O segundo valor é maior.')
elif valor38 > valor388:
    print('O primeiro valor é maior.')

# 039 - ler ano de nascimento informar a idade e verificar se precisa se alistar e o tempo de atraso ou espera
from datetime import date
ano39 = int(input('Qual é o ano que você nasceu? '))
anoatual39 = date.today().year
idade39 = anoatual39 - ano39
if idade39 == 18:
    print('Você deve se alistar este ano.')
elif idade39 > 18:
    a39 = idade39 - 18
    print('Você perdeu o prazo do alistamento. Atraso de {} anos.'.format(a39))
elif idade39 < 18:
    a39 = 18 - idade39
    print('Você ainda vai se alistar. Faltam {} anos.'.format(a39))

# 040 - duas notas de um aluno, calcula média + mensagem.
nota40 = float(input('Digite sua primeira nota: '))
nota400 = float(input('Digite sua segunda nota: '))
media40 = (nota40 +nota400)/2
print('Sua média final é: ', media40)
if media40 < 5:
    print('REPROVADO.')
elif 7 > media40 >= 5:
    print('RECUPERAÇÃO.')
elif media40 >= 7:
    print('APROVADO.')

# 041 - categoria de nadadores por idade
from datetime import date
ano41 = int(input('Vamos verificar sua categoria de natação!\n Digite seu ano de nascimento: '))
anoatual41 = date.today().year
idade41 = anoatual41 - ano41
if idade41 <= 9:
    print('Sua categoria é MIRIM.')
elif idade41 > 9 and idade41 <=14:
    print('Sua categoria é INFANTIL.')
elif idade41 > 14 and idade41 <=19:
    print('Sua categoria é JUNIOR.')
elif idade41 > 19 and idade41 <=20:
    print('Sua categoria é SÊNIOR.')
elif idade41 > 20:
    print('Sua categoria é MASTER.')

# 042 - sabendo que 3 retas formam um triangulo verifique é é equilátero, isósceles ou escaleno.
print('-=--'*15)
print('Analisador de Triângulos')
print('-=--'*15)
r1 = float(input("Primeiro seguimento: "))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos informados podem formar um triângulo')
    if r1 == r2 == r3:
        print('Este é um triângulo Equilátero.')
    elif r1 != r2 or r1 != r3 or r3 != r2:
        print ( 'Este triângulo é Escaleno.' )
    else:
        print('Este triângulo é Isósceles.')
else:
    print("Os seguimentos informados NÃO podem formar um triângulo. ")

# 043 - ler peso e altura calcular IMC e devolver mensagem.
peso43 = float(input('Digite seu peso (em quilos): '))
altura43 = float(input('Digite sua altura (em metros): '))
imc43 = peso43/(altura43**2)
print('Seu IMC é ', imc43)
if imc43 < 18.5:
    print('Você esta abaixo do peso.')
elif imc43 >= 18.5 and imc43 < 25:
    print('Você esta com peso ideal.')
elif imc43 >= 25 and imc43 < 30:
    print('Você esta com sobrepeso.')
elif imc43 >= 30 and imc43 < 40:
    print('Você esta com obesidade.')
elif imc43 >= 40:
    print('Você esta com obesidade mórbida.')

# 044 - calcula o valor a ser pago pelo produto levando em consideração o preço e condição de pagamento.
preco44 = float(input('Digite o valor do produto: '))
cond44 = int(input('Agora vamos escolher a forma de pagamento:\n [1]. à vista Dinheiro/cheque.\n [2]. à vista no Cartão.\n [3]. 2x no Cartão.\n [4]. 3x ou mais no Cartão.\n Digite: '))
if cond44 == 1:
    print('\033[37m Dinheiro/cheque selecionado.\033[m\nO valor do produto com \033[32m 10% de desconto \033[m é R$', preco44-(preco44/10))
elif cond44 == 2:
    print('\033[37m À vista no Cartão selecionado.\033[m\nO valor do produto com \033[32m 5% de desconto \033[m é R$', preco44-((5*preco44)/100))
elif cond44 == 3:
    print('\033[37m 2x no Cartão selecionado.\033[m\nO valor do produto é R$', preco44, ' com 2 parcelas de ', preco44/2)
elif cond44 ==4:
    print('\033[37m 3x ou mais no Cartão selecionado.\033[m')
    vz44 = int(input('Em quantas vezes deseja parcelar?\nDigite: '))
    juros44 = (preco44*20/100)+preco44
    print('O valor do produto fica R${:.2f} com parcela de R${:.2f} mensal.'.format(juros44,(juros44/vz44)))
else:
    print('\033[31m OPÇÃO INVÁLIDA, tente novamente.\033[m')
print('Boas compras, volte sempre!\n')

# 045 - Jokenpô com o pc
import random
print('Vamos Jogar Jokenpô!\nDecidindo entre pedra, papel ou tesoura...')
dec45 = int(input('Escolha sua opção:\n[1] Pedra\n[2] Papel\n[3] Tesoura\nDigite: '))
comp45 = random.randint(1,3)
print('Joooo\nKenn\nPô!')
if comp45 == 3:
    print('Escolhi tesoura.')
elif comp45 == 2:
    print('Escolhi Papel.')
elif comp45 == 1:
    print('Escolhi Pedra.')

if dec45 == comp45:
    print('EMPATE.')
#jogador ganha
elif (dec45 == 1 and comp45 == 3) or (dec45 == 2 and comp45 == 1) or (dec45 == 3 and comp45 == 2):
    print('Você venceu!!')
# jogador perde
elif (dec45 == 1 and comp45 == 2) or (dec45 == 2 and comp45 == 3) or (dec45 == 3 and comp45 == 1):
    print ( 'Você perdeu!!' )

#também há como fazer assim:

from random import randint
itens45 = ('Pedra', 'Papel', 'Tesoura')
computador45 = randint(0, 2)
jogador45 = int(input('Suas Opções:\n[0] Pedra\n[1] Papel\n[2] Tesoura\nDigite: '))
print('-='*10)
print('O jogador jogou {}'.format(itens45[jogador45]))
print('O computador escolheu {}'.format(itens45[computador45]))
print('-='*10)
if computador45 == 0:
    if jogador45 == 0:
        print('Empate.')
    elif jogador45 == 1:
        print('Jogador vence.')
    elif jogador45 == 2:
        print('Computador vence.')
elif computador45 == 1:
    if jogador45 == 0:
        print('Computador vence.')
    elif jogador45 == 1:
        print('Empate.')
    elif jogador45 == 2:
        print('Jogador vence.')
elif computador45 == 2:
    if jogador45 == 0:
        print('Jogador vence.')
    elif jogador45 == 1:
        print('Computador vence.')
    elif jogador45 == 2:
        print('Empate.')
