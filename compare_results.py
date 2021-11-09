import ast
import glob
import re

def get_result_files(result_dir):
    result_files = glob.glob(result_dir+"/spotify_favorites*.txt")
    result_files = sorted(result_files, key=str.lower, reverse=True)
    return result_files

def read_results(result_file):
    read_file = open(result_file, "r")
    results_str = read_file.readlines()
    results_dict = []
    for result in results_str:
        result_dict = ast.literal_eval(result)
        results_dict.append(result_dict.copy())
    return results_dict

def compare_results(new_result_file, old_result_file):
    new_result = read_results(new_result_file)
    old_result = read_results(old_result_file)
    missing_songs = []
    for old_song in old_result:
        found_match = 0
        for new_song in new_result:
            if missing_song["song_name"] ==re.sub('[^a-zA-Z0-9-_*.]','', ignore_song["song_name"]).upper() and missing_song["artist_name"] ==re.sub('[^a-zA-Z0-9-_*.]','', ignore_song["artist_name"]).upper():
                ignore = 1
        if found_match == 0:
            missing_songs.append(old_song.copy())
    return missing_songs

def ignore_results(missing_songs):
    missing_songs_without_ignored = []
    ignore_song_list = read_results("ignore_song_list.txt")
    for missing_song in missing_songs:
        ignore = 0
        for ignore_song in ignore_song_list:
            if missing_song["song_name"] == ignore_song["song_name"] and missing_song["artist_name"] == ignore_song["artist_name"]:
                ignore = 1
        if ignore == 0:
            missing_songs_without_ignored.append(missing_song)
    return missing_songs_without_ignored

def deduplicate_list(missing_songs):
    missing_songs_dedup = []
    for song in missing_songs:
        if song not in missing_songs_dedup:
            missing_songs_dedup.append(song)
    return missing_songs_dedup
