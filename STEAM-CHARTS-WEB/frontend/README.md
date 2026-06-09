# Frontend Angular

Este é o frontend da aplicação SteamCharts desenvolvido com **Angular 17+**.

## 📋 Estrutura

```
frontend/
├── src/
│   ├── app/
│   │   ├── components/      # Componentes reutilizáveis
│   │   ├── pages/           # Páginas/rotas
│   │   ├── services/        # Serviços (API)
│   │   ├── models/          # Interfaces TypeScript
│   │   ├── app.component.*  # Componente raiz
│   │   └── app.routes.ts    # Configuração de rotas
│   ├── index.html           # HTML principal
│   ├── main.ts              # Bootstrap da aplicação
│   └── styles.css           # Estilos globais
├── package.json             # Dependências npm
├── angular.json             # Configuração Angular
└── tsconfig.json            # Configuração TypeScript
```

## 🚀 Como Executar

### 1. Instalar dependências
```bash
npm install
```

### 2. Rodar o servidor de desenvolvimento
```bash
ng serve
```

Ou simplesmente:
```bash
npm start
```

O frontend estará disponível em: `http://localhost:4200`

### 3. Build para produção
```bash
ng build --configuration production
```

## 🎨 Componentes

- **DashboardComponent** - Página principal com controles e gráfico
- **ChartComponent** - Gráfico interativo com Chart.js

## 🔌 Serviços

- **SteamService** - Integración com a API FastAPI do backend

## 🎯 Modelos

- **GameData** - Dados brutos de um jogo
- **GraphResponse** - Dados filtrados para o gráfico
- **SearchHistory** - Histórico de buscas
- **GraphRequest** - Requisição de gráfico

## 🎨 Tema

O tema escuro estilo Steam está definido em:
- `styles.css` - Variáveis CSS globais
- `dashboard.component.html` - Classes Tailwind (inline)

### Cores principais:
- **Fundo**: #1B2838
- **Secundário**: #0C1419
- **Destaque**: #1A9FD8 (Azul Steam)
- **Texto**: #C7D5E0

## 📦 Dependências

- **Angular 17** - Framework
- **Chart.js** - Gráficos
- **ng2-charts** - Wrapper Angular para Chart.js
- **RxJS** - Programação reativa

## 🔗 Endpoints Necessários

O frontend conecta no backend em `http://localhost:8000`:

- `POST /api/steam/fetch` - Buscar dados
- `POST /api/steam/graph` - Gerar gráfico
- `GET /api/steam/history` - Histórico
- `GET /api/steam/health` - Health check
- `DELETE /api/steam/cache` - Limpar cache
