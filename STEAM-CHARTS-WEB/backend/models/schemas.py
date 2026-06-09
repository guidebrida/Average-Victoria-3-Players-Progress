from pydantic import BaseModel
from typing import List, Optional


class SteamGameData(BaseModel):
    """Schema para dados do jogo"""
    app_id: str
    months: List[str]
    avg_players: List[float]
    game_name: Optional[str] = None


class GraphRequest(BaseModel):
    """Schema para requisição de gráfico"""
    app_id: str
    start_month: str
    end_month: str
    chronological: bool = True


class GraphResponse(BaseModel):
    """Schema para resposta do gráfico"""
    app_id: str
    game_name: Optional[str] = None
    months: List[str]
    avg_players: List[float]
    start_month: str
    end_month: str
    chronological: bool


class SearchHistory(BaseModel):
    """Schema para histórico de busca"""
    app_id: str
    game_name: Optional[str] = None
    timestamp: str
    total_months: int
