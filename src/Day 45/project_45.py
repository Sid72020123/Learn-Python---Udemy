from requests import get
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = get(
    URL,
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.3 Safari/537.36"
    },
)

if response.status_code != 200:
    print("Failed to fetch the website:", response)

content = response.content

soup = BeautifulSoup(content, "html.parser")


movies_list = soup.select("h2 strong")
movies_list.reverse()

TERMS_TO_REMOVE = [
    "How We Chose The Top 100 Best Movies Of All Time",
    "75 — 51",
    "50 — 26",
    "25 — 11",
    "10 — 1",
]

movies_title = []
for movie in movies_list:
    movies_title.append(movie.getText())

for term in TERMS_TO_REMOVE:
    movies_title.remove(term)

with open("movies.txt", "w") as file:
    file.writelines(movie_name + "\n" for movie_name in movies_title)
