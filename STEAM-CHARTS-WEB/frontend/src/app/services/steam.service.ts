import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { GameData, GraphRequest, GraphResponse, SearchHistory } from '../models/steam.model';

@Injectable({
  providedIn: 'root'
})
export class SteamService {
  private apiUrl = 'http://localhost:8000/api/steam';

  constructor(private http: HttpClient) { }

  /**
   * Busca dados de um jogo na Steam
   */
  fetchGameData(appId: string): Observable<GameData> {
    return this.http.post<GameData>(`${this.apiUrl}/fetch?app_id=${appId}`, {});
  }

  /**
   * Gera dados filtrados para o gráfico
   */
  generateGraph(request: GraphRequest): Observable<GraphResponse> {
    return this.http.post<GraphResponse>(`${this.apiUrl}/graph`, request);
  }

  /**
   * Obtém o histórico de buscas
   */
  getSearchHistory(): Observable<SearchHistory[]> {
    return this.http.get<SearchHistory[]>(`${this.apiUrl}/history`);
  }

  /**
   * Verifica se o backend está online
   */
  healthCheck(): Observable<any> {
    return this.http.get(`${this.apiUrl}/health`);
  }

  /**
   * Limpa o cache do backend
   */
  clearCache(): Observable<any> {
    return this.http.delete(`${this.apiUrl}/cache`);
  }
}
