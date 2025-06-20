# Fórmula 1 - Análise da Temporada 2025

Este projeto coleta dados da temporada 2025 de Fórmula 1 da Wikipedia, salva as classificações e o calendário em arquivos CSV, e gera gráficos para visualização da pontuação dos pilotos e equipes.

## Funcionalidades

- Scraping automático da classificação dos pilotos (posições e pontos).
- Scraping do calendário de corridas (datas, circuitos).
- Geração de gráficos da pontuação por piloto e por equipe.

## Estrutura do Projeto

- `scripts/scraping_classificacao.py`: Puxa e salva dados de classificação dos pilotos.
- `scripts/scraping_corridas.py`: Puxa e salva o calendário de corridas.
- `scripts/analise.py`: Lê os CSVs e gera gráficos para visualização.

## Como usar

1. Clone este repositório.
2. Instale as dependências:

```bash
pip install requests beautifulsoup4 pandas matplotlib
 
