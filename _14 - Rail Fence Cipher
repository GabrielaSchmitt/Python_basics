def repeat_index_tuples(s: str, index: int) -> list:
    index_str = str(index)
    tuples_list = []
    for i, char in enumerate(s):
        repeat_count = i % len(index_str)
        repeat_index = index_str[repeat_count]
        tuples_list.append((char, int(repeat_index)))
    return tuples_list
    
def classify_chars(s, sequence, k):
    indexed_chars = repeat_index_tuples(s, sequence)
    
    output = ''
    for x in range(1,(k+1)): 
        for letra, n in indexed_chars: 
            if (n == x):
                output += letra
    return output


# Testing the function
texto_aberto = input('texto: ').replace(" ", "")
k = int(input('chave: '))

numbers = range(1, k+1)
sequence= "".join(list(map(str, numbers)) + list(map(str, reversed(numbers[:-1]))))
sequence= sequence[:-1]

saida = classify_chars(texto_aberto, int(sequence), k)
print(saida)  

# teste inicial
# texto_aberto = 'hello world'.replace(" ", "")
# k = 3
# Expected output: holelwrdlo
