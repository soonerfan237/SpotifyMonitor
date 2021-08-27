import spotipy

sp = spotipy.Spotify()
from spotipy.oauth2 import SpotifyClientCredentials
cid = '5553faba0c3a447abc4eb54bda441322'
secret = 'e961dd2b417344ed8b51e4eccc4c025d'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False
results = sp.user_playlist_tracks("soonerfan237","48JH4qE9hjDR1kQ8kW8XAP")
tracks = results['items']
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])
