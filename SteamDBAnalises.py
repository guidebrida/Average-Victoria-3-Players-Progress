import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, messagebox, StringVar
from tkinter.ttk import Combobox

def fetch_data(app_id):
    url = f'https://steamcharts.com/app/{app_id}#All'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    meses = []
    jogadores_medios = []

    table = soup.find('table', {'class': 'common-table'})
    if not table:
        return None, None

    rows = table.find_all('tr')[1:]
    for row in rows:
        columns = row.find_all('td')
        if columns:
            month = columns[0].text.strip()
            avg_players = columns[1].text.strip().replace(',', '')
            if avg_players and avg_players != '-':
                meses.append(month)
                jogadores_medios.append(float(avg_players))

    return meses, jogadores_medios

def load_months():
    app_id = app_id_entry.get().strip()
    if not app_id.isdigit():
        messagebox.showerror("Invalid App ID", "Please enter a valid numeric Steam App ID.")
        return

    global meses, jogadores_medios
    meses, jogadores_medios = fetch_data(app_id)

    if not meses:
        messagebox.showerror("Data Error", "Could not fetch data or no data available for this AppID.")
        return

    # Popula comboboxes com meses em ordem cronológica (do mais antigo ao mais recente)
    start_month_combo['values'] = meses
    end_month_combo['values'] = meses

    # Valores padrão: mês mais antigo e mês mais recente
    start_month_var.set(meses[0])
    end_month_var.set(meses[-1])

    messagebox.showinfo("Success", f"Months loaded for AppID {app_id}. Now select range and generate graph.")

def generate_graph():
    start_month = start_month_var.get()
    end_month = end_month_var.get()

    if start_month not in meses or end_month not in meses:
        messagebox.showerror("Date Error", "Selected months are not available in the data.")
        return

    start_index = meses.index(start_month)
    end_index = meses.index(end_month) + 1

    print(start_index)
    print(end_index)
    if start_index >= end_index:
        messagebox.showerror("Invalid Range", "Start month must come before end month.")
        return

    meses_filtrados = meses[start_index:end_index]
    jogadores_filtrados = jogadores_medios[start_index:end_index]

    plt.figure(figsize=(12, 6))
    plt.plot(meses_filtrados, jogadores_filtrados, marker='o', color='blue', linewidth=2)
    plt.title(f'Average Players Progress - Steam AppID: {app_id_entry.get().strip()}')
    plt.xlabel('Month')
    plt.ylabel('Average Players')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# === Tkinter GUI ===
root = Tk()
root.title("SteamCharts Player Graph")

# Define tamanho mínimo da janela
root.minsize(400, 200)

# AppID
Label(root, text="Steam App ID:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
app_id_entry = Entry(root, width=25)
app_id_entry.grid(row=0, column=1, padx=5, pady=5)

# Load Months Button
Button(root, text="Load Months", command=load_months).grid(row=1, column=0, columnspan=2, pady=5)

# Start Month
Label(root, text="Start Month:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
start_month_var = StringVar()
start_month_combo = Combobox(root, textvariable=start_month_var, state='readonly', width=22)
start_month_combo.grid(row=2, column=1, padx=5, pady=5)

# End Month
Label(root, text="End Month:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
end_month_var = StringVar()
end_month_combo = Combobox(root, textvariable=end_month_var, state='readonly', width=22)
end_month_combo.grid(row=3, column=1, padx=5, pady=5)

# Generate Graph
Button(root, text="Generate Graph", command=generate_graph).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
