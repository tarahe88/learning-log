''' 项目1
以下是一个简单的python爬虫项目，适合新手小白学习。使用requests库来发送http请求，并使用beautifulsoup库来解析html内容
项目目标是爬取一个简单的网页（例如：豆瓣电影top250)并提取电影的标题和评分。
1.安装requests和beautifulsoup库。
'''
# 2. 编写爬虫代码
import requests
from bs4 import BeautifulSoup
from lxml.html.diff import DEL_END

#目标URL(豆瓣电影top250)
url = 'https://movie.douban.com/top250'
# 发送http get请求
response = requests.get(url)
# 检查请求是否成功
if response.status_code == 200:
    #解析html内容
    soup = BeautifulSoup(response.text, 'html.parser')

    #查找所有电影条目
    movie_list = soup.find_all('div', class_='item')

    #遍历每个电影条目
    for movie in movie_list:
        # 提取电影标题
        title = movie.find('span', class_='title').text

        # 提取电影评分
        rating = movie.find('span', class_='rating_num').text

        # 打印电影标题和评分
        print(f'电影标题：{title}, 评分:{rating}')
else:
    print(f'请求失败，状态码:{response.status_code}')
'''
3. 代码解释
requests.get(url): 发送一个HTTP GET请求到指定的URL，并返回服务器的响应。
BeautifulSoup(response.text, 'html.parser'): 使用BeautifulSoup解析HTML内容，html.parser是Python内置的HTML解析器。
soup.find_all('div', class_='item'): 查找所有class为item的div元素，这些元素包含了电影的详细信息。
movie.find('span', class_='title').text: 在每个电影条目中查找class为title的span元素，并提取其文本内容（即电影标题）。
movie.find('span', class_='rating_num').text: 在每个电影条目中查找class为rating_num的span元素，并提取其文本内容（即电影评分）。
'''
# 4. 运行代码。 将上述代码保存为一个python文件（例如：douban_top250.py)。然后在终端或命令行中运行：
#python douban_top250py.
# 5.输出结果，运行代码后，竟看到类似以下的输出：
'''电影标题: 肖申克的救赎, 评分: 9.7
电影标题: 霸王别姬, 评分: 9.6
电影标题: 阿甘正传, 评分: 9.5
...'''
'''
6. 进一步学习
分页爬取: 你可以修改代码以爬取多页内容，豆瓣电影Top250有10页，每页25部电影。
数据存储: 你可以将爬取的数据存储到CSV文件或数据库中。
反爬虫策略: 学习如何处理网站的反爬虫机制，例如设置请求头、使用代理等。'''

import requests
from bs4 import BeautifulSoup
import csv

# 目标URL（豆瓣电影Top250）
url = 'https://movie.douban.com/top250'

