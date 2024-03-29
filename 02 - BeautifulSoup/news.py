import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    content = response.content
    site = BeautifulSoup(content, 'html.parser')

    # HTML da noticia
    noticia = site.find('div', class_='feed-post-body')

    # Verificar se a notícia foi encontrada
    if noticia:
        titulo = noticia.find('a', class_='feed-post-link')
        subtitulo = noticia.find('div', class_='feed-post-body-resumo')

        if titulo and subtitulo:
            print(titulo.text.strip())
            print(subtitulo.text.strip())
        else:
            print("Título ou subtítulo não encontrados.")
    else:
        print("Nenhuma notícia encontrada.")
else:
    print("Falha ao acessar a página:", response.status_code)
