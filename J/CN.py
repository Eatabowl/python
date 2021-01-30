import requests
from fake_useragent import UserAgent
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
# from selenium import webdriver


headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
            }


def getChapter(url):

    global headers
    res = requests.get(url, headers = headers)
    html = res.text.encode('utf-8','ignore')
    bs = BeautifulSoup(html,'lxml')
    chapter = bs.find('div',id='list').find_all('a')
    # chapter = chapters.find_all('a')
    tmp = 0
    for each in tqdm(chapter):
        tmp+=1
        if tmp <838:
            continue 
        chapDir = each.string           #提取目录
        chapUrl = url+each.get('href')  #具体章节链接
        getContent(chapUrl, chapDir)
    return

def getContent(chapUrl, chapDir):
    global headers
    res = requests.get(chapUrl, headers = headers, verify=False, timeout=100)
    with open('novel.log', 'a', encoding='utf-8') as l:
        l.write(chapDir)
        l.write('\n')
        l.write(str(res.status_code))
        l.write('\n')
        l.write(str(res.status_code))
    html = res.text.encode('utf-8','ignore')
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
