import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/2025_Formula_One_World_Championship"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table", class_="wikitable")
print(f"{len(tables)} tabelas encontradas.")

df_corridas = None

for idx, table in enumerate(tables):
    headers = [th.get_text(strip=True).lower() for th in table.find_all("tr")[0].find_all("th")]
    # Agora busca "grand prix", "circuit" e "race date"
    if "grand prix" in headers and "circuit" in headers and "race date" in headers:
        print(f"Tabela de calendário encontrada no índice {idx}")
        rows = table.find_all("tr")[1:]
        data = []
        for row in rows:
            cells = [cell.get_text(strip=True).replace("\xa0", " ") for cell in row.find_all(["th", "td"])]
            if len(cells) >= len(headers):
                data.append(cells[:len(headers)])
        df_corridas = pd.DataFrame(data, columns=headers)
        break

if df_corridas is None:
    print("Tabela de calendário não encontrada.")
else:
    os.makedirs("data", exist_ok=True)
    df_corridas.rename(columns={
        "round": "Round",
        "grand prix": "Grand Prix",
        "circuit": "Circuit",
        "race date": "Race date"
    }, inplace=True)
    df_corridas.to_csv("data/f1_corridas_2025.csv", index=False)
    print("CSV salvo como 'data/f1_corridas_2025.csv'")
    print(df_corridas.head())
