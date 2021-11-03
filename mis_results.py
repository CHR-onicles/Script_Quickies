from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('B:\\Downloads\\Compressed\\Web Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get('https://ienabler.ug.edu.gh/pls/prodi41/w99pkg.mi_login')

input_id = driver.find_element(By.NAME, 'unum')
input_pin = driver.find_element(By.NAME, 'pin')
input_id.clear()  # to clear field of any initial characters for safety
input_id.send_keys('')  # input your student ID here
input_pin.clear()
input_pin.send_keys('')    # input your PIN here
input_pin.send_keys(Keys.ENTER)

# switching to iFrame containing sidebar menu
sidebar = driver.find_element(By.ID, 'F1')
driver.switch_to.frame(sidebar)

student_enq = driver.find_element(By.ID, 'menuId28')
student_enq.click()
aca_record = driver.find_element(By.ID, 'menuId30')
aca_record.click()
