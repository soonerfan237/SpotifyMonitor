import pandas as pd
import spotipy
sp = spotipy.Spotify()
from spotipy.oauth2 import SpotifyClientCredentials
cid = '5553faba0c3a447abc4eb54bda441322'
secret = 'e961dd2b417344ed8b51e4eccc4c025d'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False
playlist = sp.user_playlist("soonerfan237", "48JH4qE9hjDR1kQ8kW8XAP")
songs = playlist["tracks"]["items"]
ids = []
for i in range(len(songs)):
    ids.append(songs[i]["track"]["id"])
features = sp.audio_features(ids)
df = pd.DataFrame(features)