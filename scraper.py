import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Definir o endereço do alvo.

url_alvo = "https://www.cert.br/docs/"

print(f"Iniciando investigação para o alvo: {url_alvo}")

# 1.1 Uso de um bloco try-except para lidar com possíveis erros de conexão.

try:
    # Enviamos o "agente" (requests.get) para a URL.
    # O timeout (em segundos) evita que nosso programa fique "preso" para sempre
    # se o site demorar muito para responder.

    resposta = requests.get(url_alvo, timeout=10)

    # Verificar o "status code" da resposta.
    # Código 200 significa êxito!

    if resposta.status_code == 200:
        print("Sucesso! ✔ O agente se conectou ao servidor.")

        # 1.2 Guardar o conteúdo da página (HTML completo) em uma variável.
        html_pagina = resposta.text
        print("O código HTML foi baixado com sucesso! ✔")
        print("-" * 30)
        # Linha de baixo 👇 se caso queira ver parte do HTML da página. Apenas "descomentar".
        # print(html_pagina[:500])

        # 2 Entregar o HTML para a biblioteca BeautifulSoup analisar.

        sopa = BeautifulSoup(html_pagina, "html.parser")

        # 2.1 Pedir a "sopa" encontrar TODAS as divs com a classe
        # Aqui é onde, dependendo do site alvo, precisaremos alterar conforme a estrutura HTML da página.

        publicacoes = sopa.find_all("div", class_="content-respostas")

        # 2.2 Armazenar estruturas numa lista.

        lista_publicacoes = []

        print(
            f"Encontradas {len(publicacoes)} publicações na página. Iniciando extração... ☢"
        )

        # 3 Criar um loop para percorrer todas as publicações.

        for pub in publicacoes:
            # Para cada "pub", procuramos as tags identificadoras.
            titulo_bruto = pub.find("h3", class_="title").text
            resumo_bruto = pub.find("p").text
            # Pequena alteração na estrutura para o resultado visual ficar melhor.
            titulo_limpo = ' '.join(titulo_bruto.split())
            resumo_limpo = ' '.join(resumo_bruto.split())

            link_bruto = pub.find("a")["href"]
            # Pequena verificação de URL incompleta
            if link_bruto.startswith("/"):
                link_completo = f"https://www.cert.br{link_bruto}"
            else:
                link_completo = link_bruto

            # 3.1 Após percorrer as informações tronco, organizaremos num dicionário.

            info_pubs = {"titulo": titulo_limpo, "resumo": resumo_limpo, "link": link_completo}

            # 3.2 Por fim, adicionamos o dicionário na lista principal.

            lista_publicacoes.append(info_pubs)

        # 4 Se tudo correr bem, exibirá mensagem:

        print("Extração finalizada com sucesso!")
        print("-" * 30)

        # 5 Gerar o relatório estruturado dos resultados obtidos na extração de dados.

        print("\n--- 📰 RELATÓRIO DE PUBLICAÇÕES DE CIBERSEGURANÇA 📰 ---\n")

        # 5.1 Estruturação dos dados usando Pandas.
        # Conversão da lista em um DataFrame com ajustes para colunas ficarem simétricas.

        df_pubs = pd.DataFrame(lista_publicacoes)
        pd.set_option("display.max_rows", 50)
        pd.set_option("display.max_columns", 5)
        pd.set_option("display.width", 150)
        pd.set_option("display.max_colwidth", 100)

        # 5.2 Exibir o DataFrame.

        print(df_pubs)

        # 5.3 - EXTRA - Se for necessário salvar em um arquivo CSV -> descomentar linhas abaixo.

        # df_pubs.to_csv('publicacoes_cert.csv', index=False)
        # print("\nRelatório salvo em 'publicacoes_cert.csv'")

    else:
        print(f"Erro! ❌ O servidor respondeu com o código: {resposta.status_code}")

except requests.exceptions.RequestException as e:
    print(f"O agente não conseguiu se conectar com o alvo. ❌")
    print(f"Erro: {e}")
