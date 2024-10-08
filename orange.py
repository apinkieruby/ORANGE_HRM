import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# set up the browser
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
