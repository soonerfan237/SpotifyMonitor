import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import read_config

def get_playlist_tracks():
    sp = spotipy.Spotify()
    client_credentials_manager = SpotifyClientCredentials(client_id=read_config.get_cid(), client_secret=read_config.get_secret())
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.trace=False
    results = sp.user_playlist_tracks(read_config.get_user_id(),read_config.get_playlist_id())
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
