'''
Faça uso do arquivo HTML disponibilizado no e-aula.
# abre o arquivo local nomeado exemplo.html
HTMLFile = open("exemplo.html", "r")
Crie um programa Python que faça uso da biblioteca BeautifulSoup para fazer o parsing desse arquivo e extrair informações das tags “articles” presentes no arquivo.
Na sequência, apresente essas informações de uma maneira legível (sugestão: consulte a documentação da biblioteca Pandas).
'''
from bs4 import BeautifulSoup
import pandas as pd

with open('exemplo.html', 'r') as file:
    data = file.read()
soup = BeautifulSoup(data, 'html.parser')

articles = soup.find_all('article')

data = []

for article in articles:
    title = article.find('h3').text if article.find('h3') else 'Sem título'
    content = article.find('p').text if article.find('p') else 'Sem conteúdo'
    data.append({'titulo': title, 'conteudo': content})

df = pd.DataFrame(data)

print(df)
df.to_csv('articles.csv', index=False)