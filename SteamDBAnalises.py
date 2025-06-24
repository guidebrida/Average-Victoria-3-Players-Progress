import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# ======= INPUT DO USUÁRIO =======
app_id = input("Enter the Steam App ID (example: 529340 for Victoria 3): ").strip()
start_month = input("Enter the starting month (example: Jan 2023): ").strip()

# ======= SCRAPING FROM STEAMCHARTS =======
url = f'https://steamcharts.com/app/{app_id}#All'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'common-table'})

meses = []
jogadores_medios = []

if table:
    rows = table.find_all('tr')[1:]  # Ignore table header
    for row in rows:
        columns = row.find_all('td')
        if columns:
            month = columns[0].text.strip()
            avg_players = columns[1].text.strip().replace(',', '')
            if avg_players and avg_players != '-':
                meses.append(month)
                jogadores_medios.append(float(avg_players))

# ======= FILTRAR A PARTIR DA DATA DESEJADA =======
if start_month in meses:
    start_index = meses.index(start_month)
    meses_filtrados = meses[start_index:]
    jogadores_filtrados = jogadores_medios[start_index:]
else:
    print(f"Start month '{start_month}' not found in data. Showing all available data.")
    meses_filtrados = meses
    jogadores_filtrados = jogadores_medios

# ======= GERAR O GRÁFICO =======
plt.figure(figsize=(12, 6))
plt.plot(meses_filtrados, jogadores_filtrados, marker='o', color='blue', linewidth=2)
plt.title(f'Average Players Progress - Steam AppID: {app_id}')
plt.xlabel('Month')
plt.ylabel('Average Players')
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()
