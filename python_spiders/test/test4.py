import requests
from bs4 import BeautifulSoup
 
if __name__ == '__main__':
    target = 'https://www.xsbiquge.com/15_15338/'
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    bs = BeautifulSoup(html, 'lxml')
    chapters = bs.find('div', id='list')
    chapters = chapters.find_all('a')
    for chapter in chapters:
        print(chapter)
