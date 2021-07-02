#FATIAMENTO
frase = "Curso em video Python"

print(frase[9])
print(frase[9:13]) #começa no 9 e não inclui 13
print(frase[9:21]) #de 9 a 20
print(frase[9:21:2]) #de 9 a 20 de 2 em 2
print(frase[:5]) #começa do caracter 0
print(frase[15:]) #não indica o final, então vai até o último
print(frase[9::3]) #começe do 9 vai até o final de 3 em 3
print(len(frase)) #mostra a quantidade de caracteres
print(frase.count("0")) #quantas vezes aparece o
print(frase.count("0", 0, 13)) #de 0 a 12 temos quantos o
print(frase.find("deo")) #mostra onde começou as letras
print(frase.find("Android")) # recebe -1 quando ele não encontra a string
print('Curso' in frase) #mostra se tem a palavra levando em consideração letras maiúsculas
print(frase.replace("Python", "Android")) #substitui a primeira pela segunda
print(frase.upper()) #Deixa rudo em caixa alta
print(frase.lower()) #tudo em letra minuscula
print(frase.capitalize()) #Primeira letra em caixa alta
print(frase.title()) #inicio de cada palavra em caixa alta
print(frase.title()) #inicio de cada palavra em caixa alta

frase1 = "   Aprenda Python  "

frase12 =(frase1.strip()) #retira espaços adicionais no inicio e final da frase
print(frase1.rstrip()) #retira espaços adicionais no final A DIREITA da frase
print(frase1.lstrip()) #retira espaços adicionais no inicio A ESQUERDA da frase
print(len(frase12))

#DIVISÃO
print(frase.split()) #gera uma lista com todas as palavras digitadas

#JUNÇÃO
print("-".join(frase)) #coloca o que esta entre aspas separando cada letra da frase

frase2 = "caimbra no pé"
dividido = frase2.split()
print(dividido[2])

#DESAFIO 022  - dar nome completo, colocar em maiusculo e depois minusculo, contar letras s/ espaços, contar letras do 1 nome
nome = input("Digite seu nome: ")
print("Seu nome em maiúsculo é ", nome.upper())
print("Seu nome em minúsculo é ",nome.lower())
nomeSE =(nome.strip())
es = (nomeSE.count(" "))
t = len(nomeSE)
letras = t-es
print("Há ", letras, "letras no seu nome.")
sp = nome.split()
t1 = len(sp[0])
print("Seu primeiro nome possui ", t1, " letras.")

#DESAFIO 023  - dar numero e mostrar a unidade, dezena, centena e milhar de 0 - 9999
num = int(input("Digite um número de 0 a 9999: "))
unidade = num//1 % 10
dezena = num //10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print("\n unidade: ", unidade, "\n dezena: ", dezena, "\n centena: ", centena, "\n milhar: ", milhar)

#DESAFIO 024  - dar nome da cidade e verificar se começa com nome santo
cidade = str(input("Digite o nome da sua cidade: ")).strip()
print('Sua cidade tem "Santo" no nome? ', cidade[:5].upper() == "SANTO")

#DESAFIO 025  - dar nome da cidade e verificar se tem Silva
nomee = str(input("Digite o seu nome completo: "))
print("Seu nome tem Silva? {}".format('SILVA' in nomee.upper()))

#DESAFIO 026  - quantas vezes aparece "a", qual é a primeira posição em que aparece, e a última.
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))

#Desafio 027 - mostre o primeiro e último nome da pessoa
nome27 = str(input('Digite seu nome completo: ')).strip()
nome27d = nome27.split()
print('Seu primeiro nome é: {}'.format(nome27d[0]))
print('Seu último nome é: {}'.format(nome27d[len(nome27d)-1]))