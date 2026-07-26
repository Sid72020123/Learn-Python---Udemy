### --- Challenge 3 --- ###

from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep the browser open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--window-size=1920,1080")

# Create a new driver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

first_name_input = driver.find_element(By.NAME, "fName")
last_name_input = driver.find_element(By.NAME, "lName")
email_input = driver.find_element(By.NAME, "email")

submit_button = driver.find_element(By.CSS_SELECTOR, ".btn")


first_name_input.send_keys("First Name")
last_name_input.send_keys("Last Name")
email_input.send_keys("abc@xyz.com")
submit_button.click()
