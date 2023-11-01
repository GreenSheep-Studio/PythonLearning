
from bs4 import BeautifulSoup
import requests
 
url = 'https://www.google.com/webhp?hl=zh-CN&sa=X&ved=0ahUKEwjc6761zp-CAxW5rlYBHdc-CQAQPAgJ'
urlhtml=requests.get(url)
soup=BeautifulSoup(urlhtml.text,'html.parser')

alink = soup.find_all('img',alt = "Google")
logo_url = "https:" + alink[0]['src']
print(logo_url)