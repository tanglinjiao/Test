coding = "utf-8"
from selenium import  webdriver
import time
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')
time.sleep(1)
driver.quit()
