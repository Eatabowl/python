import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
# from selenium import webdriver

def getChapter(url):
    res = requests.get(url)
    html = res.text
    bs = BeautifulSoup(html,'lxml')
    chapters = bs.find('div',id='list')
    chapter = chapters.find_all('a')
    for each in chapter:   
        chapDir = each.string           #提取目录
        chapUrl = url+each.get('href')  #具体章节链接
        getContent(chapUrl, chapDir)
    return



def getContent(chapUrl, chapDir):
    res = requests.get(chapUrl)
    print(res.status_code)
    print(res.request.headers)
    html = res.text
    bs = BeautifulSoup(html,'lxml')
    contents = bs.find('div',id='content')
    content = contents.text.replace('\xa0'*4,'\n\n')
    with open('./xiaoshuo', 'a', encoding='utf-8') as f:
        f.write(chapDir)
        f.write('\n')
        f.write(content)
        f.write('\n')
    return

    

    


if __name__ == "__main__":
    url = 'https://www.biqugg.com/xs/15432/'
    # driver = webdriver.Chrome()
    # url = input("请输入小说网址:")
    # firefox_login=webdriver.Firefox()
    # firefox_login.get(url)
    # firefox_login.maximize_window()
    print(url)
    getChapter(url)
    # firefox_login.quit()
