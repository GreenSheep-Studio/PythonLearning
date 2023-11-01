import requests
from bs4 import BeautifulSoup


cityDict = {
    "北京":101010100,"上海":101020100,
    "天津":1010301000,"重庆":101040100
}

def getHTMLText(url, timeout = 30):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except :
        return "Err"

def get_data(html) :
    finallist = []
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.body
    data = body.find('div', {'id':'7d'})
    ul = data.find('ul')
    lis = ul.find_all('li')
    for day in lis:
        templist = []
        date = day.find('hl').string
        templist.append(date)
        info = day.find_all('p')
        templist.append(info[0].string)
        if info[1].find('span'):
            temperature_highest = info[1].find('span').string
        if info[1].find('i'):
            wind_scale = info[2].find('i').string

def main():
    while (True):
        try:
            cityName = input("Enter : ")
            if cityName == 'q' or cityName == 'Q':
                print("Esc")
                break
            cityCode = cityDict[cityName]
            url = 'http://www.weather.com.cn/weather/%d.shtml' %cityCode
            html = getHTMLText(url)
            finallist = get_data(html)
            print(requests.get(url))
            print(finallist, 7,cityName)
        except:
            print("Err")

if __name__ == '__main__':
    main()
