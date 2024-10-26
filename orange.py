import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# set up the browser
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

# login
enter_username = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
enter_username.send_keys('Admin')
time.sleep(10)

enter_password = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
enter_password.send_keys('admin123')
time.sleep(5)

click_login_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
click_login_button.click()
time.sleep(5)

#My Info
click_my_info = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span')
click_my_info.click()
time.sleep(10)

#Admin
click_admin = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
click_admin.click()
time.sleep(5)

#Job
click_job = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
click_job.click()
time.sleep(5)

#Job Title
click_job_title = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a')
click_job_title.click()
time.sleep(5)

#Add Job Title
click_add_job_title = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button')
click_add_job_title.click()
time.sleep(5)

#Job Title
enter_job_title = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input')
enter_job_title.send_keys('Tester')
time.sleep(5)

#Job Description
enter_job_description = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea')
enter_job_description.send_keys('Coordinating and supporting the planning, execution and monitoring of projects within an organization')
time.sleep(5)

click_save = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]')
click_save.click()
time.sleep(5)

click_job = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
click_job.click()
time.sleep(10)

#pay grade
click_pay_grade = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]/a')
click_pay_grade.click()
time.sleep(5)

click_add_pay_grade = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button')
click_add_pay_grade.click()
time.sleep(5)

enter_pay_grade = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input')
enter_pay_grade.send_keys('Grade 12')
time.sleep(5)

click_save = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
click_save.click()
time.sleep(5)

click_job = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
click_job.click()
time.sleep(10)

#Employment Status
click_employment_status = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[3]/a')
click_employment_status.click()
time.sleep(10)

click_add = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button/i')
click_add.click()
time.sleep(10)

# Employment name
enter_add_employment_name = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input')
enter_add_employment_name.send_keys('Intern')
time.sleep(10)

click_send = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
click_send.click()
time.sleep(10)

#Job categories
click_job = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]')
click_job.click()
time.sleep(10)

click_job_category = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[4]/a')
click_job_category.click()
time.sleep(10)

# add job category
click_add_job_category = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div[1]/div/button')
click_add_job_category.click()
time.sleep(10)

enter_name = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input')
enter_name.send_keys('Busola')
time.sleep(10)

click_save_job_category = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')
click_save_job_category.click()
time.sleep(5)

#PIM
click_PIM = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
click_PIM.click()
time.sleep(5)

#Leave
click_leave = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span')
click_leave.click()
time.sleep(5)

#Time
click_time = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a')
click_time.click()
time.sleep(5)

#Recruitment
click_recruitment = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span')
click_recruitment.click()
time.sleep(5)

#Performance
click_recruitment = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span')
click_recruitment.click()
time.sleep(5)

#Directory
click_directory = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a')
click_directory.click()
time.sleep(5)

#Mainteniance
click_mainteniance = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span')
click_mainteniance.click()
time.sleep(5)

#Adminstrator Access
enter_password = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/form/div[3]/div/div[2]/input')
enter_password.send_keys('admin123')
time.sleep(10)

click_admin_confirm = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/form/div[4]/button[2]')
click_admin_confirm.click()
time.sleep(10)

#Claim
click_claim = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span')
click_claim.click()
time.sleep(10)

#Buzz
click_buzz = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span')
click_buzz.click()
time.sleep(5)