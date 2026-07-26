from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep the browser open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create a new driver
driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ"
)

price_rupee = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_paise = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(price_rupee, price_paise)

print(f"The price is: ₹{price_rupee.text}.{price_paise.text}")

# driver.close()  # Closes the current window
# driver.quit()  # Closes the browser
