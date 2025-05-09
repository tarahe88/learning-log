import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
} #伪装成浏览器
response = requests.get("https://movie.douban.com/top250", headers = headers)
html = response.text
soup = BeautifulSoup(html,"html.parser")
#<span class="title">肖申克的救赎</span>
all_titles = soup.findAll("span", attrs = {"class": "title"}) #返回的是可迭代对象，所以用for 循环
for title in all_titles:
    #print(title) #<span class="title">肖申克的救赎</span> 我们只对文字感兴趣，对周围的html标签不感兴趣
    #print(title.string) #肖申克的救赎 /The Shawshank Redemption 带原版标题，且与中文之间存在斜杠/
    title_string = title.string
    if "/" not in title_string: #就是去掉/后面的文字
        print(title_string) #肖申克的救赎  霸王别姬  阿甘正传 泰坦尼克号



