import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ChartConfiguration } from 'chart.js';
import { NgChartsModule } from 'ng2-charts';
import { GraphResponse } from '../../models/steam.model';

@Component({
  selector: 'app-chart',
  standalone: true,
  imports: [CommonModule, NgChartsModule],
  templateUrl: './chart.component.html',
  styleUrls: ['./chart.component.css']
})
export class ChartComponent {
  @Input() set data(graphData: GraphResponse | null) {
    if (graphData) {
      this.updateChart(graphData);
    }
  }

  chartConfig: ChartConfiguration<'line'> = {
    type: 'line',
    data: {
      labels: [],
      datasets: [
        {
          label: 'Jogadores Médios',
          data: [],
          borderColor: '#1A9FD8',
          backgroundColor: 'rgba(26, 159, 216, 0.1)',
          borderWidth: 2.5,
          tension: 0.4,
          fill: true,
          pointRadius: 4,
          pointBackgroundColor: '#1A9FD8',
          pointBorderColor: '#1B2838',
          pointBorderWidth: 2,
          pointHoverRadius: 6,
          pointHoverBackgroundColor: '#1A9FD8',
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      plugins: {
        legend: {
          labels: {
            color: '#C7D5E0',
            font: {
              size: 12,
              weight: 'bold'
            },
            padding: 20
          }
        },
        tooltip: {
          backgroundColor: 'rgba(12, 20, 25, 0.9)',
          titleColor: '#C7D5E0',
          bodyColor: '#C7D5E0',
          borderColor: '#566573',
          borderWidth: 1,
          padding: 12,
          displayColors: true,
          callbacks: {
            label: (context) => {
              const value = context.parsed.y;
              return `Jogadores: ${value?.toLocaleString() ?? '0'}`;
            }
          }
        }
      },
      scales: {
        x: {
          ticks: {
            color: '#8FA3B3',
            font: {
              size: 11
            },
            maxRotation: 45,
            minRotation: 45
          },
          grid: {
            color: 'rgba(86, 101, 115, 0.1)'
          }
        },
        y: {
          ticks: {
            color: '#8FA3B3',
            font: {
              size: 11
            },
            callback: (value) => {
              return (value as number).toLocaleString();
            }
          },
          grid: {
            color: 'rgba(86, 101, 115, 0.1)'
          }
        }
      }
    }
  };

  updateChart(graphData: GraphResponse) {
    if (this.chartConfig.data && this.chartConfig.data.datasets.length > 0) {
      this.chartConfig.data.labels = graphData.months;
      this.chartConfig.data.datasets[0].data = graphData.avg_players;
    }
  }
}
