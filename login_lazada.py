#!/usr/bin/env python3
import os
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

file = os.path.join('..', 'credentials', 'log_lazada.json')
with open(file, 'r') as login_details:
    login = json.load(login_details)
baseUrl = 'https://sellercenter.lazada.com.ph'
driver = webdriver.Firefox() #opens firefox browser


driver.get(baseUrl)

def element_wait():
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//button[@type='button']"))
    )

while 'Seller' not in driver.title:
    driver.get(driver.current_url)
    time.sleep(5)
    if 'Seller' in driver.title:
        break

try:
    element_wait()
except TimeoutException:
    print('Refreshing page...')
    driver.get(driver.current_url)
    element_wait()

assert 'Seller' in driver.title
email = driver.find_element_by_name('TPL_username')
email.send_keys(login['email'])
password = driver.find_element_by_name('TPL_password')
password.send_keys(login['password'])
password.send_keys(Keys.RETURN)
print('Login Successfully')

close_className = 'next-dialog-close'

while 'asc-task-item' not in driver.page_source:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
        (By.CLASS_NAME, close_className))
    )
    if 'next-overlay-backdrop' in driver.page_source:
        break

close_announcement = driver.find_element_by_class_name(
    close_className
    )
close_announcement.click()

pending_orders = driver.find_element_by_xpath(
    "//div[@class='asc-task-list']/a[@class='asc-task-item aplus-auto-exp']"
    )
pending_orders.click()
print('Going to Pending Orders page...')
