from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt"
    )
)

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
soup = BeautifulSoup(response.text, 'html.parser')

# Extract song names
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# Get Spotify user ID
user_id = sp.current_user()["id"]
print(f"Spotify User ID: {user_id}")

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    query = f"track:{song} year:{year}"
    result = sp.search(q=query, type="track")
    print(f"Searching for: {query}")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(f"Created Playlist: {playlist['name']} with ID: {playlist['id']}")

# Adding songs found into the new playlist
if song_uris:
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
    print(f"Added {len(song_uris)} songs to the playlist.")
else:
    print("No songs to add to the playlist.")
