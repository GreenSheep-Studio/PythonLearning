
from bs4 import BeautifulSoup
import requests
 
url = 'https://www.baidu.com'
urlhtml=requests.get(url)
urlhtml.encoding = "utf-8"
soup=BeautifulSoup(urlhtml.text,'html.parser')

alink = (soup.find_all('img'))[1]["src"]
print("https:" + alink)
