from typing import Text
import requests
import time
from fake_useragent import UserAgent
from tqdm import tqdm
from bs4 import BeautifulSoup
# from selenium import webdriver


if __name__ == "__main__":
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    print(headers)
    target = 'https://www.bqkan.com/1_1094/'
    response = requests.get(url = target, headers = headers)
    print(response.headers)
    print(response.status_code)
    bf = BeautifulSoup(response.text)
    b = bf.find_all('div',id = 'content',class_ = 'showtext' )
    print(b[0].text.replace('\xa0'*8,'\n'))
    