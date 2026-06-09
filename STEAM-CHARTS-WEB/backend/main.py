from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.steam import router as steam_router
import uvicorn

# Criar app FastAPI
app = FastAPI(
    title="SteamCharts API",
    description="API para análise de dados de jogadores da Steam",
    version="1.0.0"
)

# Configurar CORS para aceitar requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique os domínios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas
app.include_router(steam_router)


@app.get("/")
async def root():
    """Rota raiz da API"""
    return {
        "message": "SteamCharts API",
        "version": "1.0.0",
        "docs": "/docs"
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
