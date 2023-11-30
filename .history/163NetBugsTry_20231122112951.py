import requests
import os
import pickle
from lxml import etree

def main():
    url = 'http://tech.163.com/special/gd2016/'
    r = requests.get(url)
    content =  r.text
    
    rel = etree.HTML(content).xpath("//h3[@class='bigsize ']/a")
    for r in rel:
        print(r.text, end ='/n')

if __name__ == '__main__':
    main()