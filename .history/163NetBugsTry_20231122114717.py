import requests
import os
import pickle
from lxml import etree

def main():
    while 1:
        url = 'http://tech.163.com/special/gd2016/'
        r = requests.get(url)
        content =  r.text
    
        rel = etree.HTML(content).xpath("//h3[@class='bigsize ']/a")
        for r in rel:
            print(r.text, end ='\n\n')
        
        next_page = etree.HTML(content).xpath ("//a[@class='pages_flip'][last()]")
        if next_page[0].text == '<':
            break
        next_url = next_page[0].get('href')
        url = 'http:' + next_url
if __name__ == '__main__':
    main()