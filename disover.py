from selenium import webdriver
import time
import urllib
driver = webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("http://the-internet.herokuapp.com/login")

driver.find_element_by_id("username").send_keys("testing")
time.sleep(2)
driver.find_element_by_id("password").send_keys("test123")
driver.find_element_by_xpath('//*[@id="login"]/button').click()
time.sleep(2)
driver.refresh()
driver.find_element_by_id("username").send_keys("tomsmith")
driver.find_element_by_id("password").send_keys("SuperSecretPassword!")
driver.find_element_by_xpath('//*[@id="login"]/button').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="content"]/div/a').click()
driver.stop_client()
driver.get("http://the-internet.herokuapp.com/")