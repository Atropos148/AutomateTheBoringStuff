#! python3

import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('http://gmail.com')
try:
    emailElem = browser.find_element_by_id('Email')
    emailElem.send_keys('pythonTesting148')

    nextButtonElem = browser.find_element_by_id('next')
    nextButtonElem.click()

    passwordElem = WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.ID, 'Passwd')))
    passwordElem.send_keys('morrowind')

    signInElem = browser.find_element_by_id('signIn')
    signInElem.click()

    browser.implicitly_wait(10)

    composeElem = browser.find_element_by_xpath("//div[@class= 'T-I J-J5-Ji T-I-KE L3']")
    composeElem.click()

    sendToElem = browser.find_element_by_id(':9i')
    sendToElem.send_keys(sys.argv[1])

    subjectElem = browser.find_element_by_name('subjectbox')
    subjectElem.send_keys(sys.argv[2])

    emailBodyElem = browser.find_element_by_id(':a5')
    for word in sys.argv[3:]:
        emailBodyElem.send_keys(word + ' ')

    sendButtonElem = browser.find_element_by_id(':8s')
    sendButtonElem.click()

except:
    print('No email field found!')