# 设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 发送HTTP GET请求
response = requests.get(url, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有电影条目
    movie_list = soup.find_all('div', class_='item')

    # 打开一个CSV文件，用于保存数据
    with open('douban_top250.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 写入表头
        writer.writerow(['电影标题', '评分'])

        # 遍历每个电影条目
        for movie in movie_list:
            # 提取电影标题
            title = movie.find('span', class_='title').text

            # 提取电影评分
            rating = movie.find('span', class_='rating_num').text

            # 将数据写入CSV文件
            writer.writerow([title, rating])

            # 打印电影标题和评分（可选）
            print(f'电影标题: {title}, 评分: {rating}')
else:
    print(f'请求失败，状态码: {response.status_code}')  # 输出： 请求失败，状态码:418

'''________________________________________________________________________________________________
项目2
以下是一个完整的简单爬虫项目代码，适合新手学习。我们将使用 requests 库发送 HTTP 请求，并使用 BeautifulSoup 解析网页内容。
这个项目的目标是爬取豆瓣电影 Top250 的电影名称和评分，并将结果保存到一个 CSV 文件中。
'''
import requests
from bs4 import BeautifulSoup
import csv

# 目标URL（豆瓣电影Top250）
url = 'https://movie.douban.com/top250'
#设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
# 发送HTTP Get请求
response = requests.get(url,headers=headers)
# 检查请求是否成功
if response.status_code == 200:
    # 解析HTML内容
    soup = BeautifulSoup(response.text,'html.parser')
    #查找所有电影条目
    movie_list = soup.find_all('div',class_='item')
    # 打开一个csv文件，用于保存数据
    with open('douban_top250.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 写入表头
        writer.writerow(['电影标题','评分'])
        # 遍历每个电影条目
        for movie in movie_list:
            # 提取电影标题
            title = movie.find('span',class_='title').text
            # 提取电影评分
            rating = movie.find('span',class_='rating_num').text
            # 将数据写入csv文件
            writer.writerow([title,rating])
            # 打印电影标题和评分（可选）
            print(f'电影标题：{title},评分：{rating}')
else:
    print(f'请求失败，状态码：{response.status_code}')

'''
代码说明
requests.get(url, headers=headers):
发送 HTTP GET 请求到目标 URL。
添加 headers 模拟浏览器访问，避免被网站反爬虫机制拦截。
BeautifulSoup(response.text, 'html.parser'):
使用 BeautifulSoup 解析 HTML 内容。
soup.find_all('div', class_='item'):
查找所有 class 为 item 的 div 元素，这些元素包含电影的详细信息。
movie.find('span', class_='title').text:
提取电影标题。
movie.find('span', class_='rating_num').text:
提取电影评分。
csv.writer:
将数据写入 CSV 文件，方便后续分析或存储。
print:
在控制台打印电影标题和评分（可选）。
'''
# 运行代码
# 1. 将代码保存为douban_top250.py
# 2. 在终端运行。python douban_top250.py
# 3. 运行后会在当前目录生成一个douban_top250.csv文件，包含电影标题和评分。
# 输出示例
'''
电影标题: 肖申克的救赎, 评分: 9.7
电影标题: 霸王别姬, 评分: 9.6
电影标题: 泰坦尼克号, 评分: 9.5
电影标题: 阿甘正传, 评分: 9.5
.........................'''
'''
CSV 文件内容：
电影标题	评分
肖申克的救赎	9.7
霸王别姬	9.6
阿甘正传	9.5
...	...
'''
# 进一步扩展
# 1. 分页爬取：豆瓣top 250有10页，每页25部电影。可以通过循环遍历页码爬取所有数据。
'''
https://movie.douban.com/top250?start=0 # 第1页
https://movie.douban.com/top250?start=24 # 第2页
https://movie.douban.com/top250?start=50 # 第3页'''
# 2. 异常处理：添加try-except块，处理请求失败或解析错误的情况
# 3. 数据存储：将数据存储到数据库（如SQLite、MySQL)中。
# 4. 反爬虫策略：使用随机user-agent和代理IP,避免被网站封禁。
'''________________________________________________________________________________________________________________
项目3.爬取某个网页（例如豆瓣电影评论页）的评论区评论。 
使用requests库发送HTTP请求，使用beautifulsoup解析网页内容。
这个项目的目标是爬取评论区中的用户评论，并将结果保存到一个csv文件中。
'''
import requests
from bs4 import BeautifulSoup
import csv
# 目标URL(以豆瓣电影《肖申克的救赎》评论页为例）
url = 'https://movie.douban.com/subject/1292052/comments?status=P'
# 设置请求头，模拟浏览器访问
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
# 发送HTTP GET请求
response = requests.get(url, headers=headers)
# 检查请求是否成功
if response.status_code == 200:
    # 解析html内容
    soup = BeautifulSoup(response.text,'html.parser')
    # 查找所有评论条目
    comment_list = soup.find_all('div',class_='comment-item')
    # 打开一个csv文件，用于保存数据
    with open('douban_comments.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 写入表头
        writer.writerow(['用户名','评论内容','评分'])
        # 遍历每个评论条目
        for comment in comment_list:
            # 提取用户名
            username = comment.find('span',class_='comment-info').find('a').text
            # 提取评论内容
            content = comment.find('span',class_='short').text
            # 提取评分(如果有）
            rating_tag = comment.find('span',class_='rating')
            rating = rating_tag['title'] if rating_tag else '无评分'
            # 将数据写入csv文件
            writer.writerow([username,content,rating])
            # 打印评论信息（可选）
            print(f'用户名：{username},评论内容:{content},评分：{rating}')
else:
    print(f'请求失败，状态码：{response.status_code}')
'''
代码说明
1. requests.get(url,headers=headers):
发送http get 请求到目标url
添加headers模拟浏览器访问，避免被网站反爬虫机制拦截
2.beautifulsoup(response.text,'html.parser):
使用beautifulsoup解析html内容
3.soup.find_all('div', class='comment-item):
查找所有class胃comment-item的div元素，这些元素包含评论的详细信息。
4.comment.find('span',class='comment-info').find('a').text:
提取评论区用户的用户名
5.comment.find('span',class_='short').text:
提取评论区内容
6.comment.find('span',class_='rating')
提取用户评分（如果有），否则返回‘无评分’
7.csv.writer
将数据写入csv文件，方便后续分析或存储。
8.print:
在控制台打印评论信息（可选）
'''
# 运行代码
# 1. 将代码保存为douban_comments.py
# 2. 在终端运行： python douban_comments.py
# 3. 运行后，会在当前目录生成一个douban_comments.csv文件，包含用户名，评论内容和评分
# 输出示例
'''用户名：犀牛,评论内容:当年的奥斯卡颁奖礼上，被如日中天的《阿甘正传》掩盖了它的光彩，而随着时间的推移，这部电影在越来越多的人们心中的地位已超越了《阿甘》。每当现实令我疲惫得产生无力感，翻出这张碟，就重获力量。毫无疑问，本片位列男人必看的电影前三名！回顾那一段经典台词：“有的人的羽翼是如此光辉，即使世界上最黑暗的牢狱，也无法长久地将他围困！”,评分：力荐
用户名：如小果,评论内容:恐惧让你沦为囚犯，希望让你重获自由。——《肖申克的救赎》,评分：力荐
用户名：Eve|Classified,评论内容:“这是一部男人必看的电影。”人人都这么说。但单纯从性别区分，就会让这电影变狭隘。《肖申克的救赎》突破了男人电影的局限，通篇几乎充满令人难以置信的温馨基调，而电影里最伟大的主题是“希望”。
当我们无奈地遇到了如同肖申克一般囚禁了心灵自由的那种囹圄，我们是无奈的老布鲁克，灰心的瑞德，还是智慧的安迪？运用智慧，信任希望，并且勇敢面对恐惧心理，去打败它？
经典的电影之所以经典，因为他们都在做同一件事——让你从不同的角度来欣赏希望的美好。,评分：力荐'''
# 进一步扩展。 1.分页爬取。评论区通常有很多页，可以通过循环遍历页码爬取所有评论。 https://movie.douban.com/subject/1292052/comments?start=0&limit=20&status=P&sort=new_score  # 第1页
# https://movie.douban.com/subject/1292052/comments?start=20&limit=20&status=P&sort=new_score # 第2页
# 2. 异常处理，添加try-except块，处理请求失败或解析错误的情况。  3.数据存储。将数据存储到数据库（sqlite,mysql) 4. 反爬虫策略，使用随机user-agent和代理ip，避免网站呗封禁
'''项目3 。爬取quotes to scrape
3. 项目3 。爬取quotes to scrape。（一个专门用于训练爬虫的网站）的名人名言和作者信息。这个项目包含
1.爬取多页数据（分页爬取）
2.数据清洗和存储（保存为csv和json)
3.异常处理和日志记录
4.随机user=agent和延迟请求（避免被封禁）
''' # 完整代码
import requests
from bs4 import BeautifulSoup
import csv
import json
import time
import random
from fake_useragent import UserAgent

# 配置
BASE_URL = 'https://quotes.toscrape.com'
OUTPUT_CSV = "quotes.csv"
OUTPUT_JSON = 'quotes.json'
DELAY = 1 # 每次请求延迟1秒（避免被封）
MAX_PAGES = 5 # 最多爬取5页（可调整）

# 随机User-Agent
ua = UserAgent()
def get_random_headers():
    return {
        'User-Agent': ua.random,
        'Accept-Language': 'en-US,en;q=0.9',
    }
def scrape_quotes():
    quotes_data = []
    page_num = 1

    while page_num <= MAX_PAGES:
        url = f"{BASE_URL}/page/{page_num}"
        print(f"正在爬取：{url}")

        try:
            # 发送请求（带随机User-Agent和延迟）
            response = requests.get(
                url,
                headers=get_random_headers(),
                timeout=10
            )
            response.raise_for_status() # 检查HTTP错误

            # 解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = soup.find_all('div',class_='quotes')
            if not quotes:
                print(f"第{page_num}页没有数据，终止爬取")
                break
            # 提取数据
            for quote in quotes:
                text = quote.find('span', class_='text').text.strip()
                author = quote.find('small',class_='author').text.strip()
                tags = [tag.text for tag in quote.find_all('a', class_='tag')]
                quotes_data.append({
                    'text':text,
                    'author':author,
                    'tags':tags,
                })
            print(f"第{page_num}页爬取完成，共{len(quotes)}条名言")
            page_num += 1
            time.sleep(DELAY + random.uniform(0,1)) # 随机延迟
        except requests.RequestException as e:
            print(f"请求失败：{e}")
            break
        except Exception as e:
            print(f"解析错误:{e}")
            break
    return quotes_data
def save_to_csv(data):
    with open(OUTPUT_CSV,'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['名言','作者','标签'])
        for item in data:
            writer.writerow([
                item['text'],
                item['author'],
                ', '.join(item['tags'])
            ])
    print(f"数据已保存到{OUTPUT_CSV}")

def save_to_json(data):
    with open(OUTPUT_JSON,'w', encoding='utf-8') as file:
        json.dump(data,file,ensure_ascii=False,indent=2)
    print(f"数据已保存到{OUTPUT_JSON}")

if __name__=="__main__":
    print("开始爬取 Quotes to Scrape...")
    quotes = scrape_quotes()

    if quotes:
        save_to_csv(quotes)
        save_to_json(quotes)
        print("爬取完成！共获取{len{quotes)}条名言。")
    else:
        print("没有爬取到数据。")
'''
代码功能说明
1.爬取目标：网站：http://quotes.toscrape.com（专门用于练习爬虫）
数据：名言（text）、作者（author）、标签（tags）
2.核心功能：分页爬取：自动爬取多页数据（可设置MAX_PAGES)
随机user-agent:使用fake_useragent库模拟不同浏览器
延迟请求：避免频繁请求被封禁（delay可调整）
数据存储：支持csv和json两种格式
异常处理：捕获网络请求和解析错误
3. 输出示例：
csv文件（quotes.csv)
名言,作者,标签
"The world as we have created it is a process of our thinking. 
It cannot be changed without changing our thinking.",Albert Einstein,"change,deep-thoughts,thinking,world"
json 文件 (qutoes.json):
[{
    "text":"The world we have created it is a process of our thinking...",
    "author": "Albert Einstein",
    "tags":["change", "deep-thoughts", "thinking", "world"]
}
]
'''
# 如何运行？ 1.安装依赖库。 pip install requests beautifulsoup4 fake-useragent . 2.运行脚本 python scrape_quotes.py
# 3. 查看结果：生成的quotes.csv和quotes.json文件会自动保存在当前目录
'''扩展建议
爬取更多数据：
修改 MAX_PAGES 爬取更多页。
爬取作者详情页（例如 http://quotes.toscrape.com/author/Albert-Einstein）。
反反爬策略：
使用代理 IP（如 requests.get(..., proxies={'http': 'your_proxy'})）。
增加随机延迟（如 time.sleep(random.uniform(1, 3))）。
数据库存储：
改用 SQLite 或 MySQL 存储数据（适合大规模数据）。
'''
'''项目4 github模拟电影天堂
以下是一个从GitHub上找到的简单爬虫项目（模拟「电影天堂」电影下载链接爬取）的完整代码示例，包含详细注释和扩展建议。
我会带你逐步分析代码结构，并教你如何模仿实现类似功能。
'''
print("项目4 github模拟电影天堂")





