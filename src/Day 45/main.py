from requests import get
from bs4 import BeautifulSoup

# with open("website.html", "r") as file:
#     CONTENTS = file.read()

# soup = BeautifulSoup(CONTENTS, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)


# # print(soup.prettify())

# print(soup.a)
# print(soup.li)
# print(soup.p)

# all_a_tags = soup.find_all("a")

# print(all_a_tags)

# for tag in all_a_tags:
#     # print(tag.getText())
#     print(tag.getText(), tag.get("href"))

# heading = soup.find("h1", id="name")
# print(heading)

# section_heading = soup.find("h3", class_="heading")
# print(section_heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# headings = soup.select(selector=".heading")
# print(headings)

### --- SCRAPING LIVE WEBSITE --- ###

URL = "https://news.ycombinator.com/"

response = get(URL)

if response.status_code != 200:
    print("Failed to fetch the website:", response)

content = response.content

soup = BeautifulSoup(content, "html.parser")

titles = soup.select(".titleline a")

print(titles)
