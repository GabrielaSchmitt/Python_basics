# 1 - Escreva um programa que leia uma lista R de 6 elementos contendo um resultado da Mega-Sena e uma 
# lista A de 10 elementos contendo uma aposta. A seguir, mostre quantos acertos o apostador obteve. 

R = [] 
A = [] 
for i in range(0, 6):
  R.append(int(input('Digite o número resultado da Mega sena: ')))

for b in range(0, 10):
  A.append(int(input('Digite o número de sua Aposta: ')))

print('\nNúmeros da aposta que foram acertados: ')
for i in A: 
  #result = R.find(i)
  if i in R:
    print(i)
    


# 2 - A definição de "amplitude" em Estatística é dada pela grandeza numérica resultante da diferença entre 
# o maior valor e o menor valor do conjunto de valores de uma amostra. Escreva programa que leia uma sequencia 
# de números reais positivos terminada em zero (o número zero não deve ser processado pois serve para marcar o 
# final da entrada de dados). O programa deve determinar e mostrar o valor da amplitude estatística dos valores. 
# Exemplo: para a sequencia 4.5, 5.2, 1.7, 1.3, 1.9, 2.2, 8.3, 9.1, 5.4 e 0, teremos o resultado de 7.8 como amplitude.

numbers = []
while 1:
  val = float(input('Digite um número: '))
  if val == 0: break
  numbers.append(float(val))
numbers.sort()
#dif = numbers[0] - numbers[:]
print('A amplitude estatística da sequência de valores é: ' + str(float(numbers[-1] - numbers[0])))



# 3 - Escreva um programa que armazene em um dicionário o modelo e o consumo médio de cinco carros. Calcule 
# quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1.000 
# quilômetros e quanto isso custará, considerando o preço do combustível informado pelo usuário. 

carros = dict(zip(['Gol', 'Vectra', 'Palio', 'Sandero', 'Jeep Compass'], [11, 6, 9, 7, 6.5]))
#print('O carro mais economico do dicionário é:', max(carros, key=carros.get))
preco = float(input('Informe o preço do combustível: '))
print('Para percorrer 1000km, será gasto: \n')
for carro, autonomia in carros.items():
  txt1 = carro + ': '
  txt2 = str(round(1000/autonomia,2)) + ' litros'
  txt3 = ' - R$' + str(round(1000/autonomia*preco, 2))
  print(txt1.ljust(15), txt2.ljust(15), txt3.ljust(15))
  
  

# 4 - Um posto de combustível deseja determinar qual de seus produtos tem a preferência de seus clientes. 
# Para isso, deverá ser disponibilizado aos frentistas um programa que apresente o seguinte menu:
# [1] Álcool
# [2] Gasolina comum
# [3] Gasolina aditivada
# [4] Diesel
# [5] Fim
# A cada abastecimento, o frentista deverá informar qual foi o combustível vendido ao cliente. O programa 
# deverá será encerrado quando o código informado for o número 5 escrevendo então a mensagem: "Muito obrigado!"
# e a porcentagem de clientes que abasteceram cada tipo de combustível. 

import pandas as pd

df = pd.DataFrame()
df = pd.Series({'Álcool': 0, 'Gasolina comum': 0, 'Gasolina aditivada': 0, 'Diesel': 0, 'acessos': 0})

def acesso(controller):
  df.loc['acessos'] += 1
  #df.loc[0]['acessos'] = df.iloc[0]['acessos'] + 1
  if controller == 1:
    df.loc['Álcool'] += 1
  elif controller == 2: 
    df.loc['Gasolina comum'] +=  1
  elif controller == 3: 
    df.loc['Gasolina aditivada'] += 1
  elif controller == 4: 
    df.loc['Diesel'] += 1 
print(df)
controller = 1
while controller != 5:
  controller = int(input('\n\tPOSTO DE COMBUSTÍVEL \n\n [ 1 ] - Álcool\n [ 2 ] - Gasolina comum\n [ 3 ] - Gasolina aditivada\n [ 4 ] - Diesel \n [ 5 ] - Fim\n\nInforme a opção desejada: '))
  if controller != 5: 
    acesso(controller)
    controller = 1

print('\n\tMuito Obrigado!\n')
print('\n\tPorcentagens de clientes por combustível: \n\n Álcool: ' + str(df.loc['Álcool'] / df.loc['acessos']) + '%\n Gasolina comum: ' + str(df.loc['Gasolina comum'] / df.loc['acessos']) + '%\n Gasolina aditivada: ' + str(df.loc['Gasolina aditivada'] / df.loc['acessos']) + '%\n Diesel: ' + str(df.loc['Diesel'] / df.loc['acessos']) + '%')
