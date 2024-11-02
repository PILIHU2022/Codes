import spotipy

client_id = "Your_client_id"
client_secret = "Your_client_secret"
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_id = "7nKGUUD2sVAtG28zQOJgUp"
print(sp.playlist_cover_image(playlist_id))
# results = sp.playlist_tracks(playlist_id)
# for item in results["items"]:
#     track = item["track"]
#     print(track["name"], "-", track["artists"][0]["name"])
