from selenium import webdriver

import time

from selenium.webdriver.common.by import By

url1='http://xh-test.zhidu30.xinhuimed.net/v3/#/login'
username='admin'
password='Xh@2022!@#'
captcha_code='6666'





driver = webdriver.Chrome()

driver.maximize_window()
# time.sleep(2)
#
# driver.minimize_window()
# time.sleep(2)
# driver.set_window_size(500,800)
# time.sleep(1)
# size = driver.get_window_size()
# print(size)



driver.get(url1)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="pane-username"]/div/div[1]/div/input').send_keys(username)
driver.find_element(By.XPATH, '//*[@id="pane-username"]/div/div[2]/div/input').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="pane-username"]/div/div[3]/div/input').send_keys(captcha_code)
driver.find_element(By.XPATH, '//*[@id="pane-username"]/div/div[4]/button').click()
time.sleep(4)
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[3]').click()
time.sleep(4)
# text = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/header/div/h1').text

driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
# time.sleep()
time.sleep(6)
driver.quit()

