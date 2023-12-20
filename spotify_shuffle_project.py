from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import random

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
playlist_id = os.getenv("PLAYLIST_ID")


def get_playlist():
    # Set up the Spotify API authentication
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri,
                                                   scope="playlist-read-private"))

    # Get the current user's playlists
    playlist = sp.playlist(playlist_id)

    # Print the tracks in the playlist
    my_playlist = []
    for track in playlist['tracks']['items']:
        track_name = track['track']['name']
        artists = ", ".join([artist['name'] for artist in track['track']['artists']])
        track_info = f"{track_name} - {artists}"
        my_playlist.append(track_info)
    return my_playlist


def shuffle_playlist():
    """arranges songs from get_playlist() in random order"""
    playlist = get_playlist()
    shuffled_playlist = random.sample(playlist, len(playlist))

    for track in shuffled_playlist:
        if track == shuffled_playlist[0]:
            print("\nNow Playing:", track, "\n")
            print("Queue:")
        else:
            print(track)


shuffle_playlist()
