from selenium import webdriver

# Keep the browser open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create a new driver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://amazon.com")


driver.close()  # Closes the current window
driver.quit()  # Closes the browser
