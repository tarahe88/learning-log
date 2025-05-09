from bs4 import BeautifulSoup
import requests
# <h3> <a href="catalogue/tipping-the-velvet_999/index.html" title="Tipping the Velvet">Tipping the Velvet</a> #
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}
content = requests.get("https://books.toscrape.com/").text
soup = BeautifulSoup(content, "html.parser") #bs可以解析很多对象，# html只是其中之一
all_titles = soup.findAll("h3")
for title in all_titles:
    link = title.find("a") #本身的h3都存在且是第一个a.
    print(link.string)


