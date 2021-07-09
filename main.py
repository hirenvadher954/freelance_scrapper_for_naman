from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome('./chromedriver')

driver.get(
    'https://www.hidubai.com/businesses/winter-chiff-chaff-gents-saloon-beauty-wellness-health-beauty-salons-al'
    '-fahidi-al-souq-al-kabeer-dubai')

# email_path = driver.find_elements_by_xpath("//span[contains(text(),'Show E-mail')]")
element = WebDriverWait(driver, 40).until(
    EC.element_to_be_clickable((By.XPATH, "//i[@class='icon-email']")))
time.sleep(1)
element.click()
time.sleep(1)

email_text = driver.find_element_by_xpath("//a//span[@class='valueField hidden-xs ng-binding']").text
shop_text = driver.find_element_by_xpath("//div[@class='titleH1 ng-binding']").text
print(email_text, shop_text)

# driver.find_element_by_xpath("//i[@class='icon-email']").click()
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='icon-email']"))).click()


# element.click()

# print(element)
# xpath after click event happens
# //span[contains(text(),'@')][1]
# TODO: Extract text after click event
# plain_email = driver.find_elements_by_xpath("//span[contains(text(),'@')]")[1]
# for val in plain_email:
#     print(val)

# print("Email", plain_email.text)
# overunder=wait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Over/Under']")))
