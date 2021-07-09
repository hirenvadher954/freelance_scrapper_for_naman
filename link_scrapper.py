from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pprint import pprint
from selenium.webdriver.support import expected_conditions
import time

from collections import OrderedDict

driver = webdriver.Chrome('./chromedriver')

driver.get(
    "https://www.hidubai.com/search?resource=localBusiness&lat=25.197965&lon=55.273985&mscid=5878dcd2e4b01d34728689e0"
    "&mccid=5878dcd4e4b0c0742c50b5f9&place=All%20of%20Dubai")

all_link = list()

shop_info = OrderedDict()
count = 1
while True:
    print("Current Iteration {0}".format(count))
    count += 1
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
    element = WebDriverWait(driver, 40, ignored_exceptions=ignored_exceptions).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='imgBusiness']//a")))
    time.sleep(10)
    all_links_xpath = driver.find_elements_by_xpath("//div[@class='imgBusiness']//a")
    for val in all_links_xpath:
        all_link.append(val.get_attribute('href'))
        # shop_name.append(val.get_attribute('href').split('/')[-1])
        # shop_info[val.get_attribute('href').split('/')[-1]] = [val.get_attribute('href')]

    # shop_name_xpath = driver.find_elements_by_xpath("//h3[@class=' businessName']//a")
    # for i in range(len(all_links_xpath)):
    #     shop_name.append(shop_name_xpath[i].text)
    #     shop_info[shop_name_xpath[i].text] = [all_link[i]]

    wait_until_btn_clickable = WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@ng-disabled='noNext()||ngDisabled']")))
    elm = driver.find_element_by_xpath("//a[@ng-disabled='noNext()||ngDisabled']")
    if elm.get_attribute("tabindex") == "-1":
        break
    elm.click()



for val in all_link:
    print(val)