"""
Escreva um programa que inicialize três strings distintas, e na
sequência unifique-as em uma nova variável. Sem utilizar métodos explícitos de
remoção, na string unificada anteriormente, mantenha apenas a primeira e a
última string inicialmente inseridas.
"""

string_1 = "Hello, World!"
string_2 = "Python is awesome!"
string_3 = "The rat ran away from the cat."

unified_string = string_1 + " " + string_2 + " " + string_3

print(unified_string)

unified_string_words = unified_string.split()

for i in range(len(unified_string_words)):
    if unified_string_words[i] in string_2:
        unified_string_words[i] = ""

unified_string = " ".join(unified_string_words)
# unified_string = unified_string.replace("  ", " ")

print(unified_string)