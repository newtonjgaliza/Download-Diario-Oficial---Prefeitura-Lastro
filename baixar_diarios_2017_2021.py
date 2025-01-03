
'''
#--Diarios 2021--#

import os
import requests
from lxml import html
from urllib.parse import urljoin

# URL base da página
url_base = "https://www.lastro.pb.gov.br/diario-oficial/edicoes-2021.html"

# Definir cabeçalhos (headers) para simular um navegador real
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Função para fazer o scraping de uma página e coletar links de PDF
def pegar_links_pagina(url):
    # Realiza o download da página HTML com os cabeçalhos definidos
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Verifica se houve erro na requisição
    
    # Parseia o HTML com lxml
    tree = html.fromstring(response.content)
    
    # XPath genérico para encontrar todos os links para arquivos PDF
    xpaths = '//*[@id="phoca-dl-category-box"]//a[contains(@href, ".pdf")]'
    links = tree.xpath(xpaths)
    
    # Lista para armazenar os links de PDF encontrados
    pdf_links = []
    
    # Processa todos os links encontrados
    for link in links:
        href = link.get('href')
        if href and href.lower().endswith('.pdf'):
            pdf_links.append(urljoin(url, href))  # Faz o join para garantir que a URL seja completa
    
    # Retorna a lista de links PDF encontrados
    return pdf_links

# Função para pegar o link da próxima página
def pegar_link_proxima_pagina(tree):
    # XPath para encontrar o link com title="Próximo"
    proximo_link = tree.xpath('//ul[@class="pagination"]//a[@title="Próximo"]/@href')
    
    # Retorna o link da próxima página, se existir
    if proximo_link:
        return proximo_link[0]  # Apenas o primeiro link encontrado
    
    # Caso não exista o link para a próxima página, retorna None
    return None

# Função para baixar os PDFs
def baixar_pdf(link_pdf, pasta_destino="2021"):
    # Cria a pasta, caso não exista
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Faz o download do PDF
    nome_arquivo = os.path.join(pasta_destino, os.path.basename(link_pdf))
    with requests.get(link_pdf, stream=True, headers=headers) as r:
        r.raise_for_status()
        with open(nome_arquivo, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    print(f"PDF salvo como {nome_arquivo}")

# Função principal que lida com a navegação pelas páginas
def navegar_paginas_e_baixar():
    url_atual = url_base
    downloads_feitos = 0
    pagina_atual = 1  # Começa na página 1
    
    while True:
        # Mensagem de início da coleta para a página atual
        print(f"Iniciando coleta dos arquivos da página {pagina_atual}")
        
        # Obter os links de PDF da página atual
        pdf_links = pegar_links_pagina(url_atual)
        
        # Baixar todos os PDFs encontrados
        for pdf_link in pdf_links:
            baixar_pdf(pdf_link)
            downloads_feitos += 1
        
        # Mensagem de finalização da coleta para a página atual
        print(f"Finalizando coleta dos arquivos da página {pagina_atual}")
        
        # Fazer o scraping para pegar o link da próxima página
        response = requests.get(url_atual, headers=headers)
        response.raise_for_status()
        tree = html.fromstring(response.content)
        
        # Verifica se existe um link para a próxima página
        proxima_pagina = pegar_link_proxima_pagina(tree)
        
        # Se não houver link para a próxima página, então estamos na última página
        if not proxima_pagina:
            print("Última página alcançada. Encerrando a navegação.")
            break
        
        # Atualiza a URL para a próxima página
        url_atual = urljoin(url_base, proxima_pagina)
        
        # Incrementa para a próxima página
        pagina_atual += 1
    
    # Exibe o número total de downloads feitos
    print(f"\nTotal de {downloads_feitos} PDF(s) baixado(s).")

# Chama a função principal para iniciar o processo
navegar_paginas_e_baixar()
'''


