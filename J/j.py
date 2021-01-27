import requests
import re
import time
import socket
socket.setdefaulttimeout(10)
novl_url='http://www.tianyashuku.com/wuxia/7/'
send_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"
    }#伪装成浏览器
#小说的url
response=requests.get(novl_url,send_headers)#访问
response.close()
 
response.encoding='utf-8'
html=response.text
#print(html)
title=re.findall('<title>(.*?)</title>',html)[0]
fp=open('%s.txt'%title,'w',encoding='utf-8')
print(title)
fp.write(title)
fp.write('\n\n')
chapter_info=re.findall('<a href="(.*?)" title="(.*?)">.*?</a>',html)
 
for chapter in chapter_info:
    chapter_title=chapter[1]
    chapter_url='http://www.tianyashuku.com' +chapter[0]
    print(chapter_url,chapter_title)
    try:
        chapter_response=requests.get(chapter_url,send_headers)
        chapter_response.encoding='utf-8'
        chapter_html=chapter_response.text
        chapter_response.close()
        print(chapter_html)
 
        chapter_content=re.findall(r'<[P/p]>&nbsp;&nbsp;&nbsp; (.*?)</[P/p]>',chapter_html);
        fp.write(chapter_title)
        fp.write('\n')
        try :
            for content in chapter_content:
                temp=str(content)
                temp=temp.replace('&middot;','.')
                temp=temp.replace('&rdquo;','”')
                temp=temp.replace('&ldquo;','“')
                temp=temp.replace('&hellip;','…')
                temp=temp.replace('&mdash;','—')
                temp=temp.replace('&rsquo;','’')
                temp=temp.replace('&lsquo;','‘')
 
                fp.write(temp)
                fp.write('\n  ')
            print("成功访问并写入:%s"%chapter_title)
            fp.write('\n')
        except:
            print("写入出错!")
    except:
           print("访问失败!")
#fp.close()
print(len(chapter_info))
