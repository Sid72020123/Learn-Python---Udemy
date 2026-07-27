from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Keep the browser open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--window-size=1920,1080")

# Create a new driver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://appbrewery.github.io/gym/")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

email_entry = driver.find_element(By.ID, "email-input")
password_entry = driver.find_element(By.ID, "password-input")
login_submit_button = driver.find_element(By.ID, "submit-button")

email_entry.send_keys("student@test.com")
password_entry.send_keys("password123")
login_submit_button.click()

"""
language_select = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.ID, "langSelect-EN")
    )  # Replace with your element's locator
)
language_select.click()

sleep(5)  # Wait for the game to load completely

cookie_button = driver.find_element(By.ID, "bigCookie")


def get_best_product():
    best_item = None
    products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")
    for product in reversed(products):
        if "enabled" in product.get_attribute("class"):
            best_item = product
            break
    return best_item


# Set timers
wait_time = 15
timeout = time() + wait_time  # Check for purchases every 5 seconds
twenty_min = time() + 60 * 20  # Run for 20 minutes

while True:
    cookie_button.click()

    # Every 20 seconds, try to buy the most expensive item we can afford
    if time() > timeout:
        try:
            # Get current cookie count
            cookies = int(
                driver.find_element(By.ID, "cookies")
                .text.split(" ")[0]
                .replace(",", "")
            )

            # Find the most expensive item we can afford & buy it if found
            best_product = get_best_product()
            if best_product:
                best_product.click()
                print(f"Bought item: {best_product.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")

        # Reset timer
        timeout = time() + wait_time

    # Stop after 20 minutes
    if time() > twenty_min:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break
"""
