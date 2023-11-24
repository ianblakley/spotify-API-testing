import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")


def get_top_songs():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                   client_secret=client_secret,
                                                   redirect_uri=redirect_uri,
                                                   scope="user-top-read"))

    top_tracks = sp.current_user_top_tracks(limit=10, time_range='long_term')

    print("Top Tracks:")
    for i, track in enumerate(top_tracks['items'], start=1):
        print(f"{i}. {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")


get_top_songs()