import get_playlist_tracks
import write_results
import read_config

user_id = read_config.get_user_id()
playlist_id = read_config.get_playlist_id()
cid = read_config.get_cid()
secret = read_config.get_secret()

spotify_playlist_songs = get_playlist_tracks.get_playlist_tracks(user_id,playlist_id, cid, secret)

write_results.write_results(spotify_playlist_songs)

print("done")