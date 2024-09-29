from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

WAIT_TIME = 2
# Options().add_argument("--headless") 
driver = webdriver.Chrome(service=Service('./chromedriver-mac-arm64/chromedriver'), options=Options())

def visit_website():
    driver.get("https://campuschroniclesnyc.wixsite.com/blog")
    time.sleep(WAIT_TIME)
    try:
        driver.find_element(By.LINK_TEXT, "Posts").click()
        time.sleep(WAIT_TIME)
        driver.find_element(By.LINK_TEXT, "About").click()
        time.sleep(WAIT_TIME) 
        driver.find_element(By.LINK_TEXT, "Home").click()
        time.sleep(WAIT_TIME)
        print("Finished Successfully")
    except Exception as e:
        print(f"Error occurred: {e}")

visit_website()
driver.quit()
