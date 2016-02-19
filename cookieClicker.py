#! python3

import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES

ff = webdriver.Firefox()
ff.get('http://orteil.dashnet.org/cookieclicker/')

try:
    bigCookie = ff.find_element_by_id('bigCookie')

    while True:
        bigCookie.click()

except:
    print('Something happened')
