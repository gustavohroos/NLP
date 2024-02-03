"""
Peça ao usuário para inserir uma frase. Seu programa deve
encontrar e exibir a palavra mais longa na frase. Você pode considerar que as
palavras são separadas por espaços em branco. Por exemplo, se o usuário inserir
"Python é uma linguagem de programação poderosa", o programa deve exibir
"programação" como a palavra mais longa.
"""

string = input("Digite uma frase: ")

words = string.split()

longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("A palavra mais longa é:", longest_word)