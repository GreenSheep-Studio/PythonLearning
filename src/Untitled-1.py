import requests
from lxml import etree

def main():
    url = "http://tech.163.com/special/gd2016/"
    r = requests.get(url)
    content = r.text

    rel = etree.HTML(content).xpath("//a[@class='pages_flip'][last()]")
    next_page = rel[0].get("href")
    for e in rel:
        print(e.text)
    print(next_page)