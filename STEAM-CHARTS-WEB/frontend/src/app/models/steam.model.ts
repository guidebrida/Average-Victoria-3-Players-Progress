export interface GameData {
  app_id: string;
  game_name?: string;
  months: string[];
  avg_players: number[];
  total_months: number;
}

export interface GraphRequest {
  app_id: string;
  start_month: string;
  end_month: string;
  chronological: boolean;
}

export interface GraphResponse {
  app_id: string;
  game_name?: string;
  months: string[];
  avg_players: number[];
  start_month: string;
  end_month: string;
  chronological: boolean;
}

export interface SearchHistory {
  app_id: string;
  game_name?: string;
  timestamp: string;
  total_months: number;
}
