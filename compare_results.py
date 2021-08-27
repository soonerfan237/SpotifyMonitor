import datetime
import ast

read_file = open(f"spotify_favorites_{datetime.date.today()}.txt", "r")
res = ast.literal_eval(read_file.readline())