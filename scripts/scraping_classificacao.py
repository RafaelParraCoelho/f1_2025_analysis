import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL da temporada 2025
url = "https://en.wikipedia.org/wiki/2025_Formula_One_World_Championship"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Busca todas as tabelas da página
tables = soup.find_all('table', class_='wikitable')
print(f"{len(tables)} tabelas encontradas.")

standings_df = None

# Busca tabela com 'Pos', 'Driver' e 'Points'/'PTS'
for idx, table in enumerate(tables):
    headers_raw = table.find_all('tr')[0].find_all(['th', 'td'])
    headers = [th.get_text(strip=True).lower() for th in headers_raw]

    if any(h.startswith("pos") for h in headers) and any("driver" in h for h in headers) and any(h in ["points", "pts"] for h in headers):
        print(f"Tabela de classificação encontrada no índice {idx}")
        rows = table.find_all("tr")[1:]
        data = []

        for row in rows:
            cells = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
            if len(cells) >= len(headers):
                data.append(cells[:len(headers)])

        standings_df = pd.DataFrame(data, columns=headers)
        break

# Se achou a tabela, salva
if standings_df is not None:
    # Normaliza nomes de colunas
    col_map = {col: col.capitalize() for col in standings_df.columns}
    if "pts" in col_map: col_map["pts"] = "Points"
    if "points" in col_map: col_map["points"] = "Points"
    if "pos" in col_map: col_map["pos"] = "Pos"
    if "driver" in col_map: col_map["driver"] = "Driver"

    standings_df.rename(columns=col_map, inplace=True)

    if "Points" in standings_df.columns:
        standings_df["Points"] = pd.to_numeric(standings_df["Points"], errors="coerce")

    os.makedirs("data", exist_ok=True)
    standings_df.to_csv("data/f1_pilotos_classificacao_2025.csv", index=False)
    print("CSV salvo como 'data/f1_pilotos_classificacao_2025.csv'")
    print(standings_df.head())
else:
    print("Tabela de classificação não encontrada.")
