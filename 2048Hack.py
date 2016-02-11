#! python3

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

ff = webdriver.Firefox()

try:
    ff.get('https://gabrielecirulli.github.io/2048/')
    htmlElem = ff.find_element_by_tag_name('html')
    retryButtonElem = ff.find_element_by_class_name('retry-button')
    gameoverElem = WebDriverWait(ff, 1).until(EC.presence_of_element_located((By.CLASS_NAME, 'retry-button')))

    while True:
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)

except:
    print('Something Happened')
