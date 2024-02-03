"""
Remoção de stopwords: Remova as palavras de parada (stopwords) do texto.
Você pode usar a lista de stopwords do NLTK ou outra lista de sua escolha.
"""
import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords

with open("story.txt", "r") as file:
    story = file.read()

story_words = story.split()

stop_words = set(stopwords.words('portuguese'))

story_words = [word for word in story_words if word.lower() not in stop_words]

print(story_words)
