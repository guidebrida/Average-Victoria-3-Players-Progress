import requests
from bs4 import BeautifulSoup
from typing import Tuple, Optional, List
from datetime import datetime


class SteamService:
    """Serviço para buscar dados da Steam"""
    
    BASE_URL = "https://steamcharts.com/app"
    SEARCH_HISTORY = []
    CACHE = {}
    
    @staticmethod
    def fetch_data(app_id: str) -> Tuple[Optional[List[str]], Optional[List[float]], Optional[str]]:
        """
        Busca dados de um App ID da Steam via SteamCharts
        
        Returns:
            Tuple[months, avg_players, game_name]
        """
        # Verificar cache
        if app_id in SteamService.CACHE:
            cached = SteamService.CACHE[app_id]
            return cached['months'], cached['avg_players'], cached['game_name']
        
        try:
            url = f'{SteamService.BASE_URL}/{app_id}#All'
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Tentar extrair nome do jogo
            game_name = None
            title_elem = soup.find('h1')
            if title_elem:
                game_name = title_elem.text.strip()
            
            meses = []
            jogadores_medios = []
            
            table = soup.find('table', {'class': 'common-table'})
            if not table:
                return None, None, None
            
            rows = table.find_all('tr')[1:]
            for row in rows:
                columns = row.find_all('td')
                if columns:
                    month = columns[0].text.strip()
                    avg_players = columns[1].text.strip().replace(',', '')
                    if avg_players and avg_players != '-':
                        meses.append(month)
                        jogadores_medios.append(float(avg_players))
            
            if not meses:
                return None, None, None
            
            # Armazenar em cache
            SteamService.CACHE[app_id] = {
                'months': meses,
                'avg_players': jogadores_medios,
                'game_name': game_name
            }
            
            # Adicionar ao histórico
            SteamService.add_to_history(app_id, game_name, len(meses))
            
            return meses, jogadores_medios, game_name
            
        except Exception as e:
            print(f"Erro ao buscar dados: {str(e)}")
            return None, None, None
    
    @staticmethod
    def add_to_history(app_id: str, game_name: Optional[str], total_months: int):
        """Adiciona à história de busca"""
        history_item = {
            'app_id': app_id,
            'game_name': game_name,
            'timestamp': datetime.now().isoformat(),
            'total_months': total_months
        }
        
        # Remover duplicatas antigas
        SteamService.SEARCH_HISTORY = [
            h for h in SteamService.SEARCH_HISTORY 
            if h['app_id'] != app_id
        ]
        
        # Adicionar no início
        SteamService.SEARCH_HISTORY.insert(0, history_item)
        
        # Manter apenas últimas 20 buscas
        SteamService.SEARCH_HISTORY = SteamService.SEARCH_HISTORY[:20]
    
    @staticmethod
    def get_history():
        """Retorna o histórico de buscas"""
        return SteamService.SEARCH_HISTORY
    
    @staticmethod
    def clear_cache():
        """Limpa o cache"""
        SteamService.CACHE.clear()
