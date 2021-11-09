import datetime
import re

def write_results(spotify_playlist_songs, result_dir):

    output_file = open(result_dir+"/spotify_favorites_" + str(datetime.date.today()) + ".txt", "w")

    for song in spotify_playlist_songs:
        ssong_dict = {'artist_name': re.sub('[^a-zA-Z0-9-_*.]','',song["track"]["artists"][0]["name"]).upper(),
                     'artist_id': song["track"]["artists"][0]["id"],
                     'album_name':re.sub('[^a-zA-Z0-9-_*.]','', song["track"]["album"]["name"]).upper(),
                     'album_id': song["track"]["album"]["id"],
                     'song_name': re.sub('[^a-zA-Z0-9-_*.]','',song["track"]["name"]).upper(),
                     'song_id': song["track"]["id"],
                     'is_local': song["track"]["is_local"],
                     'external_ids': song["track"]["external_ids"]
                     }
        output_file.writelines(str(song_dict) + '\n')

    output_file.close()
