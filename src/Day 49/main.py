import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options = webdriver.ChromeOptions()

# Keep the browser open
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

ACCOUNT_EMAIL = "sid@test.com"
ACCOUNT_PASSWORD = "superSecretTestPassword"
GYM_URL = "https://appbrewery.github.io/gym/"

# Create a new driver
driver = webdriver.Chrome(options=chrome_options)

driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)

login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

email_entry = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
password_entry = driver.find_element(By.ID, "password-input")
login_submit_button = driver.find_element(By.ID, "submit-button")

email_entry.clear()
email_entry.send_keys(ACCOUNT_EMAIL)
password_entry.clear()
password_entry.send_keys(ACCOUNT_PASSWORD)
login_submit_button.click()

wait.until(
    EC.presence_of_element_located((By.ID, "schedule-page"))
)  # Wait until successful login
