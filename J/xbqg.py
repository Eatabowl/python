import requests
from bs4 import BeautifulSoup
# def getChar(url):
    # res = requests.get(url)
    # html = res.text
    # bs = BeautifulSoup(html,'lxml')
    # chara = bs.find('div',id='list')
    # charac = chara.find_all('a')
    # for each in charac:   
        # print(each.string)  #提取目录
        # print(url+each.get('href'))  #具体章节链接
    


if __name__ == '__main__':
    url = 'https://www.biqugg.com/xs/15432/'
    res = requests.get(url)
    html = res.text
    bs = BeautifulSoup(html,'lxml')
    chara = bs.find('div',id='list')
    charac = chara.find_all('a')
    for each in charac:   
        chapurl = url+each.get('href')
        chapter_name = each.string
        res1 = requests.get(chapurl)
        html1 = res1.text
        bs1 = BeautifulSoup(html1,'lxml')
        content = bs1.find('div',id='content')
        contents = content.text.replace('\xa0'*4,'\n\n')
        with open('./xiaoshuo', 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write(contents)
            f.write('\n')

        
        

    
