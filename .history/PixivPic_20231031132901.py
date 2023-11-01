
from bs4 import BeautifulSoup
import requests
 
url = 'https://gz.centanet.com/ershoufang/'
urlhtml=requests.get(url)
urlhtml.encoding='utf-8'
soup=BeautifulSoup(urlhtml.text,'lxml')

alink = soup.find_all('h4')
for i in alink:
    print(i)
