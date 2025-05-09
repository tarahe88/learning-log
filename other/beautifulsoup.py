from bs4 import BeautifulSoup
import requests
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}
content = requests.get("https://books.toscrape.com/").text
soup = BeautifulSoup(content, "html.parser") #bs可以解析很多对象，# html只是其中之一
all_prices = soup.findAll("p", attrs={"class":"price_color"}) #找p标签，可以穿入可选参数attrs.键值对class对应price_color
for price in all_prices:
    print(price.string[2:]) #string会把标签包围的文字返回
    # print(price) #<p class="price_color">Â£51.77</p>
    # print(price.string)  #Â£51.77
    # print(price.string[2:]) #51.77



#不同网页信息不一样，爬虫要随机应变