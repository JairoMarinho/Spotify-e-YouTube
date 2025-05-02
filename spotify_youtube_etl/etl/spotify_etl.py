from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from config.credentials_loader import load_credentials

def get_spotify_top_tracks():
    creds = load_credentials()
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=creds['spotify']['client_id'],
        client_secret=creds['spotify']['client_secret']
    ))

    # Buscar a playlist "Top 50 Global"
    playlist = sp.search(q='Top 50 Global', type='playlist', limit=1)['playlists']['items'][0]
    playlist_id = playlist['id']

    # Pegar as faixas da playlist
    tracks = sp.playlist_tracks(playlist_id, limit=50)['items']
    return [t['track'] for t in tracks if t.get('track')]

