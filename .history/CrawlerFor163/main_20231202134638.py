from crawlers import TitleCrawler


def main():
  url = 'http://tech.163.com/special/gd2016/'
  crawler = TitleCrawler()
  crawler.doCrawl(url)
  crawler.saveCache()

  print(f"page's count: {len(crawler.pages)}\n", crawler.pages[:10])

  print('Done.')


if __name__ == '__main__':
  main()
