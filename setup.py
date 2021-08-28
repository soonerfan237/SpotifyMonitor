import os
from pathlib import Path

def make_results_dir(result_dir):
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

def make_ignore_file(ignore_song_file):
    if not Path(ignore_song_file).is_file():
        with open(ignore_song_file, 'w') as fp:
            fp.write("{'artist_name': 'EXAMPLE ARTIST NAME', 'song_name': 'EXAMPLE SONG NAME'}")

def check_config():
    if not Path("configuration.yaml").is_file():
        print("Missing configuration.yaml.")
        return False
    return True

def setup_check(result_dir, ignore_song_file):
    make_results_dir(result_dir)
    make_ignore_file(ignore_song_file)
    return check_config()