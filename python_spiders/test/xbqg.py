import requests
import os

from bs4 import BeautifulSoup

if __name__ == '__main__':
    url1 = 'https://www.xsbiquge.com/15_15338/8549128.html'
    res = requests.get(url1)
    res.encoding = 'utf-8'
    html = res.text

    bs = BeautifulSoup(html,'lxml')

    text1 = bs.find('div',id='content')
    text2 = text1.text.replace('\xa0'*4,'\n\n')

    # fd = open('./xbqg.txt','a')
    # fd.write('\n\n\n')
    # fd.write(text2)
    # fd.close()
    
    server = 'https://www.xsbiquge.com'
    url2 = 'https://www.xsbiquge.com/15_15338/'
    res2 = requests.get(url2)
    res2.encoding = 'utf-8'

    html2 = res2.text

    bs2 = BeautifulSoup(html2,'lxml')
    text3 = bs2.find('div',id='list')
    text4 = text3.find_all('a')
    for each in text4:
        url3 = each.get('href')
        print(each.string)
        # print(server+ url3)
    # print(text4)
    # for text4 in text3:
    # fd = open('./xbqg.txt','a')
    # fd.write('\n\n\n')
    # fd.write(text4)
    # fd.close()


