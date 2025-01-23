import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# set up the browser
driver = webdriver.Chrome()
driver.get("https://automationplayground.com/crm/login.html")
driver.maximize_window()
time.sleep(2)

click_sign_in = driver.find_element(By.XPATH, '/html/body/nav/ul/li/a')
click_sign_in.click()
time.sleep(2)

# login
enter_username = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/form/div[1]/input')
enter_username.send_keys('apinkieruby@gmail.com')
time.sleep(2)

enter_password = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/form/div[2]/input')
enter_password.send_keys('football')
time.sleep(2)

check_remember_me = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/form/div[3]/label/input')
check_remember_me.click()
time.sleep(2)

# submit button
click_submit_button = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/form/button')
click_submit_button.click()
time.sleep(2)

# New Customer
click_New_Customer = driver.find_element(By.XPATH, '/html/body/div/a')
click_New_Customer.click()
time.sleep(2)

# enter email
enter_email = driver.find_element(By.ID, "EmailAddress")
enter_email.send_keys('busolaolubiyi@gmail.com')
time.sleep(2)

# enter first name
enter_firstname = driver.find_element(By.ID, 'FirstName')
enter_firstname.send_keys('Ayomide')
time.sleep(2)

enter_lastname = driver.find_element(By.ID, 'LastName')
enter_lastname.send_keys('Odunlade')
time.sleep(2)

# enter city
enter_city = driver.find_element(By.ID, 'City')
enter_city.send_keys('Lagos')
time.sleep(2)

# State
click_state = driver.find_element(By.ID, "StateOrRegion")
click_state.click()
time.sleep(2)

enter_state = driver.find_element(By.ID, 'StateOrRegion')
enter_state.send_keys('Alabama')
time.sleep(2)

# gender
click_gender_female = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/form/div[6]/input[2]')
click_gender_female.click()
time.sleep(2)

# submit button
click_submit_button = driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/form/button')
click_submit_button.click()
time.sleep(2)
