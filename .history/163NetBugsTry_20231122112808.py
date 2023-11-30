import requests
import os
import pickle
from lxml import etree

def main():
    page_dict_file = "page_dict.pkl"
    if os.path.exists(page_dict_file):
        with open(page_dict_file, "rb") as f:
            page_dict = pickle.load(f)
    else:
        page_dict = {}
    url = 'http://tech.163.com/special/gd2016/'
    if url not in page_dict:
        r = requests.get(url)
        content = page_dict[url] = r.text
    else:
        content = page_dict[url]
        print(f'Use cached content.')
    
    rel = etree.HTML(content).xpath("//h3[@class='bigsize ']/a")
    for r in rel:
        print(r.text)

if __name__ == '__main__':
    main()