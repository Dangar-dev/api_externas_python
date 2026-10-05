## Guia para    listar Esportes usando a API FORMULA 1 

# Pegue sua chave api aqui : https://dashboard.api-football.com

# usaremos o endpoint : https://v1.formula-1.api-sports.io


# Chame  o arquivo : python api_sports.py  

# Formas de usar:
   # Opção A: Pegar automaticamente os 5 primeiros colocados do ranking
# pilotos_comparacao = df_ranking.head(10)
    
# (Opcional) Opção B: Se preferir escolher nomes específicos, basta adicionar na lista:
# nomes_escolhidos = ["Max Verstappen", "Lewis Hamilton", "Charles Leclerc", "Lando Norris", "Oscar Piastri"]
# pilotos_comparacao = df_ranking[df_ranking["Piloto"].isin(nomes_escolhidos)]
