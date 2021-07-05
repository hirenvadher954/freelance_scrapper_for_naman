from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('./chromedriver')

driver.get(
    'https://www.hidubai.com/businesses/winter-chiff-chaff-gents-saloon-beauty-wellness-health-beauty-salons-al'
    '-fahidi-al-souq-al-kabeer-dubai')

# xpath to find email span
# //span[contains(text(),'Show E-mail')]
# //i[@class="icon-email"]
# TODO: Wait until span is clickable

# email_path = driver.find_elements_by_xpath("//span[contains(text(),'Show E-mail')]")
# element = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.XPATH, "i[@class='icon-email']")))
driver.find_element_by_xpath("i[@class='icon-email']").click()

# element.click()

# print(element)
# xpath after click event happens
# //span[contains(text(),'@')][1]
# TODO: Extract text after click event

# overunder=wait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Over/Under']")))
