# SteamCharts Web Application

Uma aplicação web moderna para análise de dados de jogadores ativos da Steam.

**Frontend**: Angular + TailwindCSS (Dark Mode)  
**Backend**: FastAPI + Python

## 📁 Estrutura do Projeto

```
STEAM-CHARTS-WEB/
├── backend/              # API FastAPI (Python)
│   ├── main.py          # Aplicação principal
│   ├── requirements.txt  # Dependências Python
│   ├── models/          # Schemas Pydantic
│   ├── routes/          # Endpoints da API
│   └── services/        # Lógica de negócio
├── frontend/            # Aplicação Angular
│   ├── src/
│   ├── package.json
│   └── angular.json
└── README.md
```

## 🚀 Quick Start

### Backend (Terminal 1)

```bash
cd backend
pip install -r requirements.txt
python main.py
```

Backend rodando em: `http://localhost:8000`

### Frontend (Terminal 2)

```bash
cd frontend
npm install
ng serve
```

Frontend rodando em: `http://localhost:4200`

## 📡 API Endpoints

- `GET /` - Status da API
- `GET /api/steam/health` - Health check
- `POST /api/steam/fetch?app_id=730` - Buscar dados
- `POST /api/steam/graph` - Gerar gráfico
- `GET /api/steam/history` - Histórico
- `DELETE /api/steam/cache` - Limpar cache

**Docs Interativa**: http://localhost:8000/docs

## 🎨 Características

✅ Dark Theme estilo Steam  
✅ Gráficos interativos (Chart.js)  
✅ Histórico de buscas em memória  
✅ API REST completa  
✅ Responsivo (mobile-friendly)  
✅ Validação de dados com Pydantic  

## 🛠️ Tecnologias

### Backend
- FastAPI
- Uvicorn
- Requests
- BeautifulSoup4
- Pydantic

### Frontend
- Angular 17+
- TypeScript
- TailwindCSS
- Chart.js
- RxJS

## 📝 Desenvolvimento

Ambas as aplicações têm auto-reload habilitado durante desenvolvimento.

Para parar os servidores: `CTRL+C`

## 📄 Licença

MIT
