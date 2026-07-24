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

# articles_table = soup.find("tr", id="bigbox").find_all("tr")

# for article in articles_table:
#     print(article)
#     title_info = soup.find("span", class_="titleline").find("a")
#     title_name = title_info.string
#     title_link = title_info.get("href")
#     print(title_name, title_link)

titles = soup.find_all("span", class_="titleline")
scores = soup.select(".subline span.score")

titles_texts = []
titles_links = []
titles_scores = []

for index, title in enumerate(titles):
    link = title.find("a")
    if link and scores[index]:
        score = int(scores[index].getText().replace(" points", ""))

        titles_texts.append(link.getText())
        titles_links.append(link.get("href"))
        titles_scores.append(score)

# combined_data = zip(titles_texts, titles_links, titles_scores)
# print(max(combined_data, key=lambda x: x[2]))

combined_data = sorted(
    zip(titles_texts, titles_links, titles_scores), key=lambda x: x[2], reverse=True
)

for data in combined_data:
    print(f"[{data[2]:04}] {data[0]} => {data[1]}")
