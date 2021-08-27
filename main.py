import get_playlist_tracks
import write_results
import read_config

user_id = read_config.get_user_id()
playlist_id = read_config.get_playlist_id()

spotify_playlist_songs = get_playlist_tracks.get_playlist_tracks(user_id,playlist_id)

write_results.write_results(spotify_playlist_songs)

print("done")