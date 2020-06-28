#作业一： 使用 Requests、bs4库 抓取猫眼电影 前10个电影名、
# 类型和上映时间，并以UTF-8保存到csv文件

import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

header ={'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showtype=3'

response = requests.get(myurl,headers = header)

bs_info = bs(response.text, 'html.parser')

for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-title'}):
    for atag in tags.find_all('span'):
        print(atag.find('span',attrs={'class': 'name'}).text)
        # 获取电影名称
        print(atag.find('span',attrs={'class': 'hover-tag'}).text)
        # 获取电影类型
        print(atag.find('span',attrs={'class': 'hover-tag'}).text)
        # 获取上映时间

