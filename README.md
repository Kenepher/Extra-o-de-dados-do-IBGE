# IBGE Data Extraction Project

Este projeto em Python foi desenvolvido para extrair dados dos municípios brasileiros disponíveis no site do [IBGE](https://www.ibge.gov.br/explica/codigos-dos-municipios.php) e salvá-los em um arquivo CSV.

## Descrição

Este script realiza uma requisição HTTP para a página de códigos dos municípios brasileiros no site do IBGE, extrai os dados da tabela disponível na página e os salva em um arquivo CSV (`output.csv`). Os dados extraídos incluem informações sobre o código e o nome dos municípios.

### Ferramentas utilizadas:
- **requests**: Para fazer a requisição HTTP.
- **BeautifulSoup (bs4)**: Para fazer o parsing do conteúdo HTML.
- **pandas**: Para manipulação e exportação dos dados.

## Requisitos

Antes de rodar o script, certifique-se de que as seguintes bibliotecas estão instaladas:

```bash
pip install requests beautifulsoup4 pandas
```
## Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/ibge-data-extraction.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd ibge-data-extraction
   ```
3. Execute o script:
   ```bash
   python extract_ibge_data.py
   ```
4. O arquivo CSV (output.csv) contendo os dados extraídos será gerado no diretório do projeto.

## Estrutura do Projeto
```
ibge-data-extraction/
│
├── extract_ibge_data.py   # Script principal para extração dos dados
├── output.csv             # Arquivo CSV gerado após a execução do script
└── README.md              # Arquivo com informações sobre o projeto
```

## Exemplo de Saída
O arquivo output.csv conterá informações como:
```
Código, Município
1100015, Alta Floresta D'Oeste
1100023, Ariquemes
...
```

## Erro Comuns
- Se o site do IBGE estiver fora do ar ou o endereço da URL mudar, o código retornará uma mensagem de erro com o status HTTP.

## Contribuições
Sinta-se à vontade para abrir issues e enviar pull requests!
