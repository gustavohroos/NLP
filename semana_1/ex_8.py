"""
Uso de Expressões Regulares: Use expressões regulares para encontrar todas
as ocorrências das palavras "João" e "Maria", inclusive como subpalavras, na
história e destaque essas palavras no texto, reescrevendo-as com todas as
letras maiúsculas.
"""

import re
import unidecode

with open("story.txt", "r") as file:
    story = file.read()

story = unidecode.unidecode(story)

story = story.lower()

def upper(match):
    return match.group().upper()

joao_count = len(re.findall(r'\bjoao\w*\b', story))
maria_count = len(re.findall(r'\bmaria\b', story))

story = re.sub(r'\bjoao\w*\b', upper, story)
story = re.sub(r'\bmaria\b', 'MARIA', story)

print(story)
print(f"João aparece {joao_count} vezes na história.")
print(f"Maria aparece {maria_count} vezes na história.")
