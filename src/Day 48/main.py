from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep the browser open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--window-size=1920,1080")

# Create a new driver
driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://python.org/")

# driver.get(
#     "https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ"
# )

# price_rupee = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_paise = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(price_rupee, price_paise)

# print(f"The price is: ₹{price_rupee.text}.{price_paise.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# submit_button = driver.find_element(By.ID, value="submit")
# print(submit_button.size)

# documentation_link = driver.find_element(
#     By.CSS_SELECTOR, value=".documentation-widget a"
# )
# print(documentation_link.text)

# website_bug_report = driver.find_element(
#     By.XPATH, value="/html/body/div/footer/div[2]/div/ul/li[3]/a"
# )
# print(website_bug_report.text)

# driver.close()  # Closes the current window
# driver.quit()  # Closes the browser

### --- Challenge 1 --- ###

driver.get("https://python.org/")

events_list = driver.find_element(
    By.XPATH, value="/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul"
)

event_details = events_list.find_elements(By.TAG_NAME, "li")

result = {}

for index, event in enumerate(event_details):
    time = event.find_element(By.TAG_NAME, "time")
    event_name = event.find_element(By.TAG_NAME, "a")

    print(time.text, event_name.text)

    result[index] = {"time": time.text, "name": event_name.text}

print(result)
