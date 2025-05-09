'''
面向对象编程（OOP，Object-Oriented Programming）是 Python 编程中的重要概念，它可以帮助你更好地组织代码、提高代码的可重用性和可维护性。对于爬虫开发来说，掌握 OOP 可以让你更高效地编写模块化和可扩展的爬虫程序。
以下是 Python 面向对象编程的核心概念及其在爬虫中的应用
'''
# 1. 类(class)与对象（object)
    # 类：类是对象的蓝图或模版，定义了对象的属性和方法。
    # 对象：对象是类的实例，具有定义类的属性和行为。
# 在爬虫中的应用：可以将爬虫定义为一个类，每个爬虫实例是一个独立的对象，具有自己的属性和行为。
# 例：定义一个spider类，每个爬虫实例可以负责抓取不同的网站。
class Spider
    def __init__(self,name,target_url):
        self.name = name
        self.target_url = target_url
    def crawl(self):
        print(f"{self.name} is crawling{self.target_url}")
# 创建对象
spider1 = Spider("Spider1","https://example.com")
spider2 = Spider("Spider2","https://anotherexample.com")
#调用方法
spider1.crawl()
spider2.crawl()
# 2. 构造函数(__init__方法）。构造函数在创建对象时自动调用，用于初始化对象的属性。
# 在爬虫中的应用：可以在构造函数中初始化爬虫的名称，目标URL，请求头等属性。
class Spider:
    def __init__(self,name,target_url):
        self.name = name
        self.target_url = target_url
        self.headers = {"User-Agent": "MySpider/1.0"}
# 3. 属性（Attributes). 属性是类或对象的变量，用于存储数据。
# 在爬虫中的应用。可以定义属性来存储爬虫的状态信息，例如已抓取的页面数量，请求间隔时间等。
class Spider:
    def __init__(self,name,target_url):
        self.name = name
        self.target_url = target_url
        self.crawled_pages = 0 # 记录已经被抓取的页面数量。
# 4. 方法(methods). 方法是类中定义的函数，用于执行操作。
# 在爬虫中的应用：可以定义方法来执行爬虫的核心功能，例如发送请求，解析页面，保存数据等。
import requests
class Spider:
    def __init__(self,name,target_url):
        self.name = name
        self.target_url = target_url
    def send_request(self):
        response = requests.get(self.target_url)
        return response.text
    def parse(self,html):
        print(f"{self.name} is parsing HTML content")
        # 解析 HTML 的逻辑
    def save_data(self,data):
        print(f"{self.name} is saving data")
        # 保存数据的逻辑
# 5. 继承（Inheritance). 继承允许一个类继承另一个类的属性和方法，便于代码复用。
# 在爬虫中的应用：可以定义一个基础的Spider类，然后通过继承创建特定类型的爬虫（例如ImageSpider,VideoSpider).
class Spider:
    def __init__(self,name,target_url):
        self.name = name
        self.target_url = target_url
    def crawl(self):
        print(f"{self.name} is crawling{self.target_url}")
class ImageSpider(Spider):
    def download_images(self):
        print(f"{self.name} is downloading images from {self.target_url}")
# 使用继承
image_spider = ImageSpider("ImageSpider", "https://example.com/images")
image_spider.crawl()
image_spider.download_images()
# 6. 封装（Encapsulation). 封装通过限制对某些属性或方法的直接访问，保护对象的内部状态。
# 在爬虫中的应用。 可以将敏感数据（例如API密钥）或核心逻辑封装起来，避免外部直接访问。
class Spider:
    def __init__(self,name,target_url, api_key):
        self.name = name
        self.target_url = target_url
        self.__api__key = api_key # 私有属性
    def get_api_key(self):
        return self.__api__key # 通过方法访问私有属性
# 7. 多态（polymorphism) # 多态允许不同类的对象对同一方法调用做出不同响应
# 在爬虫中的应用。可以定义不同类型的爬虫（比如Spider和APISpider)，它们都实现crawl方法，但具体行为不同。
class Spider:
    def crawl(self):
        print("Spider is crawling")
class APISpider:
    def crawl(self):
        print("APISpider is fetching data from API")
def start_crawling(crawler):
    crawler.crawl()
# 多态
start_crawling(Spider())
start_crawling(APISpider())
# 8. 类变量与实例变量
    # 类变量：属于类，所有对象共享
    # 实例变量：属于对象，每个对象有独立的实例变量
# 在爬虫中的应用：可以使用类变量记录所有爬虫实例的共享数据（例如总请求数），使用实例变量记录每个爬虫的独立数据（例如目标URL）
class Spider:
    total_requests = 0 # 类变量
    def __init__(self,name,target_url):
        self.name = name
        self.target_url = target_url
    def send_request(self):
        Spider.total_requests += 1
        print(f"{self.name} sent a request to {self.target_url}")
        print(f"Total requests:{Spider.total_requests}")
# 9. 特殊方法（Magic Methonds)
# 特殊方法（如__str__, __rep__)用于定义对象的行为。
# 在爬虫中的应用。可以使用__str__方法定义爬虫对象的字符串表示形式，便于调试和日志记录
class Spider:
    def __init__(self,name,target_url):
        self.name = name
        self.target_url = target_url
    def __str__(self):
        return f"Spider(name={self.name},target_url={self.target_url}"
spider = Spider("MySpider","https://example.com")
print(spider) # 输出： Spider(name=MySpider, target_url=https://example.com
# 10 模块与包. 模块是包含Python代码的文件，包是包含多个模块的目录。
# 在爬虫中的应用：可以将爬虫类放在单独的模块中，便于管理和复用。
# spiders/spider.py
class Spider:
    def __init__(self,name,target_url)
        self.name = name
        self.target_url = target_url
# main.py
from spiders.spider import Spider
spider = Spider("MySpider", "https://example.com")







