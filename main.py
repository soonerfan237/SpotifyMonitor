import datetime
import get_playlist_tracks
import write_results
import compare_results
import send_results
import setup
import cleanup

result_dir = "results"
ignore_song_file = "ignore_song_list.txt"

if setup.setup_check(result_dir, ignore_song_file):

    start_time = datetime.datetime.now()

    spotify_playlist_songs = get_playlist_tracks.get_playlist_tracks()

    write_results.write_results(spotify_playlist_songs, result_dir)

    result_files = compare_results.get_result_files(result_dir)
    missing_songs = []
    for result_file in result_files[1:]:
        missing_songs.extend(compare_results.compare_results(result_files[0], result_file))

    missing_songs = compare_results.deduplicate_list(missing_songs)
    missing_songs = compare_results.ignore_results(missing_songs)

    if len(missing_songs) == 0 and len(result_files) > 1:
        cleanup.remove_result_file(result_files[0])

    contents = send_results.email_results(missing_songs, start_time)

    print(contents)