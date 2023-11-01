
from bs4 import BeautifulSoup
import requests

ID_list = []
while True:
    IDcode = input()
    if IDcode:
        ID_list.append(int(IDcode))
    else:
        break
for ID in ID_list:
    url = 'https://www.pixiv.net/artworks/%d' %ID
    urlhtml=requests.get(url)
    urlhtml.encoding = "utf-8"
    soup=BeautifulSoup(urlhtml.text,'html.parser')
    alink = soup.find_all('meta')
    print(alink[6]["content"])

urlzhihu = "https://www.zhihu.com/question/63610436/answer/2986716866"
urlzhihuHtml = requests.get(urlzhihu)
soupzhihu=BeautifulSoup(urlzhihuHtml.text,'html.parser')
blink = soupzhihu.find_all('p')
for i in range(6,len(blink),2) :
    print(blink[i]["id"], end = "\n")