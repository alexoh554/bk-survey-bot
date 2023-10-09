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

driver.get("https://www.mybkexperience.com/")
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
    # PAGE 1
    iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
    driver.switch_to.frame(iframe)
    
    restaurant_number = wait.until(EC.presence_of_element_located((By.NAME, "QR~QID114~TEXT")))

    restaurant_number.send_keys("17885")
    time.sleep(DELAY)

    nextPage()

    # Page 2
    Select(wait.until(EC.element_to_be_clickable((By.NAME, "QR~QID6")))).select_by_value('46')

    wait_and_click((By.NAME, 'QR~QID118~2~TEXT'))
    wait_and_click((By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[2]'))

    random_hour = str(random.randint(1, 12))
    Select(wait.until(EC.element_to_be_clickable((By.NAME, 'QR~QID8#1~1')))).select_by_value(random_hour)
    random_minute = str(random.randint(0, 60))
    Select(wait.until(EC.element_to_be_clickable((By.NAME, 'QR~QID8#2~1')))).select_by_value(random_minute)
    random_time = str(random.randint(1, 2))
    Select(wait.until(EC.element_to_be_clickable((By.NAME, 'QR~QID8#3~1')))).select_by_value(random_time)
    time.sleep(DELAY)

    nextPage()

    # Page 3
    wait_and_click((By.XPATH, '//*[@id="QID18-24-label"]'))
    time.sleep(DELAY)
    nextPage()

    # Page 4
    wait_and_click((By.XPATH, '//*[@id="QID13-2-label"]'))
    time.sleep(DELAY)
    nextPage()

    # Page 5
    wait_and_click((By.XPATH, '//*[@id="QID12-2-label"]'))
    time.sleep(DELAY)
    nextPage()

    # Page 6
    wait_and_click((By.XPATH, '//*[@id="QID83-1-label"]'))
    time.sleep(DELAY)
    nextPage()

    # Page 7
    wait_and_click((By.XPATH, '//*[@id="QID84-1-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 8
    wait_and_click((By.XPATH, '//*[@id="QID123-1-label"]'))
    wait_and_click((By.XPATH, '//*[@id="QID124-1-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 9
    wait_and_click((By.XPATH, '//*[@id="QID21"]/div[3]/div/fieldset/div/table/tbody/tr[1]/td[2]'))
    wait_and_click((By.XPATH, '//*[@id="QID21"]/div[3]/div/fieldset/div/table/tbody/tr[2]/td[2]/label[1]'))
    wait_and_click((By.XPATH, '//*[@id="QID21"]/div[3]/div/fieldset/div/table/tbody/tr[3]/td[2]/label[1]'))
    wait_and_click((By.XPATH, '//*[@id="QID21"]/div[3]/div/fieldset/div/table/tbody/tr[4]/td[2]/label[1]'))
    wait_and_click((By.XPATH, '//*[@id="QID21"]/div[3]/div/fieldset/div/table/tbody/tr[5]/td[2]/label[1]'))
    wait_and_click((By.XPATH, '//*[@id="QID21"]/div[3]/div/fieldset/div/table/tbody/tr[6]/td[2]/label[1]'))
    wait_and_click((By.XPATH, '//*[@id="QID21"]/div[3]/div/fieldset/div/table/tbody/tr[7]/td[2]/label[1]'))
    wait_and_click((By.XPATH, '//*[@id="QID21"]/div[3]/div/fieldset/div/table/tbody/tr[8]/td[2]/label[1]'))
    wait_and_click((By.XPATH, '//*[@id="QID21"]/div[3]/div/fieldset/div/table/tbody/tr[9]/td[2]/label[1]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 10
    wait_and_click((By.XPATH, '//*[@id="QID41"]/div[3]/div/fieldset/div/table/tbody/tr[1]/td[2]/label[1]'))
    wait_and_click((By.XPATH, '//*[@id="QID41"]/div[3]/div/fieldset/div/table/tbody/tr[2]/td[2]/label[1]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 11
    review = "It was so tasty. Delicious even. Very good."
    review_form = wait.until(EC.presence_of_element_located((By.NAME, 'QR~QID120~TEXT')))
    review_form.send_keys(review)
    time.sleep(DELAY)
    nextPage()
    
    # Page 12
    wait_and_click((By.XPATH, '//*[@id="QID38-2-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 13
    wait_and_click((By.XPATH, '//*[@id="QID103-7-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 14
    wait_and_click((By.XPATH, '//*[@id="QID106-3-label"]'))
    time.sleep(DELAY)
    nextPage()

    # Page 15
    wait_and_click((By.XPATH, '//*[@id="QID48-12-label"]'))
    time.sleep(DELAY)
    nextPage()

    # Page 16
    wait_and_click((By.XPATH, '//*[@id="QID49"]/div[3]/div/fieldset/div/table/tbody/tr[1]/td[2]/label[1]'))
    wait_and_click((By.XPATH, '//*[@id="QID49"]/div[3]/div/fieldset/div/table/tbody/tr[2]/td[2]/label[1]'))
    wait_and_click((By.XPATH, '//*[@id="QID49"]/div[3]/div/fieldset/div/table/tbody/tr[3]/td[2]/label[1]'))
    wait_and_click((By.XPATH, '//*[@id="QID49"]/div[3]/div/fieldset/div/table/tbody/tr[4]/td[2]/label[1]'))
    wait_and_click((By.XPATH, '//*[@id="QID49"]/div[3]/div/fieldset/div/table/tbody/tr[5]/td[2]/label[1]'))
    wait_and_click((By.XPATH, '//*[@id="QID49"]/div[3]/div/fieldset/div/table/tbody/tr[6]/td[2]/label[1]'))
    wait_and_click((By.XPATH, '//*[@id="QID49"]/div[3]/div/fieldset/div/table/tbody/tr[7]/td[2]/label[1]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 17
    wait_and_click((By.XPATH, '//*[@id="QID50-2-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 18
    wait_and_click((By.XPATH, '//*[@id="QID60-1-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 19
    wait_and_click((By.XPATH, '//*[@id="QID62-4-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 20
    wait_and_click((By.XPATH, '//*[@id="QID57-3-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 21
    wait_and_click((By.XPATH, '//*[@id="QID94-2-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 22
    wait_and_click((By.XPATH, '//*[@id="QID96-3-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 23
    wait_and_click((By.XPATH, '//*[@id="QID55-1-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 24
    wait_and_click((By.XPATH, '//*[@id="QID97-1-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 25
    wait_and_click((By.XPATH, '//*[@id="QID100-2-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 26
    nextPage()
    
    # Page 27
    wait_and_click((By.XPATH, '//*[@id="QID65-2-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 28
    wait_and_click((By.XPATH, '//*[@id="QID66-4-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 29
    wait_and_click((By.XPATH, '//*[@id="QID67-5-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Page 30 
    wait_and_click((By.XPATH, '//*[@id="QID99-4-label"]'))
    time.sleep(DELAY)
    nextPage()
    
    # Final page
    code_message = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="EndOfSurvey"]'))).get_attribute('textContent')
    print(code_message.text)

    time.sleep(10)
    driver.close()
    

if __name__ == "__main__":
    main()
