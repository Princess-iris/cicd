from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Chrome options para sa Jenkins environment
chrome_options = Options()
chrome_options.add_argument('--headless')        # Walang GUI
chrome_options.add_argument('--no-sandbox')      # Kailangan sa Jenkins
chrome_options.add_argument('--disable-dev-shm-usage')  # Para sa limited memory
chrome_options.add_argument('--disable-gpu')     # Optional, pero recommended
chrome_options.add_argument('--window-size=1920,1080')  # Set window size

# I-set ang chromedriver path (galing sa installation mo)
service = Service('/usr/bin/chromedriver')

# Initialize driver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # I-test ang local Apache server mo
    driver.get("http://localhost")
    time.sleep(2)  # Hintayin mag-load ang page
    
    # I-check kung may "Hello CI/CD World" sa page
    assert "Hello CI/CD World" in driver.page_source
    print("TEST PASSED ✅")
    
finally:
    driver.quit()
