import os

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
filesname_without_extension = []

for music_filename in music_in_dir:
    music_without_extension = os.path.splitext(music_filename)[0]
    filesname_without_extension.append(music_without_extension)

uri_of_files = []

for filename_without_extension in filesname_without_extension:
    results = sp.search(filename_without_extension, limit=1, type="track")
    if results["tracks"]["items"]:
        song_uri = results["tracks"]["items"][0]["uri"]
        # print(song_uri)
    else:
        print("No results found.")
    uri_of_files.append(song_uri)

for uri in uri_of_files:
    sp.playlist_add_items(playlist_id, [uri])
