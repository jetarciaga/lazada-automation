#!/usr/bin/env python3
import os
import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


file = os.path.join('..', 'credentials', 'log_lazada.json')
with open(file, 'r') as login_details:
    login = json.load(login_details)

driver = webdriver.Firefox() #opens firefox browser

def login_page():
    try:
        driver.get('https://sellercenter.lazada.com.ph')
        time.sleep(2)
    except:
        driver.get(driver.current_url)
        print('Refreshing page...')
        time.sleep(2)

def credentials():
    element = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,"//button[@type='button']"))
    )
    email = driver.find_element_by_name('TPL_username')
    email.send_keys(login['email'])
    password = driver.find_element_by_name('TPL_password')
    password.send_keys(login['password'])
    password.send_keys(Keys.RETURN)

for i in range(1,6): #loop if login page fail to load
    if 'Seller' not in driver.title:
        login_page()
    else:
        print('Login Attempts ' + str(i))
        credentials()
        break

print('Login Successfully')
time.sleep(5)

for i in range(1,6): #close announcement pop-up then go to pending orders
    try:
        pending_orders = driver.find_element_by_xpath(
            "//div[@class='asc-task-list']/a[@class='asc-task-item aplus-auto-exp']"
            )
        pending_orders.click()
        break
    except:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
        By.CLASS_NAME, 'next-dialog-close'))
        )
        driver.get(driver.current_url)
        time.sleep(5)
        close_announcement = driver.find_element_by_class_name(
            'next-dialog-close'
            )
        close_announcement.click()
        print('Closing Announcement')
    time.sleep(5)
print('Going to Pending Orders page...')

for i in range(1,6):
    if len(driver.window_handles) == 2:
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)
        close_reminder = driver.find_element_by_class_name(
            'next-dialog-close')
        close_reminder.click()
        time.sleep(3)
        break
    else:
        print('Current tabs open ' + str(len(driver.window_handles)))
        time.sleep(3)

print('You are now in order page...')

order_checkbox = driver.find_element_by_xpath("(//input[@type='checkbox'])[1]")
order_checkbox.click()
hover_print = driver.find_element_by_xpath("(//button[@type='button'])[2]")
hover = ActionChains(driver).move_to_element(hover_print)
hover.perform()
time.sleep(3)
#separate action xpath will only appear when hover_print is mouse over
hover_document = driver.find_element_by_xpath(
    "//ul[@class='next-menu-content']/li[position()=1]"
)
hover_next = ActionChains(driver).move_to_element(hover_document).click()
hover_next.perform()
print("Printing needs manual intervention")