'''
#--Diarios 2020--#

import os
import requests
from lxml import html
from urllib.parse import urljoin

# URL base da página
url_base = "https://www.lastro.pb.gov.br/diario-oficial/edicoes-2020.html"

# Definir cabeçalhos (headers) para simular um navegador real
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Função para fazer o scraping de uma página e coletar links de PDF
def pegar_links_pagina(url):
    # Realiza o download da página HTML com os cabeçalhos definidos
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Verifica se houve erro na requisição
    
    # Parseia o HTML com lxml
    tree = html.fromstring(response.content)
    
    # XPath genérico para encontrar todos os links para arquivos PDF
    xpaths = '//*[@id="phoca-dl-category-box"]//a[contains(@href, ".pdf")]'
    links = tree.xpath(xpaths)
    
    # Lista para armazenar os links de PDF encontrados
    pdf_links = []
    
    # Processa todos os links encontrados
    for link in links:
        href = link.get('href')
        if href and href.lower().endswith('.pdf'):
            pdf_links.append(urljoin(url, href))  # Faz o join para garantir que a URL seja completa
    
    # Retorna a lista de links PDF encontrados
    return pdf_links

# Função para pegar o link da próxima página
def pegar_link_proxima_pagina(tree):
    # XPath para encontrar o link com title="Próximo"
    proximo_link = tree.xpath('//ul[@class="pagination"]//a[@title="Próximo"]/@href')
    
    # Retorna o link da próxima página, se existir
    if proximo_link:
        return proximo_link[0]  # Apenas o primeiro link encontrado
    
    # Caso não exista o link para a próxima página, retorna None
    return None

# Função para baixar os PDFs
def baixar_pdf(link_pdf, pasta_destino="2020"):
    # Cria a pasta, caso não exista
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Faz o download do PDF
    nome_arquivo = os.path.join(pasta_destino, os.path.basename(link_pdf))
    with requests.get(link_pdf, stream=True, headers=headers) as r:
        r.raise_for_status()
        with open(nome_arquivo, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    print(f"PDF salvo como {nome_arquivo}")

# Função principal que lida com a navegação pelas páginas
def navegar_paginas_e_baixar():
    url_atual = url_base
    downloads_feitos = 0
    pagina_atual = 1  # Começa na página 1
    
    while True:
        # Mensagem de início da coleta para a página atual
        print(f"Iniciando coleta dos arquivos da página {pagina_atual}")
        
        # Obter os links de PDF da página atual
        pdf_links = pegar_links_pagina(url_atual)
        
        # Baixar todos os PDFs encontrados
        for pdf_link in pdf_links:
            baixar_pdf(pdf_link)
            downloads_feitos += 1
        
        # Mensagem de finalização da coleta para a página atual
        print(f"Finalizando coleta dos arquivos da página {pagina_atual}")
        
        # Fazer o scraping para pegar o link da próxima página
        response = requests.get(url_atual, headers=headers)
        response.raise_for_status()
        tree = html.fromstring(response.content)
        
        # Verifica se existe um link para a próxima página
        proxima_pagina = pegar_link_proxima_pagina(tree)
        
        # Se não houver link para a próxima página, então estamos na última página
        if not proxima_pagina:
            print("Última página alcançada. Encerrando a navegação.")
            break
        
        # Atualiza a URL para a próxima página
        url_atual = urljoin(url_base, proxima_pagina)
        
        # Incrementa para a próxima página
        pagina_atual += 1
    
    # Exibe o número total de downloads feitos
    print(f"\nTotal de {downloads_feitos} PDF(s) baixado(s).")

# Chama a função principal para iniciar o processo
navegar_paginas_e_baixar()
'''


