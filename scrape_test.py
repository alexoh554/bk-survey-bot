from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

import random
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://stackoverflow.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Time between pages
DELAY = 0.3

def wait_and_click(element_locator):
    wait.until(EC.element_to_be_clickable(element_locator)).click()

def nextPage():
    wait_and_click((By.NAME, 'NextButton'))
    time.sleep(DELAY)

def main():
    
    test = driver.find_element(By.XPATH, '//*[@id="content"]/header/div/div[1]/div[1]/div/h2').text
    print(test)
    

    driver.close()
    

if __name__ == "__main__":
    main()
