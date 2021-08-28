#TODO: schedule this to run on regular basis
import datetime
import get_playlist_tracks
import write_results
import read_config
import compare_results
import send_results

start_time = datetime.datetime.now()

result_dir = "results"

user_id = read_config.get_user_id()
playlist_id = read_config.get_playlist_id()
cid = read_config.get_cid()
secret = read_config.get_secret()

spotify_playlist_songs = get_playlist_tracks.get_playlist_tracks(user_id, playlist_id, cid, secret)

write_results.write_results(spotify_playlist_songs, result_dir)

result_files = compare_results.get_result_files(result_dir)
missing_songs = []
for result_file in result_files[1:]:
    missing_songs.extend(compare_results.compare_results(result_files[0], result_file))

missing_songs = compare_results.deduplicate_list(missing_songs)

contents = send_results.send_results(missing_songs, start_time)

print(contents)
print("Done")