# 🚀 Como Rodar a Aplicação Completa

Esta é uma aplicação full-stack com **Frontend Angular** e **Backend FastAPI**.

## ⚡ Quick Start (2 Terminais)

### Terminal 1: Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
python main.py
```
✅ Backend rodando em: `http://localhost:8000`  
📚 Docs: `http://localhost:8000/docs`

### Terminal 2: Frontend (Angular)
```bash
cd frontend
npm install
npm start
```
✅ Frontend rodando em: `http://localhost:4200`

---

## 📋 Pré-requisitos

- **Node.js** 18+ e **npm**
- **Python** 3.8+

### Verificar instalações:
```bash
node --version
npm --version
python --version
```

---

## 📁 Estrutura

```
STEAM-CHARTS-WEB/
├── backend/              # FastAPI + Python
│   ├── main.py
│   ├── requirements.txt
│   ├── routes/
│   ├── models/
│   ├── services/
│   └── README.md
├── frontend/             # Angular + TypeScript
│   ├── src/
│   ├── package.json
│   ├── angular.json
│   └── README.md
└── README.md
```

---

## 🔧 Instalação Detalhada

### 1. Backend

```bash
# Navegar para o diretório
cd backend

# Criar ambiente virtual (opcional mas recomendado)
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Rodar servidor
python main.py
```

### 2. Frontend

```bash
# Navegar para o diretório
cd frontend

# Instalar dependências
npm install

# Rodar servidor
npm start
```

---

## ✅ Verificação

1. **Backend** - Acesse: `http://localhost:8000`
   - Deve retornar: `{"message": "SteamCharts API"}`

2. **Frontend** - Acesse: `http://localhost:4200`
   - Deve mostrar a interface com o logo SteamCharts

3. **API Docs** - Acesse: `http://localhost:8000/docs`
   - Interface interativa Swagger da API

---

## 🧪 Testando a Aplicação

1. Insira um **App ID** válido (ex: `730` para CS:GO)
2. Clique em **Carregar Dados**
3. Escolha a **Ordem** (Cronológica ou Invertida)
4. Selecione o **Período**
5. Clique em **Gerar Gráfico**

### App IDs Populares para Teste:
- `570` - Dota 2
- `730` - CS:GO
- `1091500` - Cyberpunk 2077
- `1313860` - Ready or Not
- `105600` - Terraria

---

## 🛑 Parando os Serviços

- Press `CTRL + C` em cada terminal

---

## 🐛 Troubleshooting

### "Port already in use"
Se a porta 8000 ou 4200 já estiver em uso:

**Backend:**
```bash
python main.py --port 8001
```

**Frontend:**
```bash
ng serve --port 4201
```

### CORS Error
Certifique-se de que ambos os servidores estão rodando.

### Módulos não encontrados
```bash
# Backend
pip install -r requirements.txt

# Frontend
npm install
```

---

## 📞 Endpoints principais

- `POST /api/steam/fetch?app_id=730` - Buscar dados
- `POST /api/steam/graph` - Gerar gráfico
- `GET /api/steam/history` - Histórico de buscas
- `GET /api/steam/health` - Status do backend

---

## 🎯 Características

✅ Dark Theme estilo Steam  
✅ Gráficos interativos  
✅ Histório de buscas  
✅ API REST com validação  
✅ Responsivo (mobile)  
✅ Auto-reload em desenvolvimento  

---

## 📚 Documentação

- [Backend README](./backend/README.md)
- [Frontend README](./frontend/README.md)

---

**Enjoy! 🎮**
