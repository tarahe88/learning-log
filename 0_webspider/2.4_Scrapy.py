# scrapy是强大的python爬虫框架，专为高效抓取和提取网页数据而设计。 有完整的爬虫开发工具链，适合大中型爬虫项目。以下是学习的核心知识和技巧
# 1. Scrapy 的优势
        # 高效：基于异步框架twisted,性能优异
        # 模块化：机构清晰，易于扩展
        # 功能丰富：内置数据提取，存储，中间件，管道等功能。
        # 社区支持： 文档完善，社区活跃。
# 2. Scrapy 的安装
# 2.1 安装 Scrapy pip install scrapy
# 2.2 验证安装 scrapy version
# 3. Scrapy 的核心组件。 核心组件包括
# Spider: 定义爬取逻辑
# Item: 定义数据结构
# Pipeline: 处理爬取的数据（如清晰，存储）
# Downloader Middleware：处理请求和响应
# Spider Middleware: 处理Spider的输入和输出。
# Scheduler：管理请求队列。
# 4. Scrapy 的基本使用
# 4.1 创建项目
'''
scrapy startproject myproject
项目结构如下：
myproject/
    scrapy.cfg
        myproject/
            __init__.py
            items.py
            middlewares.py
            pipeline.py
            settings.py
            spiders/
                __init__.py
'''
# 4.2 创建Spider。 spider是scrapy的核心，用于定义爬取逻辑。 示例：创建一个简单的spider
import scrapy
from scrapy.settings.default_settings import ITEM_PIPELINES, DOWNLOADER_MIDDLEWARES, CONCURRENT_REQUESTS, \
    COOKIES_ENABLED, LOG_LEVEL, SCHEDULER, DUPEFILTER_CLASS


class MySpider(scrapy.Spider):
    name = "myspider" # spider的名称。
    start_urls = [
        "https://www.example.com",
    ]
    def parse(self, response):
        # 提取数据
        title = response.xpath("//title.text(").get()
        yield{"title": title}
# 4.3 运行 Spider
scrapy crawl myspider
# 5 scrapy的核心功能
# 5.1 数据提取。 scrapy支持xpath 和 css选择器提取数据。
# 使用xpath
title = response.xpath("//title/text()").get()
# 使用css选择器
title = response.css("title::text").get()

# 5.2 定义 Item. item用于定义爬取数据的结构。
# 在items.py中定义item
import scrapy
class MyItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
# 在spider中使用item
from myproject.items import MyItem
def parse(self, response):
    item = MyItem()
    item["title"] = response.xpath("//title/text()").get()
    item["url"] = response.url
    yield item
# 5.3 数据存储. 通过pipeline将数据存储到文件或数据库中。
# 在pipelines.py中定义pipeline
import json
class MyPipeline:
    def open_spider(self,spider):
        self.file = open("output.json","w")
    def close_spider(self,spider):
        self.file.close()
    def process_item(self,item,spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
# 在 settings.py 中启用 Pipeline
ITEM_PIPELINES = {
    "myproject.pipelines.MyPipeline": 300,
}
# 5.4 处理分页. 通过递归请求处理分页。示例：分页爬取
def parse(self,response):
    #提取当前页数据
    for item in response.xpath("//div[@class='item']"):
        yield{"title":item.xpath(".//h2/text()").get()}
    #提取下一页链接
    next_page = response.xpath("//a[@class='next-page']/@href").get()
    if next_page:
        yield response.follow(next_page, self.parse)
# 5.5 处理动态内容 Scrapy 本身不支持 JavaScript 渲染，但可以通过以下方式处理动态内容：
# 使用 Splash（基于 Lua 的渲染服务）。
# 结合 Selenium（性能较低，适合小规模爬取）。
# 6. Scrapy 的进阶功能
# 6.1 中间件. 中间件可以修改请求和响应。
# 示例：自定义 User-Agent
class MyMiddleware:
    def process_request(self,request,spider):
        request.headers["User-Agent"] = "My Custom User-Agent"
# 在settings.py中启用中间件
DOWNLOADER_MIDDLEWARES = {
    "myproject.middlewares.MyMiddleware": 543,
}
# 6.2 配置设置 . 在 settings.py 中配置爬虫行为。常用配置：
# 并发请求数
CONCURRENT_REQUESTS = 16
# 下载延迟
DOWNLOAD_DELAY= 1
# 启用Cookies
COOKIES_ENABLED = True
# 日志级别
LOG_LEVEL = "INFO"

# 6.3 分布式爬虫 #使用 Scrapy-Redis 实现分布式爬虫。
# 安装 Scrapy-Redis pip install scrapy-redis
#配置 Scrapy-Redis
# 使用 redis作为调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 使用redis去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# redis 连接设置
REDIS_URL = "redis://localhost:6379"

# 7. Scrapy 学习建议
# 掌握基础：先熟悉 Scrapy 的核心组件和基本用法。
# 多练习：通过实际项目练习 Scrapy 的使用。
# 阅读文档：Scrapy 官方文档非常详细，是学习的最佳资源。

# 8. 示例：完整 Scrapy 项目 以下是一个完整的 Scrapy 项目示例，爬取书籍信息并存储到 JSON 文件。
'''
项目结构
myproject/
    scrapy.cfg
    myproject/
        __init__.py
        items.py
        pipelines.py
        settings.py
        spiders/
            __init__.py
            books.py
'''
# items.py
import scrapy
class BookItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
# pipelines.py
import json
class BookPipeline:
    def open_spider(self,spider):
        self.file = open("books.json", "w")
    def close_spider(self,spider):
        self.file.close()
    def process_item(self,item,spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
# settings.py
ITEM_PIPELINES = {
    "myproject.pipelines.BookPipeline": 300,
}
#spiders/books.py
import scrapy
from myproject.items import BookItem
class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        "https://books.toscrape.com",
    ]
    def parse(self, response):
        for book in response.css("article.product_pod"):
            item = BookItem()
            item["title"] = book.css("h3 a::attr(title)").get()
            item["price"] = book.css("p.price_color::text").get()
            yield item
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
# 运行爬虫
scrapy crawl books







