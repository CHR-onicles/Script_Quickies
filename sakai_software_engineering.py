from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# replace path with the path to your web driver
driver = webdriver.Chrome('B:\\Downloads\\Compressed\\Web Drivers\\chromedriver_win32\\chromedriver.exe')
driver.get('https://sakai.ug.edu.gh/')

input_id = driver.find_element(By.ID, 'eid')
input_id.clear()
input_id.send_keys('')    # input your student ID here
input_pin = driver.find_element(By.ID, 'pw')
input_pin.clear()
input_pin.send_keys('')    # input your PIN here
input_pin.send_keys(Keys.ENTER)

softeng = driver.find_element(By.LINK_TEXT, 'CSCD 306 1 S2-2021')
softeng.click()

lessons = driver.find_element(By.CSS_SELECTOR, '[href="https://sakai.ug.edu.gh/portal/site/CSCD-306-1-S2-2021/tool/0988f8c0-1411-4340-8cc7-01db6b4d4ce0"]')
lessons.click()

# Open notifications to see what new
notifs = driver.find_element(By.ID, 'Mrphs-academic-bullhorn')
notifs.click()