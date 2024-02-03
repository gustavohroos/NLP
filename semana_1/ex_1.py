"""
Solicite ao usuário que insira uma frase. Seu programa deve inverter
a ordem das palavras na frase e exibi-la de trás para frente. Por exemplo, se o
usuário inserir "Python é divertido", o programa deve exibir "divertido é Python".
Remova espaços extras contidos na frase, se houver
"""

string = input("Digite uma frase: ")

words = string.split()

for i in range(len(words), 0, -1):
    print(words[i-1], end=" ")