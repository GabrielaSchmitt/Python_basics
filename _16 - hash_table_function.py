# Hash table function, used to grant dispersion between data
# in this scenario, we would have a hashed tabe of names being inserted. For that, each name will be encrypted using the above function
sum = 0
for letter in input("Nome: "): 
    sum += ord(letter)

hash = sum % 26 # 26 == max_alpha
print(hash)
