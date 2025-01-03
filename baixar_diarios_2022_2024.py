#ANO:2024

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
import time

# Função para configurar o navegador Firefox
def configurar_navegador():
    options = Options()
    options.headless = True  # Executar o navegador em modo headless (sem abrir a janela)
    return options

# Função para criar a pasta "2024" caso não exista
def criar_pasta(nome_pasta):
    if not os.path.exists(nome_pasta):
        os.makedirs(nome_pasta)

# Função para coletar links de cada página
def coletar_links_pagina(driver):
    links = []
    try:
        # Encontrar todos os links na página
        elementos = driver.find_elements(By.XPATH, "//td[@class='fabrik_actions fabrik_element']//a[contains(@href, '/diario-oficial/details')]")
        for el in elementos:
            href = el.get_attribute('href')
            if href:
                links.append(href)
    except Exception as e:
        print(f"Erro ao coletar links: {e}")
    return links

# Inicializa o navegador com o Firefox e o GeckoDriver
options = configurar_navegador()
servico = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=servico, options=options)

# URL base
base_url = "https://www.lastro.pb.gov.br/diario-oficial.html"
driver.get(base_url)

# Alterar o valor do elemento <select> para "2024"
try:
    # Esperar o carregamento do <select> e interagir com ele
    select_element = Select(driver.find_element(By.ID, "diario_oficial___exerciciovalue"))
    select_element.select_by_value("12")  # Seleciona a opção com valor "12" (para o ano 2024)
    print("Ano de 2024 selecionado com sucesso.")
    
    # Esperar um pouco para garantir que a página seja atualizada após a seleção
    time.sleep(3)
except Exception as e:
    print(f"Erro ao selecionar o ano de 2024: {e}")

# Coletando links por página
links_totais = []
numero_paginas = 7  # Número total de páginas conhecido

for pagina in range(1, numero_paginas + 1):
    print(f"Coletando links da página {pagina}...")
    try:
        # Alterar a URL com base no número da página
        driver.get(f"{base_url}?resetfilters=0&clearordering=0&clearfilters=0&limitstart27={(pagina - 1) * 10}")
        
        # Esperar um pouco para garantir que a página carregue completamente
        time.sleep(3)
        
        # Coletar os links dessa página
        links = coletar_links_pagina(driver)
        
        if links:
            print(f"Links encontrados na página {pagina}:")
            for link in links:
                print(link)
        
        links_totais.extend(links)
    
    except Exception as e:
        print(f"Erro ao coletar os links da página {pagina}: {e}")
    
# Gravar os links no arquivo 2024.txt
try:
    with open("2024.txt", "w") as f:
        for link in links_totais:
            f.write(link + "\n")
    print("Links salvos com sucesso no arquivo 2024.txt.")
except Exception as e:
    print(f"Erro ao salvar os links: {e}")

# Fechar o navegador
#driver.quit()
print('Fim')



