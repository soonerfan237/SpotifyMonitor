#TODO: email results of missing songs
import datetime

def format_results(missing_songs, start_time):
    processing_time = datetime.datetime.now() - start_time
    contents = "Processing time - " + str(processing_time) + "\n"
    contents = contents + str(len(missing_songs)) + " missing songs.\n"
    contents = contents + "Artist | Song \n"
    for song in missing_songs:
        contents = contents + song["artist_name"] + " | " + song["song_name"] + "\n"
    return contents

def send_results(missing_songs, start_time):
    contents = format_results(missing_songs, start_time)
    return contents
