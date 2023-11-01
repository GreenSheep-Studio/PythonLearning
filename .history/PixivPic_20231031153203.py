
from bs4 import BeautifulSoup
import requests
 
url = 'https://www.pixiv.net/artworks/110149485'
urlhtml=requests.get(url)
urlhtml.encoding = "utf-8"
soup=BeautifulSoup(urlhtml.text,'html.parser')
print(urlhtml)
alink = soup.find_all('meta')
for i in alink:
    print(i, end = "\n")
