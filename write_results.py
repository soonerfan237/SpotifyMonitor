import datetime

def write_results(spotify_playlist_songs):

    output_file = open(f"spotify_favorites_{datetime.date.today()}.txt", "w")
    for song in spotify_playlist_songs:
        song_dict = {'artist_name': song["track"]["artists"][0]["name"],
                     'artist_id': song["track"]["artists"][0]["id"],
                     'album_name': song["track"]["album"]["name"],
                     'album_id': song["track"]["album"]["id"],
                     'song_name': song["track"]["name"],
                     'song_id': song["track"]["id"],
                     'is_local': song["track"]["is_local"],
                     'external_ids': song["track"]["external_ids"]
                     }
        output_file.writelines(str(song_dict) + '\n')

    output_file.close()