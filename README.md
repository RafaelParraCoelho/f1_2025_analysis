# Formula 1 - 2025 Season Analysis

This project collects data from the 2025 Formula 1 season using Wikipedia, saves standings and race calendar into CSV files, and generates visualizations for drivers' and teams' scores.

## Features

- Automatic scraping of driver standings (positions and points).
- Scraping of race calendar (dates and circuits).
- Score visualization through charts for both drivers and teams.

## Project Structure

- `scripts/scraping_classificacao.py`: Fetches and saves driver standings.
- `scripts/scraping_corridas.py`: Fetches and saves race calendar data.
- `scripts/analise.py`: Reads the CSVs and generates charts for analysis.

## How to Use

1. Clone this repository.
2. Install the dependencies:

```bash
pip install requests beautifulsoup4 pandas matplotlib
```