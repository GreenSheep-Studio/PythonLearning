from bs4 import BeautifulSoup
import requests

urlzhihu = "https://www.zhihu.com/question/63610436/answer/2986716866"
urlzhihuHtml = requests.get(urlzhihu)
soupzhihu=BeautifulSoup(urlzhihuHtml.text,'html.parser')
blink = soupzhihu.find_all('p')
ID_list = []
for i in range(6, 78 , 3):
    ID_list.append(blink[i].text)
ID_list = ("".join(ID_list)).split("id=")
ID_list.pop(0)

for ID in ID_list:
    url = 'https://www.pixiv.net/artworks/%d' %int(ID)
    urlhtml=requests.get(url)
    urlhtml.encoding = "utf-8"
    soup=BeautifulSoup(urlhtml.text,'html.parser')
    alink = soup.find_all('meta')
    print(alink[6]["content"])

