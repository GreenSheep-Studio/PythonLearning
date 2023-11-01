
from bs4 import BeautifulSoup
import requests
 
url = 'https://gz.centanet.com/ershoufang/'
urlhtml=requests.get(url)
soup=BeautifulSoup(urlhtml.text,'lxml')

alink = soup.find_all('head')
for i in alink:
    print(i)
