import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# set up the browser
driver = webdriver.Chrome()
driver.get("https://automationplayground.com/crm/login.html")
driver.maximize_window()
time.sleep(5)

click_sign_in = driver.find_element(By.XPATH, '/html/body/nav/ul/li/a')
click_sign_in.click()
time.sleep(10)

# login
enter_username = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/form/div[1]/input')
enter_username.send_keys('apinkieruby@gmail.com')
time.sleep(10)

enter_password = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/form/div[2]/input')
enter_password.send_keys('football')
time.sleep(5)

check_remember_me = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/form/div[3]/label/input')
check_remember_me.click()
time.sleep(5)

# submit button
click_submit_button = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/form/button')
click_submit_button.click()
time.sleep(5)