from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep the browser open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--window-size=1920,1080")

# Create a new driver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH, '//*[@id="mwDw"]')

print(article_count.text)

# article_count.click() # Clicking a link

all_portals = driver.find_element(
    By.LINK_TEXT, "Content portals"
)  # Locating by link text content
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")  # Write content in input box

# search_button = driver.find_element(
#     By.CSS_SELECTOR, "#searchform > button:nth-child(2)"
# )
# print(search_button.text)

search.send_keys(Keys.ENTER)
