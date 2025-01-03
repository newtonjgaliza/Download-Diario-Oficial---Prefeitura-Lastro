#ANO:2023

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from urllib.parse import urljoin

# Função para configurar o navegador Firefox com Selenium
def configurar_navegador():
    options = Options()
    options.headless = True  # Para executar o navegador em modo headless (sem abrir a janela)
    return options

# Função para fazer o download do PDF com cabeçalhos personalizados
def download_pdf(url_base, page_url, pasta_destino, driver):
    driver.get(page_url)
    
    # Usar Explicit Wait para aguardar até que o elemento esteja presente
    try:
        # Espera até que o elemento com o link do PDF seja carregado
        a_tag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='group92']/div[1]/ul[2]/li/a"))
        )
        
        # Obter o link do PDF
        pdf_relative_url = a_tag.get_attribute('href')

        if pdf_relative_url:
            # Construa a URL completa para o PDF
            pdf_url = urljoin(url_base, pdf_relative_url)
            print(f"Fazendo o download do PDF: {pdf_url}")

            # Configurando os cabeçalhos HTTP para simular um navegador
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'application/pdf',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive'
            }

            # Realizar o download do PDF com cabeçalhos
            pdf_response = requests.get(pdf_url, headers=headers, stream=True)
            if pdf_response.status_code == 200:
                # Extrair o nome do arquivo a partir da URL
                pdf_filename = pdf_url.split('/')[-1]

                # Definir o caminho de onde o arquivo será salvo
                save_path = os.path.join(pasta_destino, pdf_filename)

                # Garantir que a pasta de destino exista
                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)

                # Salvando o arquivo PDF
                with open(save_path, 'wb') as f:
                    for chunk in pdf_response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                print(f"Arquivo {pdf_filename} salvo em {save_path}")
            else:
                print(f"Erro ao baixar o PDF: {pdf_response.status_code}")
        else:
            print("Não foi encontrado o link para o PDF.")

    except Exception as e:
        print(f"Erro ao processar a página: {e}")

# Função para ler os links do arquivo txt
def processar_links(txt_file, url_base, pasta_destino):
    # Configura o navegador
    options = configurar_navegador()
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

    # Lendo o arquivo txt
    with open(txt_file, 'r') as file:
        links = file.readlines()

    # Processando cada link
    for link in links:
        link = link.strip()  # Remover espaços extras e quebras de linha
        print(f"Processando o link: {link}")
        download_pdf(url_base, link, pasta_destino, driver)

    # Fechar o navegador após o processo
    driver.quit()

# URL base do site
url_base = 'https://www.lastro.pb.gov.br'

# Caminho do arquivo txt com os links
txt_file = '2023.txt'

# Nome da pasta onde os PDFs serão salvos
pasta_destino = '2023'

# Processar os links do arquivo e fazer o download dos PDFs
processar_links(txt_file, url_base, pasta_destino)


'''
#ANO:2022

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from urllib.parse import urljoin

# Função para configurar o navegador Firefox com Selenium
def configurar_navegador():
    options = Options()
    options.headless = True  # Para executar o navegador em modo headless (sem abrir a janela)
    return options

# Função para fazer o download do PDF com cabeçalhos personalizados
def download_pdf(url_base, page_url, pasta_destino, driver):
    driver.get(page_url)
    
    # Usar Explicit Wait para aguardar até que o elemento esteja presente
    try:
        # Espera até que o elemento com o link do PDF seja carregado
        a_tag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='group92']/div[1]/ul[2]/li/a"))
        )
        
        # Obter o link do PDF
        pdf_relative_url = a_tag.get_attribute('href')

        if pdf_relative_url:
            # Construa a URL completa para o PDF
            pdf_url = urljoin(url_base, pdf_relative_url)
            print(f"Fazendo o download do PDF: {pdf_url}")

            # Configurando os cabeçalhos HTTP para simular um navegador
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'application/pdf',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive'
            }

            # Realizar o download do PDF com cabeçalhos
            pdf_response = requests.get(pdf_url, headers=headers, stream=True)
            if pdf_response.status_code == 200:
                # Extrair o nome do arquivo a partir da URL
                pdf_filename = pdf_url.split('/')[-1]

                # Definir o caminho de onde o arquivo será salvo
                save_path = os.path.join(pasta_destino, pdf_filename)

                # Garantir que a pasta de destino exista
                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)

                # Salvando o arquivo PDF
                with open(save_path, 'wb') as f:
                    for chunk in pdf_response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                print(f"Arquivo {pdf_filename} salvo em {save_path}")
            else:
                print(f"Erro ao baixar o PDF: {pdf_response.status_code}")
        else:
            print("Não foi encontrado o link para o PDF.")

    except Exception as e:
        print(f"Erro ao processar a página: {e}")

# Função para ler os links do arquivo txt
def processar_links(txt_file, url_base, pasta_destino):
    # Configura o navegador
    options = configurar_navegador()
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

    # Lendo o arquivo txt
    with open(txt_file, 'r') as file:
        links = file.readlines()

    # Processando cada link
    for link in links:
        link = link.strip()  # Remover espaços extras e quebras de linha
        print(f"Processando o link: {link}")
        download_pdf(url_base, link, pasta_destino, driver)

    # Fechar o navegador após o processo
    driver.quit()

# URL base do site
url_base = 'https://www.lastro.pb.gov.br'

# Caminho do arquivo txt com os links
txt_file = '2022.txt'

# Nome da pasta onde os PDFs serão salvos
pasta_destino = '2022'

# Processar os links do arquivo e fazer o download dos PDFs
processar_links(txt_file, url_base, pasta_destino)
'''
