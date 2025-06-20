import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados
df = pd.read_csv("data/f1_pilotos_classificacao_2025.csv")

# Converte pontos
df["Points"] = pd.to_numeric(df["Points"], errors="coerce")

# Exibe top 5
print("Top 5 pilotos por pontuação:")
print(df[["Driver", "Points"]].head())

# Gráfico de pontuação por piloto
df.plot(kind="bar", x="Driver", y="Points", color="crimson", legend=False)
plt.title("Pontuação dos Pilotos - Temporada 2025")
plt.xlabel("Piloto")
plt.ylabel("Pontos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# (Opcional) gráfico por equipe se houver coluna 'Team'
if "Team" in df.columns:
    df.groupby("Team")["Points"].sum().sort_values(ascending=False).plot(kind="bar", color="skyblue")
    plt.title("Pontuação por Equipe - Temporada 2025")
    plt.ylabel("Total de Pontos")
    plt.xlabel("Equipe")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
