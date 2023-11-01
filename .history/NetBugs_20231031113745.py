import requests
from bs4 import BeautifulSoup

url = 'http://www.weather.com.cn/weather/101010100.shtml'

def getHTMLText(url, timeout = 30):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except :
        return "Err"
    
html = getHTMLText(url)
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())