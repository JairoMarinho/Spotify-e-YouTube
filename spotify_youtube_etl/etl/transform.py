import pandas as pd

def clean_spotify_data(raw_tracks: list) -> pd.DataFrame:
    """
    Transforma a lista de faixas do Spotify em DataFrame limpo e estruturado.
    """
    # Converter para DataFrame
    df = pd.DataFrame([{
        'track_name': track['name'],
        'artist': track['artists'][0]['name'] if track['artists'] else None,
        'album': track['album']['name'],
        'duration_ms': track['duration_ms'],
        'popularity': track['popularity'],
        'release_date': track['album']['release_date']
    } for track in raw_tracks])

    # Remover nulos importantes
    df.dropna(subset=['track_name', 'artist'], inplace=True)

    # Padronizar nomes (caixa baixa, tirar espaços extras)
    df['track_name'] = df['track_name'].str.strip().str.lower()
    df['artist'] = df['artist'].str.strip().str.lower()
    df['album'] = df['album'].str.strip().str.lower()

    # Converter datas
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

    return df


def calculate_spotify_metrics(df: pd.DataFrame) -> dict:
    """
    Calcula métricas descritivas a partir dos dados do Spotify.
    """
    metrics = {
        'total_tracks': len(df),
        'avg_duration_min': round(df['duration_ms'].mean() / 60000, 2),
        'avg_popularity': round(df['popularity'].mean(), 2),
        'top_artist': df['artist'].mode()[0] if not df['artist'].mode().empty else None
    }
    return metrics
