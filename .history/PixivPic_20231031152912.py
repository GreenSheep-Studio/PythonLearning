
from bs4 import BeautifulSoup
import requests
 
url = 'https://www.pexels.com/zh-cn/search/Genshin/'
urlhtml=requests.get(url)
urlhtml.encoding = "utf-8"
soup=BeautifulSoup(urlhtml.text,'html.parser')

alink = soup.find_all('meta')
for i in alink:
    print(i, end = "\n")
