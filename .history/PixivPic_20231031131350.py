import requests
from bs4 import BeautifulSoup
html = requests.get("https://www.pixiv.net/users/12845810/artworks")
response = html.text
pic_list = response.find("img")
for i in pic_list:
    print(i)