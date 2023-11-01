
from bs4 import BeautifulSoup
import requests
 
url = 'https://www.pixiv.net/users/12845810/artworks'
urlhtml=requests.get(url)
soup=BeautifulSoup(urlhtml.text,'html.parser')

alink = soup.find_all('img')
logo_url = "https:" + alink[0]["src"]
print(logo_url)
