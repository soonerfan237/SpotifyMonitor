import yaml

def get_user_id():
    #user_id = ""
    with open("configuration.yaml", 'r') as stream:
        try:
            user_id = yaml.safe_load(stream)["USER_ID"]
        except yaml.YAMLError as exc:
            print(exc)
    return user_id

def get_playlist_id():
    with open("configuration.yaml", 'r') as stream:
        try:
            playlist_id = yaml.safe_load(stream)["PLAYLIST_ID"]
        except yaml.YAMLError as exc:
            print(exc)
    return playlist_id

def get_cid():
    with open("configuration.yaml", 'r') as stream:
        try:
            cid = yaml.safe_load(stream)["CID"]
        except yaml.YAMLError as exc:
            print(exc)
    return cid

def get_secret():
    with open("configuration.yaml", 'r') as stream:
        try:
            secret = yaml.safe_load(stream)["SECRET"]
        except yaml.YAMLError as exc:
            print(exc)
    return secret