import os
import random
from typing import Dict
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

def get_spotify_client() -> spotipy.Spotify:
    client_credentials_manager = SpotifyClientCredentials(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
    )
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_random_track() -> Dict[str, str]:
    try:
        sp = get_spotify_client()
        playlist_id = os.getenv('SPOTIFY_PLAYLIST_ID')
        print(f"Attempting to fetch playlist with ID: {playlist_id}")  # Debug print

        results = sp.playlist_items(playlist_id, additional_types=('track',))
        tracks = results['items']

        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])

        track = random.choice(tracks)['track']

        return {
            'name': track['name'],
            'artists': ', '.join(artist['name'] for artist in track['artists']),
            'url': track['external_urls']['spotify']
        }
    except Exception as e:
        print(f"Detailed error in get_random_track: {str(e)}")  # Debug print
        raise