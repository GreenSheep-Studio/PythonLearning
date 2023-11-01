
from bs4 import BeautifulSoup
import requests
 
url = 'https://www.baidu.com'
urlhtml=requests.get(url)
soup=BeautifulSoup(urlhtml.text,'html.parser')

alink = soup.find_all('img')
logo_url = "https:" + alink[0]["src"]
print(alink)
