# Backend Flask/FastAPI

Este é o backend da aplicação SteamCharts desenvolvido com **FastAPI** em Python.

## 📋 Estrutura

```
backend/
├── main.py              # Aplicação FastAPI
├── requirements.txt     # Dependências Python
├── models/
│   └── schemas.py       # Modelos Pydantic
├── routes/
│   └── steam.py         # Rotas da API
└── services/
    └── steam_service.py # Lógica de negócio
```

## 🚀 Como Executar

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Rodar o servidor
```bash
python main.py
```

O servidor estará disponível em `http://localhost:8000`

### 3. Documentação interativa
Acesse `http://localhost:8000/docs` para a documentação Swagger

## 📡 Endpoints

- `GET /api/steam/health` - Verificar status do backend
- `POST /api/steam/fetch?app_id=730` - Buscar dados de um jogo
- `POST /api/steam/graph` - Gerar dados para gráfico
- `GET /api/steam/history` - Obter histórico de buscas
- `DELETE /api/steam/cache` - Limpar cache

## 🔧 Tecnologias

- **FastAPI** - Framework web moderno
- **Uvicorn** - Servidor ASGI
- **Pydantic** - Validação de dados
- **BeautifulSoup** - Web scraping
- **Requests** - HTTP requests
