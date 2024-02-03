"""
Normalização: Normalize o texto fornecido em letras minúsculas e também
remova os acentos encontrados. Considere o uso da biblioteca unidecode.
"""

import unidecode

with open("story.txt", "r") as file:
    story = file.read()

story = unidecode.unidecode(story)
story = story.lower()

print(story)