'''
#--Diarios 2019--#

import os
import requests
from lxml import html
from urllib.parse import urljoin

# URL base da página
url_base = "https://www.lastro.pb.gov.br/diario-oficial/edicoes-2019.html"

# Definir cabeçalhos (headers) para simular um navegador real
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Função para fazer o scraping de uma página e coletar links de PDF
def pegar_links_pagina(url):
    # Realiza o download da página HTML com os cabeçalhos definidos
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Verifica se houve erro na requisição
    
    # Parseia o HTML com lxml
    tree = html.fromstring(response.content)
    
    # XPath genérico para encontrar todos os links para arquivos PDF
    xpaths = '//*[@id="phoca-dl-category-box"]//a[contains(@href, ".pdf")]'
    links = tree.xpath(xpaths)
    
    # Lista para armazenar os links de PDF encontrados
    pdf_links = []
    
    # Processa todos os links encontrados
    for link in links:
        href = link.get('href')
        if href and href.lower().endswith('.pdf'):
            pdf_links.append(urljoin(url, href))  # Faz o join para garantir que a URL seja completa
    
    # Retorna a lista de links PDF encontrados
    return pdf_links

# Função para pegar o link da próxima página
def pegar_link_proxima_pagina(tree):
    # XPath para encontrar o link com title="Próximo"
    proximo_link = tree.xpath('//ul[@class="pagination"]//a[@title="Próximo"]/@href')
    
    # Retorna o link da próxima página, se existir
    if proximo_link:
        return proximo_link[0]  # Apenas o primeiro link encontrado
    
    # Caso não exista o link para a próxima página, retorna None
    return None

# Função para baixar os PDFs
def baixar_pdf(link_pdf, pasta_destino="2019"):
    # Cria a pasta, caso não exista
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Faz o download do PDF
    nome_arquivo = os.path.join(pasta_destino, os.path.basename(link_pdf))
    with requests.get(link_pdf, stream=True, headers=headers) as r:
        r.raise_for_status()
        with open(nome_arquivo, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    print(f"PDF salvo como {nome_arquivo}")

# Função principal que lida com a navegação pelas páginas
def navegar_paginas_e_baixar():
    url_atual = url_base
    downloads_feitos = 0
    pagina_atual = 1  # Começa na página 1
    
    while True:
        # Mensagem de início da coleta para a página atual
        print(f"Iniciando coleta dos arquivos da página {pagina_atual}")
        
        # Obter os links de PDF da página atual
        pdf_links = pegar_links_pagina(url_atual)
        
        # Baixar todos os PDFs encontrados
        for pdf_link in pdf_links:
            baixar_pdf(pdf_link)
            downloads_feitos += 1
        
        # Mensagem de finalização da coleta para a página atual
        print(f"Finalizando coleta dos arquivos da página {pagina_atual}")
        
        # Fazer o scraping para pegar o link da próxima página
        response = requests.get(url_atual, headers=headers)
        response.raise_for_status()
        tree = html.fromstring(response.content)
        
        # Verifica se existe um link para a próxima página
        proxima_pagina = pegar_link_proxima_pagina(tree)
        
        # Se não houver link para a próxima página, então estamos na última página
        if not proxima_pagina:
            print("Última página alcançada. Encerrando a navegação.")
            break
        
        # Atualiza a URL para a próxima página
        url_atual = urljoin(url_base, proxima_pagina)
        
        # Incrementa para a próxima página
        pagina_atual += 1
    
    # Exibe o número total de downloads feitos
    print(f"\nTotal de {downloads_feitos} PDF(s) baixado(s).")

# Chama a função principal para iniciar o processo
navegar_paginas_e_baixar()
'''



'''
#--Diarios 2018--#

import os
import requests
from lxml import html
from urllib.parse import urljoin

# URL base da página
url_base = "https://www.lastro.pb.gov.br/diario-oficial/edicoes-2018.html"

# Definir cabeçalhos (headers) para simular um navegador real
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Função para fazer o scraping de uma página e coletar links de PDF
def pegar_links_pagina(url):
    # Realiza o download da página HTML com os cabeçalhos definidos
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Verifica se houve erro na requisição
    
    # Parseia o HTML com lxml
    tree = html.fromstring(response.content)
    
    # XPath genérico para encontrar todos os links para arquivos PDF
    xpaths = '//*[@id="phoca-dl-category-box"]//a[contains(@href, ".pdf")]'
    links = tree.xpath(xpaths)
    
    # Lista para armazenar os links de PDF encontrados
    pdf_links = []
    
    # Processa todos os links encontrados
    for link in links:
        href = link.get('href')
        if href and href.lower().endswith('.pdf'):
            pdf_links.append(urljoin(url, href))  # Faz o join para garantir que a URL seja completa
    
    # Retorna a lista de links PDF encontrados
    return pdf_links

# Função para pegar o link da próxima página
def pegar_link_proxima_pagina(tree):
    # XPath para encontrar o link com title="Próximo"
    proximo_link = tree.xpath('//ul[@class="pagination"]//a[@title="Próximo"]/@href')
    
    # Retorna o link da próxima página, se existir
    if proximo_link:
        return proximo_link[0]  # Apenas o primeiro link encontrado
    
    # Caso não exista o link para a próxima página, retorna None
    return None

# Função para baixar os PDFs
def baixar_pdf(link_pdf, pasta_destino="2018"):
    # Cria a pasta, caso não exista
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Faz o download do PDF
    nome_arquivo = os.path.join(pasta_destino, os.path.basename(link_pdf))
    with requests.get(link_pdf, stream=True, headers=headers) as r:
        r.raise_for_status()
        with open(nome_arquivo, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    print(f"PDF salvo como {nome_arquivo}")

# Função principal que lida com a navegação pelas páginas
def navegar_paginas_e_baixar():
    url_atual = url_base
    downloads_feitos = 0
    pagina_atual = 1  # Começa na página 1
    
    while True:
        # Mensagem de início da coleta para a página atual
        print(f"Iniciando coleta dos arquivos da página {pagina_atual}")
        
        # Obter os links de PDF da página atual
        pdf_links = pegar_links_pagina(url_atual)
        
        # Baixar todos os PDFs encontrados
        for pdf_link in pdf_links:
            baixar_pdf(pdf_link)
            downloads_feitos += 1
        
        # Mensagem de finalização da coleta para a página atual
        print(f"Finalizando coleta dos arquivos da página {pagina_atual}")
        
        # Fazer o scraping para pegar o link da próxima página
        response = requests.get(url_atual, headers=headers)
        response.raise_for_status()
        tree = html.fromstring(response.content)
        
        # Verifica se existe um link para a próxima página
        proxima_pagina = pegar_link_proxima_pagina(tree)
        
        # Se não houver link para a próxima página, então estamos na última página
        if not proxima_pagina:
            print("Última página alcançada. Encerrando a navegação.")
            break
        
        # Atualiza a URL para a próxima página
        url_atual = urljoin(url_base, proxima_pagina)
        
        # Incrementa para a próxima página
        pagina_atual += 1
    
    # Exibe o número total de downloads feitos
    print(f"\nTotal de {downloads_feitos} PDF(s) baixado(s).")

# Chama a função principal para iniciar o processo
navegar_paginas_e_baixar()
'''



