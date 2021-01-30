import requests
import time
from fake_useragent import UserAgent
from tqdm import tqdm
from bs4 import BeautifulSoup
# from selenium import webdriver

ua = UserAgent()
headers = {
    'User-Agent': ua.random
}


def getChapter(url):
    global ua
    global headers
    res = requests.get(url, headers = headers)
    html = res.text
    bs = BeautifulSoup(html,'lxml')
    chapter = bs.find('div',id='listmain').find_all('a')
    # chapter = chapters.find_all('a')
    for each in tqdm(chapter):   
        chapDir = each.string           #提取目录
        chapUrl = url+each.get('href')  #具体章节链接
        getContent(chapUrl, chapDir)
    return

def getContent(chapUrl, chapDir):
    global ua
    global headers
    res = requests.get(chapUrl, headers = headers, timeout=10)
    with open('novel.log', 'a', encoding='utf-8') as l:
        l.write(chapDir)
        l.write('\n')
        l.write(str(res.status_code))
        l.write('\n')
        l.write(str(res.status_code))
    html = res.text
    bs = BeautifulSoup(html,'lxml')
    contents = bs.find('div',id='content')
    content = contents.text.replace('\xa0'*4,'\n\n')
    with open('./小说.txt', 'a', encoding='utf-8') as f:
        f.write(chapDir)
        f.write('\n')
        f.write(content)
        f.write('\n')
    return

if __name__ == "__main__":
    url = 'https://www.biqugg.com/xs/5499/'
    print(url)
    getChapter(url)
