# biblioteca que nos permite realizar requisições  
import requests  
# biblioteca para decodificar o html e navegar nos dados  
from bs4 import BeautifulSoup  

# adicionar cores às strings
from colorama import Fore, init, Style

# Inicializa o colorama
init()

# função para obter as notícias  
def get_news(termo):  
    url = 'https://www.globo.com/'  
  
    # realizar a requisição  
    page = requests.get(url)  
  
    # usando o BS4 para organizar o retorno html  
    soup = BeautifulSoup(page.text, 'html.parser')  
  
    # Encontrar todas as tags <a>  
    noticias = soup.find_all('a')  
  
    for noticia in noticias:  
        titulo = noticia.find('h2')  # Verificar se existe uma tag <h2>  
        if titulo:  
            link = noticia['href']  # Extrair o link diretamente da tag <a>  
            # Busca por termo sem considerar maiúsculas ou minúsculas
            if termo.lower() in titulo.text.lower():
                print(Fore.GREEN + f'\nTítulo: {titulo.text}\n' + Fore.YELLOW + f'Link: {link}\n' + Style.RESET_ALL + '========================================\n')  

# Função para exibir o designer
def designer():
    print(Fore.RED + r'''
    _____ _       _                               
  / ____| |     | |                              
 | |  __| | ___ | |__   ___   ___ ___  _ __ ___  
 | | |_ | |/ _ \| '_ \ / _ \ / __/ _ \| '_ ` _ \ 
 | |__| | | (_) | |_) | (_) | (_| (_) | | | | | |
  \_____|_|\___/|_.__/ \___(_)___\___/|_| |_| |_|
                                                 
                                                 
''' + Style.RESET_ALL)

# Função para analisar o input do usuário
def analisar_input(frase):
    while True:
        analisar = input(frase)
        if analisar:
            return analisar
        else:
            print(Fore.BLUE + 'Favor preencha o campo de pesquisa...' + Style.RESET_ALL)

try:
    designer()
    print('\n\n\n')
    termo = analisar_input('Informe o termo de pesquisa: ')
    get_news(termo)
except Exception as e:
    print(Fore.RED + f'Ocorreu um erro, tente novamente... Erro: {e}' + Style.RESET_ALL)
