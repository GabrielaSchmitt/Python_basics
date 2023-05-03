alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

texto = input("texto: ")              
chave = int(input("chave k: "))       
what  = int(input("[1] - cifrar \n[2] - decifrar\nDigite: "))

if what == 1:
    traduzido = [alpha[(alpha.index(letra) + chave) % 26] for letra in texto]
else: 
    traduzido = [alpha[(alpha.index(letra) - chave) % 26] for letra in texto]
print(str(''.join(traduzido)))                     
