
from bs4 import BeautifulSoup
import requests
 
url = 'https://www.pixiv.net/users/12845810/artworks'
urlhtml=requests.get(url)
soup=BeautifulSoup(urlhtml.text,'lxml')

alink = soup.find_all('head')
for i in alink:
    print(i)
