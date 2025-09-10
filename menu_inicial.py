from tkinter import Button, Label, messagebox

class MenuInicial:
    def __init__(self, root):
        self.root = root
        self.root.title("SteamCharts Tool - Menu Inicial")
        self.root.minsize(300, 200)

        Label(root, text="Bem-vindo ao SteamDB Análises!", font=("Arial", 14)).pack(pady=10)

        Button(root, text="Gerar Gráfico de Jogadores", command=self.abrir_grafico).pack(pady=5)
        Button(root, text="Configurações", command=self.abrir_configuracoes).pack(pady=5)
        Button(root, text="Sair", command=root.quit).pack(pady=5)

    def abrir_grafico(self):
        self.root.destroy()
        from SteamDBAnalises import SteamDBAnalises
        SteamDBAnalises()  # abre a tela principal

    def abrir_configuracoes(self):
        messagebox.showinfo("Configurações", "Menu de configurações em desenvolvimento.")
