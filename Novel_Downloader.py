#   a tool for downloading novel
#   
from re import search
import random
import time
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from requests.models import Response
from tqdm.std import tqdm

ua = UserAgent()
headers = {
    'User-Agent': ua.random
}

def getBookName(book_name):
    
    url_search = 'https://so.biqusoso.com/s.php?ie=gbk&siteid=biqukan.com&s=2758772450457967865&q='

    respose = requests.get(url_search,headers = headers)
    print(respose.request.headers)
    html = respose.text
    bs = BeautifulSoup(html,'lxml')
    chap = bs.find_all('a')

    return chap

def selectBook(chap,x):
    tmp = 0
    # print(x)
    for i in chap:
        tmp+=1
        # print(tmp)
        href = i.get('href')
        if tmp == x:
            return (href)


    

def printList(chap):
    tmp = 0
    for each in chap:
        tmp+=1
        print(str(tmp)+"."+each.string)


def getChapters(url):
    respose = requests.get(url = url, headers = headers)
    print(respose.request.headers)
    html = respose.text
    bs = BeautifulSoup(html,'lxml')
    chapters = bs.find('div',id='lismain')
    # chaptertmp = chapters.find_all('dt')
    chapter = chapters.find_all('a')
    for each in tqdm(chapter):   
        chapDir = each.string           #提取目录
        chapUrl = url+each.get('href')  #具体章节链接
        getContent(chapUrl, chapDir)
    return



def getContent(chapUrl, chapDir):
    respose = requests.get(url = chapUrl, headers = headers)
    print(respose.request.headers)
    # print(res.status_code)
    # print(res.request.headers)
    html = respose.text
    bs = BeautifulSoup(html,'lxml')
    contents = bs.find('div', id = 'content',class_ = 'showtxt')
    content = contents[0].text.replace('\xa0'*8,'\n\n')
    with open('./novelname.txt', 'a', encoding='utf-8') as f:
        f.write(chapDir)
        f.write('\n')
        f.write(content)
        f.write('\n')
    return 

    

if __name__ == '__main__':
    book_name = input("请输入搜索书名：")
    time.sleep(random.uniform(1,5))
    chap = getBookName(book_name)
    printList(chap)
    selection = int(input("select a book"))
    url_novel = selectBook(chap,selection)
    print(url_novel)
    getChapters(url_novel)

    