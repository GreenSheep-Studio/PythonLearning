
from bs4 import BeautifulSoup
import requests
 
url = 'https://www.pixiv.net/artworks/78371847'
urlhtml=requests.get(url)
urlhtml.encoding = "utf-8"
soup=BeautifulSoup(urlhtml.text,'html.parser')

alink = soup.find_all('meta')
print(alink[6]["content"])
