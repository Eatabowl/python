import time
from selenium import webdriver
driver = webdriver.Firefox()

driver.get('http://www.bqkan.com/')

time.sleep(5)

driver.find_element_by_name("q").send_keys(u"青岛")
driver.find_element_by_class_name("btn").click()
url = driver.current_url
print(url)