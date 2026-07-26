from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep the browser open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--window-size=1920,1080")

# Create a new driver
driver = webdriver.Chrome(options=chrome_options)

### --- Challenge 2 --- ###

driver.get("https://en.wikipedia.org/wiki/Main_Page")

print(driver.find_element(By.XPATH, '//*[@id="mwDw"]').text)
