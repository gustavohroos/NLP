"""
Tokenização: Divida a história em palavras individuais.
"""

with open("story.txt", "r") as file:
    story = file.read()

story_words = story.split()

print(story_words)
