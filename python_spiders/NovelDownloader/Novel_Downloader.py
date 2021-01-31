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

server = 'http://www.bqkan.com/'

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
    div_bf = BeautifulSoup(html,'lxml')
    div = div_bf.find_all('div', class_ = 'listmain')
    # print(div[0])
    a_bf = BeautifulSoup(str(div[0]),'lxml')
    chapter = a_bf.find_all('a')
    # div = bs.find_all('div',class_='lismain')
    # print(div[0])
    # chapters = BeautifulSoup(str(chapt[0]))
    # chaptertmp = chapters.find_all('dt')
    # chapter = chapters.find_all('a')
    for each in tqdm(chapter):   
        time.sleep(random.uniform(1,2))
        chapDir = each.string           #提取目录
        chapUrl = server+each.get('href')  #具体章节链接   urlzhisever
        # print(chapUrl)
        # print(chapDir)
        # print('hehehhehehhehehehehehehehehehehe')
        getContent(chapUrl, chapDir)
    return



def getContent(chapUrl, chapDir):
    # print(chapUrl)
    # print(chapDir)
    respose = requests.get(url = chapUrl, headers = headers)
    # print(respose.request.headers)
    # print(res.status_code)
    # print(res.request.headers)
    html = respose.text
    bf = BeautifulSoup(html,'lxml')
    texts = bf.find_all('div', class_ = 'showtxt')
    # print(texts[0])
    texts = texts[0].text.replace('\xa0'*8,'\n\n')
    # contents = bs.find_all('div',class_ = 'showtxt')
    # content = contents.text.replace('\xa0'*8,'\n\n')
    with open('./novelname.txt', 'a', encoding='utf-8') as f:
        f.write(chapDir)
        f.write('\n')
        f.write(texts)
        f.write('\n')
    return 

    

if __name__ == '__main__':
    book_name = input("请输入搜索书名：")
    time.sleep(random.uniform(1,5))
    chap = getBookName(book_name)
    printList(chap)
    selection = int(input("select a book"))
    url_novel = selectBook(chap,selection)
    # print(url_novel)
    # print('urlllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll')
    getChapters(url_novel)

    