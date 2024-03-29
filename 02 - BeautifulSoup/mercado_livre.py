import requests
from bs4 import BeautifulSoup

# Pesquisa no ML

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja?\n')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class':'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})

# print(produto.prettify())
contador = 0

for produto in produtos:
    contador += 1
    titulo = produto.find('h2', attrs={'class':'ui-search-item__title'})
    link = produto.find('a', attrs={'class':'ui-search-item__group__element ui-search-link__title-card ui-search-link'})
    real = produto.find('span', attrs={'class':'andes-money-amount__fraction'})
    centavos = produto.find('span', attrs={'class':'andes-money-amount__cents andes-money-amount__cents--superscript-24'})
    

    print('Titulo: ', titulo.text)
    print('Link', link['href'])
    print('Item nº: ', contador)

    if(centavos):
        print(f'Valor: R$ {real.text}, {centavos.text}')
    else:
        print(f'Valor: R$ {real.text}')

    print('\n\n')
  
