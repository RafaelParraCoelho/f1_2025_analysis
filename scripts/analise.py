import pandas as pd
import matplotlib.pyplot as plt

def load_data(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename)
    df["Points"] = pd.to_numeric(df["Points"], errors="coerce")
    return df

def plot_points_per_pilot(df: pd.DataFrame):
    df.plot(kind="bar", x="Driver", y="Points", color="crimson", legend=False)
    plt.title("Pontuação dos Pilotos - Temporada 2025")
    plt.xlabel("Piloto")
    plt.ylabel("Pontos")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_teams(df: pd.DataFrame):
    if "Team" not in df.columns:
        return "No `Teams` column in provided DataFrame."
    df.groupby("Team")["Points"].sum().sort_values(ascending=False).plot(kind="bar", color="skyblue")
    plt.title("Pontuação por Equipe - Temporada 2025")
    plt.ylabel("Total de Pontos")
    plt.xlabel("Equipe")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
