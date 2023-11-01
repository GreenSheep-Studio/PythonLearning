import requests
from bs4 import BeautifulSoup
html = requests.get("https://www.pixiv.net/users/12845810/artworks")
obj = BeautifulSoup(html, 'html.parser')
title = obj.head.title
pic_info  = obj.find_all('img')
for i in pic_info:
    print(i)