'''
#ANO:2023

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
import time

# Função para configurar o navegador Firefox
def configurar_navegador():
    options = Options()
    options.headless = True  # Executar o navegador em modo headless (sem abrir a janela)
    return options

# Função para criar a pasta "2023" caso não exista
def criar_pasta(nome_pasta):
    if not os.path.exists(nome_pasta):
        os.makedirs(nome_pasta)

# Função para coletar links de cada página
def coletar_links_pagina(driver):
    links = []
    try:
        # Encontrar todos os links na página
        elementos = driver.find_elements(By.XPATH, "//td[@class='fabrik_actions fabrik_element']//a[contains(@href, '/diario-oficial/details')]")
        for el in elementos:
            href = el.get_attribute('href')
            if href:
                links.append(href)
    except Exception as e:
        print(f"Erro ao coletar links: {e}")
    return links

# Inicializa o navegador com o Firefox e o GeckoDriver
options = configurar_navegador()
servico = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=servico, options=options)

# URL base
base_url = "https://www.lastro.pb.gov.br/diario-oficial.html"
driver.get(base_url)

# Alterar o valor do elemento <select> para "2023"
try:
    # Esperar o carregamento do <select> e interagir com ele
    select_element = Select(driver.find_element(By.ID, "diario_oficial___exerciciovalue"))
    select_element.select_by_value("11")  # Seleciona a opção com valor "1" (para o ano 2023)
    print("Ano de 2023 selecionado com sucesso.")
    
    # Esperar um pouco para garantir que a página seja atualizada após a seleção
    time.sleep(3)
except Exception as e:
    print(f"Erro ao selecionar o ano de 2023: {e}")

# Coletando links por página
links_totais = []
numero_paginas = 6  # Número total de páginas conhecido

for pagina in range(1, numero_paginas + 1):
    print(f"Coletando links da página {pagina}...")
    try:
        # Alterar a URL com base no número da página
        driver.get(f"{base_url}?resetfilters=0&clearordering=0&clearfilters=0&limitstart27={(pagina - 1) * 10}")
        
        # Esperar um pouco para garantir que a página carregue completamente
        time.sleep(3)
        
        # Coletar os links dessa página
        links = coletar_links_pagina(driver)
        
        if links:
            print(f"Links encontrados na página {pagina}:")
            for link in links:
                print(link)
        
        links_totais.extend(links)
    
    except Exception as e:
        print(f"Erro ao coletar os links da página {pagina}: {e}")
    
# Gravar os links no arquivo 2023.txt
try:
    with open("2023.txt", "w") as f:
        for link in links_totais:
            f.write(link + "\n")
    print("Links salvos com sucesso no arquivo 2023.txt.")
except Exception as e:
    print(f"Erro ao salvar os links: {e}")

# Fechar o navegador
driver.quit()
print('Fim')
'''



'''
#ANO:2022

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
import time

# Função para configurar o navegador Firefox
def configurar_navegador():
    options = Options()
    options.headless = True  # Executar o navegador em modo headless (sem abrir a janela)
    return options

# Função para criar a pasta "2022" caso não exista
def criar_pasta(nome_pasta):
    if not os.path.exists(nome_pasta):
        os.makedirs(nome_pasta)

# Função para coletar links de cada página
def coletar_links_pagina(driver):
    links = []
    try:
        # Encontrar todos os links na página
        elementos = driver.find_elements(By.XPATH, "//td[@class='fabrik_actions fabrik_element']//a[contains(@href, '/diario-oficial/details')]")
        for el in elementos:
            href = el.get_attribute('href')
            if href:
                links.append(href)
    except Exception as e:
        print(f"Erro ao coletar links: {e}")
    return links

# Inicializa o navegador com o Firefox e o GeckoDriver
options = configurar_navegador()
servico = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=servico, options=options)

# URL base
base_url = "https://www.lastro.pb.gov.br/diario-oficial.html"
driver.get(base_url)

# Alterar o valor do elemento <select> para "2022"
try:
    # Esperar o carregamento do <select> e interagir com ele
    select_element = Select(driver.find_element(By.ID, "diario_oficial___exerciciovalue"))
    select_element.select_by_value("10")  # Seleciona a opção com valor "10" (para o ano 2022)
    print("Ano de 2022 selecionado com sucesso.")
    
    # Esperar um pouco para garantir que a página seja atualizada após a seleção
    time.sleep(3)
except Exception as e:
    print(f"Erro ao selecionar o ano de 2022: {e}")

# Coletando links por página
links_totais = []
numero_paginas = 6  # Número total de páginas conhecido

for pagina in range(1, numero_paginas + 1):
    print(f"Coletando links da página {pagina}...")
    try:
        # Alterar a URL com base no número da página
        driver.get(f"{base_url}?resetfilters=0&clearordering=0&clearfilters=0&limitstart27={(pagina - 1) * 10}")
        
        # Esperar um pouco para garantir que a página carregue completamente
        time.sleep(3)
        
        # Coletar os links dessa página
        links = coletar_links_pagina(driver)
        
        if links:
            print(f"Links encontrados na página {pagina}:")
            for link in links:
                print(link)
        
        links_totais.extend(links)
    
    except Exception as e:
        print(f"Erro ao coletar os links da página {pagina}: {e}")
    
# Gravar os links no arquivo 2022.txt
try:
    with open("2022.txt", "w") as f:
        for link in links_totais:
            f.write(link + "\n")
    print("Links salvos com sucesso no arquivo 2022.txt.")
except Exception as e:
    print(f"Erro ao salvar os links: {e}")

# Fechar o navegador
#driver.quit()
print('Fim')
'''