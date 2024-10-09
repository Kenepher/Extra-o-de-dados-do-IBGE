import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL do site que você quer extrair dados
url = 'https://www.ibge.gov.br/explica/codigos-dos-municipios.php'

# Enviar uma requisição GET para o site
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Criar um objeto BeautifulSoup para analisar o conteúdo HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar a tabela no HTML (ajuste o seletor conforme necessário)
    table = soup.find('table')

    # Criar uma lista para armazenar os dados
    data = []

    # Iterar sobre as linhas da tabela
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]  # Extrair texto e remover espaços em branco
        if cols:  # Verifica se a linha não está vazia
            data.append(cols)

    # Criar um DataFrame do pandas
    df = pd.DataFrame(data)

    # Salvar os dados em um arquivo CSV
    df.to_csv('output.csv', index=False, header=False)
    print("Dados extraídos e salvos em 'output.csv'.")

else:
    print("Erro ao acessar a URL:", response.status_code)
 
