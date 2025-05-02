import sys
import os
sys.path.append(os.path.abspath('.'))

from etl.spotify_etl import get_spotify_top_tracks
from etl.transform import clean_spotify_data, calculate_spotify_metrics
from load.to_mongodb import load_to_mongodb



def main():
    print("🔄 Iniciando pipeline ETL...")

    # 1. Extração de dados do Spotify
    raw_tracks = get_spotify_top_tracks()
    print(f"🎵 {len(raw_tracks)} faixas extraídas do Spotify.")

    # 2. Transformação
    df = clean_spotify_data(raw_tracks)
    metrics = calculate_spotify_metrics(df)
    print("✅ Dados transformados com sucesso.")

    # 3. Carga no MongoDB
    load_to_mongodb(df.to_dict(orient='records'), "spotify_tracks")
    print("📦 Dados inseridos no MongoDB.")

    # 4. Exibir métricas
    print("\n📊 Métricas extraídas:")
    for key, value in metrics.items():
        print(f"• {key}: {value}")

if __name__ == "__main__":
    main()
