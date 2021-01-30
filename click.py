from re import search
import time
from bs4 import BeautifulSoup
import requests
#from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from fake_useragent import UserAgent

book_name = input("请输入搜索书名：")
url_search = 'https://so.biqusoso.com/s.php?ie=gbk&siteid=biqukan.com&s=2758772450457967865&q='

driver = webdriver.Firefox()

ua = UserAgent()
headers = {
    'User-Agent': ua.random
}

driver.get('http://www.bqkan.com/')
time.sleep(5)
driver.find_element_by_name("q").send_keys(book_name)
driver.find_element_by_class_name("btn").click()
windows = driver.window_handles
driver.switch_to.window(windows[1])
time.sleep(5)

url = driver.current_url
print(url) 
respose = requests.get(url_search,headers = headers)
html = respose.text
#print(html)
bs = BeautifulSoup(html,'lxml')
chap = bs.find_all('a')
#chap = bs.find('span',class_ = 's2')
tmp = 0
for each in chap:
    tmp+=1
    print(str(tmp)+"."+each.string+each.get('href'))