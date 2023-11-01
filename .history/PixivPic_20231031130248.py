from urllib.request import urlopen
from bs4 import BeautifulSoup as bf
html = urlopen("https://www.pixiv.net/users/12845810/artworks")
obj = bf(html.read(), 'html.parser')
title = obj.head.title
pic_info  = obj.find_all('img')
for i in pic_info:
    print(i)