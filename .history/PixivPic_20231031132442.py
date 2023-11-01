
from bs4 import BeautifulSoup
import requests
 
url = 'https://www.pixiv.net/users/12845810/artworks/'
urlhtml=requests.get(url)
urlhtml.encoding='utf-8'
soup=BeautifulSoup(urlhtml.text,'lxml')
 
alink = soup.find_all('img')
for i in alink:
    print(i)