'''
--Diarios 2017--


import os
import requests
from lxml import html
from urllib.parse import urljoin

# URL base da página
url_base = "http://www.lastro.pb.gov.br/diario-oficial/edicoes-2017.html"

# Definir cabeçalhos (headers) para simular um navegador real
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Função para fazer o scraping de uma página e coletar links de PDF
def pegar_links_pagina(url):
    # Realiza o download da página HTML com os cabeçalhos definidos
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Verifica se houve erro na requisição
    
    # Parseia o HTML com lxml
    tree = html.fromstring(response.content)
    
    # XPath genérico para encontrar todos os links para arquivos PDF
    xpaths = '//*[@id="phoca-dl-category-box"]//a[contains(@href, ".pdf")]'
    links = tree.xpath(xpaths)
    
    # Lista para armazenar os links de PDF encontrados
    pdf_links = []
    
    # Processa todos os links encontrados
    for link in links:
        href = link.get('href')
        if href and href.lower().endswith('.pdf'):
            pdf_links.append(urljoin(url, href))  # Faz o join para garantir que a URL seja completa
    
    # Retorna a lista de links PDF encontrados
    return pdf_links

# Função para pegar o link da próxima página
def pegar_link_proxima_pagina(tree):
    # XPath para encontrar o link com title="Próximo"
    proximo_link = tree.xpath('//ul[@class="pagination"]//a[@title="Próximo"]/@href')
    
    # Retorna o link da próxima página, se existir
    if proximo_link:
        return proximo_link[0]  # Apenas o primeiro link encontrado
    
    # Caso não exista o link para a próxima página, retorna None
    return None

# Função para baixar os PDFs
def baixar_pdf(link_pdf, pasta_destino="2017"):
    # Cria a pasta, caso não exista
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Faz o download do PDF
    nome_arquivo = os.path.join(pasta_destino, os.path.basename(link_pdf))
    with requests.get(link_pdf, stream=True, headers=headers) as r:
        r.raise_for_status()
        with open(nome_arquivo, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    print(f"PDF salvo como {nome_arquivo}")

# Função principal que lida com a navegação pelas páginas
def navegar_paginas_e_baixar():
    url_atual = url_base
    downloads_feitos = 0
    pagina_atual = 1  # Começa na página 1
    
    while True:
        # Mensagem de início da coleta para a página atual
        print(f"Iniciando coleta dos arquivos da página {pagina_atual}")
        
        # Obter os links de PDF da página atual
        pdf_links = pegar_links_pagina(url_atual)
        
        # Baixar todos os PDFs encontrados
        for pdf_link in pdf_links:
            baixar_pdf(pdf_link)
            downloads_feitos += 1
        
        # Mensagem de finalização da coleta para a página atual
        print(f"Finalizando coleta dos arquivos da página {pagina_atual}")
        
        # Fazer o scraping para pegar o link da próxima página
        response = requests.get(url_atual, headers=headers)
        response.raise_for_status()
        tree = html.fromstring(response.content)
        
        # Verifica se existe um link para a próxima página
        proxima_pagina = pegar_link_proxima_pagina(tree)
        
        # Se não houver link para a próxima página, então estamos na última página
        if not proxima_pagina:
            print("Última página alcançada. Encerrando a navegação.")
            break
        
        # Atualiza a URL para a próxima página
        url_atual = urljoin(url_base, proxima_pagina)
        
        # Incrementa para a próxima página
        pagina_atual += 1
    
    # Exibe o número total de downloads feitos
    print(f"\nTotal de {downloads_feitos} PDF(s) baixado(s).")

# Chama a função principal para iniciar o processo
navegar_paginas_e_baixar()
'''