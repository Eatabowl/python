#   a tool for downloading novel
#   
from re import search
import random
import time
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    'User-Agent': ua.random
}

def getBookName(book_name):
    
    url_search = 'https://so.biqusoso.com/s.php?ie=gbk&siteid=biqukan.com&s=2758772450457967865&q='

    respose = requests.get(url_search,headers = headers)
    html = respose.text
    bs = BeautifulSoup(html,'lxml')
    chap = bs.find_all('a')

    return chap

def selectBook(chap,x):
    tmp = 0
    print(x)
    for i in chap:
        tmp+=1
        print(tmp)
        href = i.get('href')
        if tmp == x:
            return (str(tmp)+"."+href)


    

def printList(chap):
    tmp = 0
    for each in chap:
        tmp+=1
        print(str(tmp)+"."+each.string)



if __name__ == '__main__':
    book_name = input("请输入搜索书名：")
    time.sleep(random.uniform(1,5))
    chap = getBookName(book_name)
    printList(chap)

    selection = input("select a book")

    selectBook(chap,selection)
    