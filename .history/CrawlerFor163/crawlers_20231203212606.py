import os
import pickle
import requests
from lxml import etree


class Crawler():

  def __init__(self, cache_filename='pages_dict.pkl'):
    self.page_cache = dict()
    self.cache_filename = cache_filename
    self.loadCache()
    self.queue = []
    self.pages = []

  def loadCache(self):
    if os.path.exists(self.cache_filename):
      with open(self.cache_filename, 'rb') as f:
        self.page_cache = pickle.load(f)
    else:d
      self.page_cache = {}

  def saveCache(self):
    with open(self.cache_filename, 'wb') as f:
      pickle.dump(self.page_cache, f)

  def doCrawl(self, url):
    self.queue.append(url)
    while len(self.queue) > 0:
      url = self.queue.pop(0)
      self.crawlPage(url)

  def crawlPage(self, url):
    if url not in self.page_cache:
      r = requests.get(url)
      content = self.page_cache[url] = r.text
    else:
      content = self.page_cache[url]
      print(f'Use cached content.')

    rel = etree.HTML(content)
    titles = rel.xpath("//h3[@class='bigsize ']/a")
    for title in titles:
      title_text = title.text
      title_link = title.get('href')
      self.queue.append(title_link)
      self.pages.append((title_text, title_link))
    next_page_link = rel.xpath("//a[@class='pages_flip'][last()]")
    if next_page_link[0].text != '<':
      next_url = next_page_link[0].get('href')
      url = 'http:' + next_url
      self.queue.append(url)


class TitleCrawler(Crawler):

  def __init__(self, cache_filename='pages_dict.pkl'):
    self.page_cache = dict()
    self.cache_filename = cache_filename
    self.loadCache()
    self.queue = []
    self.pages = []
    self.titles = []

  def crawlPage(self, url):
    if url not in self.page_cache:
      r = requests.get(url)
      content = self.page_cache[url] = r.text
    else:
      content = self.page_cache[url]
      print(f'Use cached content.')

    rel = etree.HTML(content)
    if 'tech.163.com/special' in url:
      titles = rel.xpath("//h3[@class='bigsize ']/a")
      for title in titles:
        title_text = title.text
        title_link = title.get('href')
        self.queue.append(title_link)
        self.pages.append((title_text, title_link))
      next_page_link = rel.xpath("//a[@class='pages_flip'][last()]")
      if next_page_link[0].text != '<':
        next_url = next_page_link[0].get('href')
        url = 'http:' + next_url
        self.queue.append(url)
    else:
      #TODO:解析正文页提取标题
      pass