"""
Peça ao usuário para inserir uma frase ou uma palavra. Em seguida,
crie um programa que conte quantas vogais e consoantes estão presentes na
entrada. Exiba os resultados.
"""

string = input("Digite uma frase ou uma palavra: ")

vowels = ['a', 'e', 'i', 'o', 'u']

vowels_count = 0
consonants_count = 0

for i in range(len(string)):
    if string[i] in vowels:
        vowels_count += 1
    elif string[i].isalpha():
        consonants_count += 1

print(f"Quantidade de vogais: {vowels_count}")
print(f"Quantidade de consoantes: {consonants_count}")