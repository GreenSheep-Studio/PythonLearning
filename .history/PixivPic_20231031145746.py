
from bs4 import BeautifulSoup
import requests
 
url = 'https://www.baidu.com'
urlhtml=requests.get(url)
soup=BeautifulSoup(urlhtml.text,'html.parser')
print(soup)
alink = soup.find('img')
print(alink)
