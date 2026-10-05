import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 🔑 Insira sua chave real da API-Sports (Fórmula 1)
API_KEY = "7b393b923c767255d2e72ca58542ebff"
BASE_URL = "https://v1.formula-1.api-sports.io"
HEADERS = {"x-apisports-key": API_KEY}

def buscar_dados_endpoint(endpoint, params=None):
    """Função genérica para buscar dados na API de F1."""
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url, headers=HEADERS, params=params)
    
    print(f"Status da API para /{endpoint}: {response.status_code}")
    
    if response.status_code == 200:
        resposta_json = response.json()
        # A API-Sports costuma entregar os dados dentro da chave 'response'
        return resposta_json.get("response", [])
    else:
        print(f"Erro na API: {response.text}")
    return []

# ==========================================
# DESAFIO 2: Rankings e Médias (Ranking de Pilotos)
# ==========================================
print("--- Executando Desafio 2: Ranking de Pilotos na F1 ---")

# Buscando o ranking de pilotos da temporada de 2024
ranking_pilotos = buscar_dados_endpoint("rankings/drivers", {"season": 2024})

df_ranking = pd.DataFrame() # Cria um DataFrame vazio por segurança

if ranking_pilotos:
    lista_processada = []
    for item in ranking_pilotos:
        # Extraindo informações seguras do JSON da F1
        driver_info = item.get("driver", {})
        nome_piloto = driver_info.get("name", "Desconhecido")
        posicao = item.get("position")
        pontos = item.get("points")
        
        lista_processada.append({
            "Piloto": nome_piloto,
            "Posição": posicao,
            "Pontos": pontos if pontos is not None else 0
        })
    
    if lista_processada:
        df_ranking = pd.DataFrame(lista_processada)
        df_ranking = df_ranking.sort_values(by="Pontos", ascending=False).reset_index(drop=True)
        print("\nRanking de Pilotos:")
        print(df_ranking.head(10))
else:
    print("[Aviso] Nenhum dado retornado para o ranking de pilotos.")
# ==========================================
# DESAFIO 1: Comparação de mais pilotos
# ==========================================
print("\n--- Executando Desafio 1: Comparação de Desempenho ---")

if not df_ranking.empty:
    # Opção A: Pegar automaticamente os 5 primeiros colocados do ranking
    pilotos_comparacao = df_ranking.head(10)
    
    # (Opcional) Opção B: Se preferir escolher nomes específicos, basta adicionar na lista:
    # nomes_escolhidos = ["Max Verstappen", "Lewis Hamilton", "Charles Leclerc", "Lando Norris", "Oscar Piastri"]
    # pilotos_comparacao = df_ranking[df_ranking["Piloto"].isin(nomes_escolhidos)]

    if not pilotos_comparacao.empty:
        # Aumentamos um pouco a largura da figura (figsize) para caberem mais barras
        plt.figure(figsize=(12, 6))
        
        # Gerando o gráfico com Seaborn
        sns.barplot(data=pilotos_comparacao, x="Piloto", y="Pontos", palette="viridis")
        
        plt.title("Comparação de Pontuação: Top Pilotos (Temporada 2024)")
        plt.xlabel("Piloto")
        plt.ylabel("Pontos na Temporada")
        
        # Rotaciona os nomes dos pilotos caso fiquem compridos
        plt.xticks(rotation=15)
        
        plt.show()
    else:
        print("Nenhum piloto encontrado para comparação.")
else:
    print("Não foi possível executar o Desafio 1 pois o ranking está vazio.")