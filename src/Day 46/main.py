from bs4 import BeautifulSoup
from requests import get
from ytmusicapi import YTMusic

URL = "https://appbrewery.github.io/bakeboard-hot-100"

date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
)

response = get(
    f"{URL}/{date}",
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.3 Safari/537.36"
    },
)

if response.status_code != 200:
    print("Failed to fetch the website:", response)

content = response.content

soup = BeautifulSoup(content, "html.parser")

song_titles = soup.find_all("h3", class_="chart-entry__title")

song_names = []

for title in song_titles:
    song_names.append(title.getText())

print(song_names)

yt = YTMusic("browser.json")

# Verify authentication works
# playlists = yt.get_library_playlists()

# print(f"Found {len(playlists)} playlists in your library.")

PLAYLIST_NAME = f"{date} Billboard 100"

# Check if playlist already exists
playlist_id = None
playlists = yt.get_library_playlists(limit=100)

for p in playlists:
    if p["title"] == PLAYLIST_NAME:
        playlist_id = p["playlistId"]
        break

if playlist_id:
    print("This playlist already exists.")
else:
    playlist_id = yt.create_playlist(
        PLAYLIST_NAME,
        f"Playlist with the hottest songs from {date}",
        privacy_status="PRIVATE",
    )
    print("Playlist created.")

# Search and add each song
for song in song_names:
    try:
        search_results = yt.search(song, filter="songs", limit=1)
        yt.add_playlist_items(playlist_id, [search_results[0]["videoId"]])
        print(f"Added: {song}")
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")
