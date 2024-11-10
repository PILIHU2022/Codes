import os

import opencc
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Asking parameter
playlist_id = input(
    "Input your playlist ID(https://open.spotify.com/playlist/<playlist_id>):"
)
print(
    "You need to see this document before you input the parameter following, and create an api for this script!\n"
)
print("https://spotipy.readthedocs.io/")
client_id = input("Input your client id:")
client_secret = input("Input your client secret:")
music_in_dir = os.listdir("")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri="http://example.com",
        scope="playlist-modify-private,playlist-modify-public",
    )
)

# online
results = sp.playlist_tracks(playlist_id)
inplaylist_online = []
name_in_list_online = []
# local
name_in_list_tc_offline = []


def get_file_name_with_out_extension():
    for music_filename in music_in_dir:
        music_without_extension = os.path.splitext(music_filename)[0]


def get_songs_in_playlist():
    for item in results["items"]:
        track = item["track"]
        inplaylist_online.append(track)


for __i in inplaylist_online:
    ___i = __i["name"], "- 陳奕迅"
    name_in_list_online.append(" ".join(___i))

for item_1 in eason_filesname_without_extension:
    convert_to_tc = opencc.OpenCC("s2tw.json").convert(item_1)
    name_in_list_tc_offline.append(convert_to_tc)

for item_2 in name_in_list_tc_offline:
    if item_2 not in name_in_list_online:
        item_2 = opencc.OpenCC("tw2sp.json").convert(item_2)
        print(f"{item_2} NOT in playlist!")
