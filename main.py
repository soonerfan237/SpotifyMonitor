import get_playlist_tracks
import write_results

user_id="soonerfan237"
playlist_id="48JH4qE9hjDR1kQ8kW8XAP"

spotify_playlist_songs = get_playlist_tracks.get_playlist_tracks(user_id,playlist_id)

write_results.write_results(spotify_playlist_songs)

print("done")