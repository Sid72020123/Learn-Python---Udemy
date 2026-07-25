from bs4 import BeautifulSoup
from requests import get

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
