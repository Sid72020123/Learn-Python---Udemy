from bs4 import BeautifulSoup
from requests import get

URL = "https://appbrewery.github.io/instant_pot/"

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

price = soup.find("span", class_="a-offscreen")

print(price.get_text().split("$")[1])
