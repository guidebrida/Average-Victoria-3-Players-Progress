from fastapi import APIRouter, HTTPException
from typing import List
from models.schemas import GraphRequest, GraphResponse, SearchHistory
from services.steam_service import SteamService

router = APIRouter(prefix="/api/steam", tags=["steam"])


@router.get("/health")
async def health_check():
    """Verifica se o backend está online"""
    return {"status": "ok"}


@router.post("/fetch")
async def fetch_game_data(app_id: str):
    """Busca dados de um jogo na Steam"""
    if not app_id.isdigit():
        raise HTTPException(status_code=400, detail="App ID deve ser numérico")
    
    months, avg_players, game_name = SteamService.fetch_data(app_id)
    
    if not months:
        raise HTTPException(
            status_code=404, 
            detail=f"Não foi possível obter dados para o App ID {app_id}"
        )
    
    return {
        "app_id": app_id,
        "game_name": game_name,
        "months": months,
        "avg_players": avg_players,
        "total_months": len(months)
    }


@router.post("/graph")
async def generate_graph(request: GraphRequest) -> GraphResponse:
    """Gera dados filtrados para o gráfico"""
    
    months, avg_players, game_name = SteamService.fetch_data(request.app_id)
    
    if not months:
        raise HTTPException(status_code=404, detail="Dados não encontrados")
    
    # Encontrar índices
    if request.start_month not in months or request.end_month not in months:
        raise HTTPException(status_code=400, detail="Meses não encontrados nos dados")
    
    start_index = months.index(request.start_month)
    end_index = months.index(request.end_month)
    
    # Filtrar dados
    if request.chronological:
        start_index, end_index = sorted([start_index, end_index])
        end_index += 1
        filtered_months = months[start_index:end_index]
        filtered_players = avg_players[start_index:end_index]
    else:
        start_index, end_index = sorted([start_index, end_index], reverse=True)
        filtered_months = list(reversed(months[end_index:start_index + 1]))
        filtered_players = list(reversed(avg_players[end_index:start_index + 1]))
    
    return GraphResponse(
        app_id=request.app_id,
        game_name=game_name,
        months=filtered_months,
        avg_players=filtered_players,
        start_month=request.start_month,
        end_month=request.end_month,
        chronological=request.chronological
    )


@router.get("/history")
async def get_search_history() -> List[SearchHistory]:
    """Retorna o histórico de buscas"""
    return SteamService.get_history()


@router.delete("/cache")
async def clear_cache():
    """Limpa o cache"""
    SteamService.clear_cache()
    return {"message": "Cache limpo com sucesso"}
