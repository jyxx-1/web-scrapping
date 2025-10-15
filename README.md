# Web-scrapping 📚🐍

## 🇧🇷 Português

Este projeto visa o entendimento do web-scrapping. Utilizando uma analogia básica do robô cansado de copiar e colar:
Imagine que você quer criar uma planilha com o nome e o preço de todos os videogames da primeira página de um site de vendas.

O jeito manual: Você abre o site, encontra o primeiro videogame, seleciona o nome, `Ctrl+C`. Vai para a sua planilha, `Ctrl+V`. Volta pro site, seleciona o preço, `Ctrl+C`. Vai para a planilha, `Ctrl+V`. Repete isso para o segundo, o terceiro... o quinquagésimo videogame. Chato, né? Lento, cansativo e fácil de cometer erros.

O jeito Web Scraping: Agora, imagine que você pode programar um "robô" (um script em Python) e dar a ele uma única ordem: "Robô, vá até este site, encontre a área onde estão os videogames e, para cada um deles, pegue o nome e o preço e me traga tudo organizado em uma lista."

O robô faz isso em segundos, sem reclamar e sem erros.

### Descrição do Projeto
Este é um script em Python que realiza web scraping no portal CERT.br para coletar as publicações mais recentes sobre segurança digital. Ele extrai título, resumo e link de cada publicação, realiza um processo de limpeza dos dados textuais, corrige links relativos e, por fim, exibe as informações de forma organizada em uma tabela utilizando a biblioteca Pandas.

## 🇺🇸 English

This project aims to understand web scraping. Using a basic analogy of the tired copy-paste robot:

Imagine you want to create a spreadsheet with the name and price of every video game on the front page of a retail website.

The manual way: You open the site, find the first video game, select the name, `Ctrl+C`. You go to your spreadsheet, `Ctrl+V`. You go back to the site, select the price, `Ctrl+C`. You go to the spreadsheet, `Ctrl+V`. You repeat this for the second, the third... the fiftieth video game. It's tedious, right? Slow, tiring, and prone to errors.

The Web Scraping way: Now, imagine you can program a "robot" (a Python script) and give it a single command: "Robot, go to this website, find the area where the video games are, and for each one, grab the name and the price and bring them all back to me in an organized list."

The robot does this in seconds, without complaining and without errors.

### Project Description
This is a Python script that performs web scraping on the CERT.br portal to collect the latest publications on digital security. It extracts the title, summary, and link for each publication, performs a cleaning process on the textual data, corrects relative links, and finally, displays the information in an organized table using the Pandas library.

---

# 🚀 Funcionalidades Principais (Features)
✅ Coleta automatizada de dados do portal de publicações do CERT.br.

✅ Extração de informações específicas: Título, resumo e link de cada artigo.

✅ Limpeza e tratamento dos dados para remover quebras de linha e espaços desnecessários.

✅ Correção automática de links relativos para links absolutos e funcionais.

✅ Apresentação profissional dos dados em um DataFrame (tabela) com Pandas.

# 🛠️ Tecnologias Utilizadas (Tech Stack)
Linguagem: Python

Bibliotecas:

`requests` para realizar as requisições HTTP.

`Beautiful Soup 4` para fazer o parse do HTML.

`Pandas` para a estruturação e exibição dos dados.

---

⚙️ Como Executar o Projeto (Getting Started)
Siga os passos abaixo para executar o projeto em sua máquina local.

### 1. Clone o Repositório
- git clone https://github.com/jyxx-1/web-scrapping.git
- cd web-scrapping.git

### 2. Crie e Ative o Ambiente Virtual (venv)
- `python -m venv venv`
### 2.1 Ative o Ambiente Virtual (venv)
* Windows:
- `venv\Scripts\activate`
* macOS/Linux:
- `source venv/bin/activate`

### 3. Instale as Dependências

Este projeto utiliza as bibliotecas requests, beautifulsoup4 e pandas. Instale as dependências a partir do arquivo com o comando:

`pip install -r requirements.txt`

### 4. Execute o Script

Para rodar o scraper e ver o relatório de publicações, execute o seguinte comando no terminal:

`python scraper.py`

---

# 📫 Contato
Em caso de dúvidas ou sugestões, entre em contato!

- LinkedIn: [João Massari](https://www.linkedin.com/in/joao-paulo-massari-382604278)

- Instagram: @massarii07
