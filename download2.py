# --*-- coding : utf-8 --**--
# --*-- author : muchen --**--
import requests
from bs4 import BeautifulSoup
import threading
import os
import re
chapeterUrl = 'https://www.cnoz.org/0_1/' #小说目录页面
header = {'User-Agent': ''}#每个人的header不一样注意。
webUrl = 'https://www.cnoz.org' #小说章节共同前缀
errorUrl = [] #爬取失败的章节list
filepath = r'./Gui'#存储的地址
filename = '诡秘之主' #最终合并的章节名字
def getChapeterList():
    #获取章节地址list
    html = requests.get(chapeterUrl, headers=header, timeout=20)
    html.encoding = 'gb18030' #注意网页编码
    soup = BeautifulSoup(html.text, "html.parser")
    chapeterList = []
    chapeterListWeb = soup.select('#list > dl > dd > a')#审查元素，对应元素，右键copy select
    del chapeterListWeb[:9] #切片删除无效地址
    for chapeter in chapeterListWeb:
        chapeterList.append(chapeter['href'])
    return chapeterList
def getText(URL):
    #获取章节内容
    html = requests.get(webUrl + URL, headers=header, timeout=20)
    html.encoding = 'gbk'
    soup = BeautifulSoup(html.text, "html.parser")
    #章节名字
    name = soup.select('#wrapper > div.content_read > div > div.bookname > h1')#审查元素，对应元素，右键copy select
    for name in name:
        pageName = name.get_text()
    # 章节内容
    text = soup.select('#content')
    for text in text:
        pageText = text.get_text()
    html.close()
    return pageName, pageText
def writeText(URL):
    #把每章的内容存取下来
    try:
        name, text = getText(URL)
    except Exception as e:
        #如果获取内容失败则会把失败章节地址存入list
        #print(e) #输出错误原因
        errorUrl.append(URL)
        return
    a = URL.split(r'/')
    #这里的命名方式采用了将每个章节地址按‘/’分割后取最后一段
    with open(filepath + r'\\' + a[2] + '.txt', 'w', encoding='utf-8') as f:
        f.write(name + '\n')
        f.write(text)
        #print(name + " 结束")
def writrPart(partList):
    #多线程存取全部章节内容
    #防止出现超时等一些列问题，所以采用循环爬取，一次不成功会再次进入队列等待下一次
    ts = []
    global errorUrl #声明全局变量
    errorUrl = partList[:]
    while errorUrl:
        l = len(errorUrl)
        print(l,'一次')
        ts = []
        if l>=300:
            l = 300#将每次最大线程数设置为300，防止溢出，可以尝试调大数值
        print(l, '二次')
        for url in range(l):
            try:
                t = threading.Thread(target=writeText, args=(errorUrl[url],))
                # print(t)
                ts.append(t)
                t.start()
            except Exception as e:
                #如果线程打开失败，将章节地址存入list之后
                #print(e)
                errorUrl.append(url)
                continue
        #等所有进程都结束再进行下一步
        for i in ts:
            i.join()
        del errorUrl[0:l]#删除已经存取过的章节地址
        print('一次结束')
def hb():
    #将所有章节合并
    global filepath
    list = os.listdir(filepath)
    list = sorted(list, key=lambda i: int(re.match(r'(\d+)', i).group()))
    with open(filepath + filename + '.txt', 'w', encoding='utf-8') as f:
        for i in list:
            filepath2 = os.path.join(filepath, i)
            print(i)
            with open(filepath2, encoding='utf-8') as ff:
                content = ff.read()
            ff.close()
            f.write(content)

if __name__ == "__main__":
    chapeterList = getChapeterList()
    del chapeterList[0:1000]
    writrPart(chapeterList)
    hb()
