import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_playlist_tracks(user_id, playlist_id):
    sp = spotipy.Spotify()
    cid = '5553faba0c3a447abc4eb54bda441322'
    secret = 'e961dd2b417344ed8b51e4eccc4c025d'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.trace=False
    results = sp.user_playlist_tracks(user_id,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks