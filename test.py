from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("http://localhost")
    time.sleep(2)
    page_source = driver.page_source
    
    # I-print ang page source para sa debugging
    print("=== PAGE SOURCE START ===")
    print(page_source[:2000])  # Unang 2000 characters lang
    print("=== PAGE SOURCE END ===")
    
    # I-check kung may text
    if "Hello CI/CD World" in page_source:
        print("TEST PASSED ✅")
    else:
        print("TEST FAILED ❌ - 'Hello CI/CD World' not found")
        print("Nakita sa page:")
        if "<?php" in page_source:
            print("⚠️  PHP code ay hindi na-process - problema sa PHP configuration")
        elif "php" in page_source.lower():
            print("⚠️  May PHP-related text pero hindi nag-render")
        else:
            print("❌ Walang PHP output at all")
        
        exit(1)
        
finally:
    driver.quit()
