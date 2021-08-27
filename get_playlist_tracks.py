import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_playlist_tracks(user_id, playlist_id, cid, secret):
    sp = spotipy.Spotify()
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.trace=False
    results = sp.user_playlist_tracks(user_id,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks