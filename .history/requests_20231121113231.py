import requests
import os
import pickle
from lxml import etree

def main():
  #TODO:加载上次保存的pages_dict
  pages_dict_filename = 'pages_dict.pkl'
  if os.path.exists(pages_dict_filename):
    with open(pages_dict_filename, 'rb') as f:
      pages_dict = pickle.load(f)
  else:
    pages_dict = {}
  
  url = 'http://tech.163.com/special/gd2016/'
  while 1:
    if url not in pages_dict:
      r = requests.get(url)
      content = pages_dict[url] = r.text
    else:
      content = pages_dict[url]
      print(f'Use cached content.')
  
    rel = etree.HTML(content)
    titles = rel.xpath("//h3[@class='bigsize ']/a")
    for title in titles:
      print(title.text)
      # print(title.get('href'))
    next_page_link = rel.xpath("//a[@class='pages_flip'][last()]")
    if next_page_link[0].text == '<':
      break
    next_url = next_page_link[0].get('href')
    url = 'http:' + next_url
    print('new url:', url)
    # break
  
  #TODO:保存pages_dict到磁盘
  with open(pages_dict_filename, 'wb') as f:
    pickle.dump(pages_dict, f)

  print('Done.')

if __name__ == '__main__':
  main()