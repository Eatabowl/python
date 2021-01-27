import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url = target) 
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div', class_ = 'showtxt')
    print(texts[0].text.replace('\xa0'*8,'\n\n'))

    # target = 'http://www.biqukan.com/1_1094/'
    # req = requests.get(url = target)
    # req.encoding = "utf-8"
    # html = req.text
    # div_bf = BeautifulSoup(html)
    # div = div_bf.find_all('div', class_ = 'listmain')
    # print(div[0].text)
