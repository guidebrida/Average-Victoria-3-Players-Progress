import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { SteamService } from '../../services/steam.service';
import { GameData, GraphResponse, SearchHistory } from '../../models/steam.model';
import { ChartComponent } from '../../components/chart/chart.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, FormsModule, ChartComponent],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  appIdInput: string = '';
  gameData: GameData | null = null;
  graphData: GraphResponse | null = null;
  searchHistory: SearchHistory[] = [];
  
  isLoading: boolean = false;
  isGenerating: boolean = false;
  errorMessage: string = '';
  successMessage: string = '';
  
  chronological: boolean = true;
  selectedStartMonth: string = '';
  selectedEndMonth: string = '';

  constructor(private steamService: SteamService) { }

  ngOnInit() {
    this.loadSearchHistory();
  }

  /**
   * Carrega dados de um jogo
   */
  fetchGameData() {
    if (!this.appIdInput.trim()) {
      this.errorMessage = 'Por favor, insira um App ID.';
      return;
    }

    this.isLoading = true;
    this.errorMessage = '';
    this.successMessage = '';

    this.steamService.fetchGameData(this.appIdInput).subscribe({
      next: (data) => {
        this.gameData = data;
        this.selectedStartMonth = data.months[0];
        this.selectedEndMonth = data.months[data.months.length - 1];
        this.successMessage = `✅ ${data.total_months} meses carregados!`;
        this.isLoading = false;
      },
      error: (error) => {
        this.errorMessage = 'Erro ao buscar dados. Verifique o App ID.';
        this.isLoading = false;
      }
    });
  }

  /**
   * Escolhe a ordem cronológica
   */
  chooseOrder(chrono: boolean) {
    this.chronological = chrono;
    if (this.gameData) {
      if (chrono) {
        this.selectedStartMonth = this.gameData.months[0];
        this.selectedEndMonth = this.gameData.months[this.gameData.months.length - 1];
      } else {
        this.selectedStartMonth = this.gameData.months[this.gameData.months.length - 1];
        this.selectedEndMonth = this.gameData.months[0];
      }
    }
  }

  /**
   * Gera o gráfico
   */
  generateGraph() {
    if (!this.gameData || !this.selectedStartMonth || !this.selectedEndMonth) {
      this.errorMessage = 'Selecione os meses inicial e final.';
      return;
    }

    this.isGenerating = true;
    this.errorMessage = '';

    const request = {
      app_id: this.appIdInput,
      start_month: this.selectedStartMonth,
      end_month: this.selectedEndMonth,
      chronological: this.chronological
    };

    this.steamService.generateGraph(request).subscribe({
      next: (data) => {
        this.graphData = data;
        this.isGenerating = false;
      },
      error: (error) => {
        this.errorMessage = 'Erro ao gerar gráfico.';
        this.isGenerating = false;
      }
    });
  }

  /**
   * Carrega o histórico de buscas
   */
  loadSearchHistory() {
    this.steamService.getSearchHistory().subscribe({
      next: (data) => {
        this.searchHistory = data;
      },
      error: (error) => {
        console.log('Histórico vazio');
      }
    });
  }

  /**
   * Carrega um item do histórico
   */
  loadFromHistory(appId: string) {
    this.appIdInput = appId;
    this.fetchGameData();
  }

  /**
   * Limpa o cache
   */
  clearCache() {
    this.steamService.clearCache().subscribe({
      next: () => {
        this.successMessage = '✅ Cache limpo!';
        this.gameData = null;
        this.graphData = null;
      },
      error: () => {
        this.errorMessage = 'Erro ao limpar cache.';
      }
    });
  }
}
