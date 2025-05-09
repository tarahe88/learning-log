#简单版：https://blog.csdn.net/qq_59931372/article/details/128869887
#CSDN解析:https://blog.csdn.net/xiaosutongxue/article/details/126630841
import json
from os import makedirs
from os.path import exists
import requests #爬取页面
import logging #输出信息
import re #解析
from urllib.parse import urljoin #做URL拼接
import multiprocessing
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s-%(levelname)s:%(message)s') # 设置日志输出模式. #一定要加这个，不然什么都显示不出来
#2025-01-20 15:29:03,408-INFO:data saved successfully
# 1. 爬取页面，获得html文件
BASE_URL = "https://ssr1.scrape.center" #BASE_URL是变量，在f'{}花括号里
TOTAL_PAGE = 10
RESULTS_DIR = '../../results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)
#定义一个通用爬取页面。因为不仅要爬取列表页，还要爬取详情页。
def scrape_page(url): #定义一个通用爬取页面方法，接收参数url，返回页面的html代码
    logging.info('scraping %s...', url) #2025-01-20 15:29:57,949-INFO:scraping https://ssr1.scrape.center/detail/100...
    try:
        response = requests.get(url) #返回页面html 代码 ## 对目标URL进行访问
        if response.status_code == 200: ## 对状态码进行判断，如果返回状态码200说明连接正常
            return response.text #这个漏掉了所以运行不出来
        logging.error('get invalid status code %s while scraping %s',
                      response.staus_code, url)
    except requests.RequestException:  # 对错误的堆栈信息进行追踪
        logging.error('error occurred while scraping %s', url,
                      exc_info=True)
    # print(response.text)
#定义列表页爬取方法
def scrape_index(page): #在scrape_page基础上，定义列表页的爬取方法 #接收一个页码参数
    index_url = f'{BASE_URL}/page/{page}' #'f'格式化字符串参数使得变量可以填充字符串。花括号里是变量，不在括号里的是字符串
    #f'格式化字符串中用{}包裹变量 #https://ssr1.scrape.center/page/1 网址和后面的数字1是变量
    return scrape_page(index_url) #调用scrape_page方法，得到列表页html代码
# scrape_index(10) #输入页数，返回html文件。想要结果显示就是直接调用方法，方法里面输入参数。
# 2. 解析列表页，并得到每部电影的详情页的URL。参数：网页前端代码，返回值类型：string
# <a data-v-7f856186="" href="/detail/1" class="name">
def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">') #用re构造出每部电影对应href的匹配模式
    items = re.findall(pattern, html) #在前端代码中查找与pattern相匹配的代码
    # print(items)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL,item) #每部电影URL=基本URL+ items #https://ssr1.scrape.center//detail/1
        # print(detail_url) #https://ssr1.scrape.center/detail/1-100
        yield detail_url ## 关键字yield的机制是，暂停当前运行进程、输出当前结果并保存状态
    # 此函数作用同scrape_page()完全相同
# 构造此函数的目的：为日后进行爬取拓展提供接口
def scrape_detail(url): ## 此函数作用同scrape_page()完全相同
    return scrape_page(url)

# 功能：定位目标资源的前端代码，而后返回相应的数据
# 参数：对应每部电影的前端代码
# 返回值类型：dictionary
#https://ssr1.scrape.center/detail/1 霸王别姬详情页面
def parse_detail(html):
    # 分别对电影的封面、名称、分类、发行时间、评分、概要设置相应的re匹配规则
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S) #提取图片.多行跨行re.S
    """<div data-v-63864230="" class="el-col el-col-24 el-col-xs-0 el-col-sm-8">
          <a data-v-63864230="" class="router-link-exact-active router-link-active">
            <img data-v-63864230="" src="https://p0.meituan.net/movie/ce4da3e03e655b5b88ed31b5cd7896cf62472.jpg@464w_644h_1e_1c" class="cover">
          </a>
        </div>"""
    name_pattern = re.compile('<h2.*?>(.*?)</h2') #要提取的东西是括号里的(.*?)
    #<h2 data-v-63864230="" class="m-b-sm">霸王别姬 - Farewell My Concubine</h2>
    categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>', re.S)
    """<button data-v-7f856186="" type="button" class="el-button category el-button--primary el-button--mini">
                  <span>剧情</span>
                </button>"""
    published_at_pattern =re.compile('r(\\d{4}-\\d{2}-\\d{2})\\s上映') #标准时间正则：(\d{4}-\d{2}-\d{2})
    """<div data-v-7f856186="" class="m-v-sm info">
                <span data-v-7f856186="">1993-07-26 上映</span>
              </div>"""
    score_pattern = re.compile('<p.*?score.*?>(.*?)</p>', re.S)
    """<p data-v-63864230="" class="score m-t-md m-b-n-sm">
              9.5</p> """
    drama_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>(.*?)</p>', re.S)
    """
    <div data-v-63864230="" class="drama"><h3 data-v-63864230="">剧情简介</h3>
                <p data-v-63864230="">
                  影片借一出《霸王别姬》的京戏，牵扯出三个人之间一段随时代风云变幻的爱恨情仇。段小楼（张丰毅 饰）与程蝶衣（张国荣 饰）是一对打小一起长大的师兄弟，两人一个演生，一个饰旦，一向配合天衣无缝，尤其一出《霸王别姬》，更是誉满京城，为此，两人约定合演一辈子《霸王别姬》。但两人对戏剧与人生关系的理解有本质不同，段小楼深知戏非人生，程蝶衣则是人戏不分。段小楼在认为该成家立业之时迎娶了名妓菊仙（巩俐 饰），致使程蝶衣认定菊仙是可耻的第三者，使段小楼做了叛徒，自此，三人围绕一出《霸王别姬》生出的爱恨情仇战开始随着时代风云的变迁不断升级，终酿成悲剧。
                </p></div>"""
    cover = re.search(cover_pattern, html).group(1).strip() if re.search(cover_pattern,html) else None # 查什么,在哪查.返回第一个括号的内容.删掉开头和末尾的空格
    name = re.search(name_pattern,html).group(1).strip()  if re.search(name_pattern,html) else None
    categories = re.findall(categories_pattern,html) if re.findall(
        categories_pattern,html) else [] #因为分类有2处，所以是findall.
    published_at = re.search(published_at_pattern,html).group(1) if re.search(published_at_pattern,html) else None
    score = float(re.search(score_pattern,html).group(1).strip()) if re.search(score_pattern,html) else None #float 浮点数，带小数点
    drama = re.search(drama_pattern,html).group(1).strip() if re.search(drama_pattern, html) else None
    # 将所获取的数据以字典的形式进行返回
    return {
        'cover': cover,
        'name': name,
        "categories": categories,
        "published_at": published_at,
        "drama": drama,
        "score": score
    }
#功能：将获取到的数据以.json形式存储
#参数：数据
#返回值类型：None
RESULTS_DIR = '../../results'  #定义保存数据的文件夹 RESULTS_DIR
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)
def save_data(data): #定义保存数据的方法
    name = data.get('name')  # 获取电影名称
    data_path = f'{RESULTS_DIR}/{name}.json'  # 根据电影名称，规定相应电影的文件名。
    json.dump(data, open(data_path, 'w', encoding='utf-8'),
                            ensure_ascii=False, indent=2)  # 将数据写入文件/ensure_ascii保证中文字符正常显示，而不是unicode字符，缩紧2个字

# 功能：爬取并保存电影信息
# 参数：网站当前页数
# 返回值类型：None



# 参数：网站当前页数
# 返回值类型：None
def main(page):
    index_html = scrape_index(page)  # 获取当前页面下的前端代码
    detail_urls = parse_index(index_html)  # 获取当前页面下所有电影的URL
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)  # 获取每部电影页面的前端代码
        data = parse_detail(detail_html)  # 获取每部电影的信息
        logging.info('get detail data %s', data) #2025...{'cover': 'https://p1.meituan.net/... 'name': '大闹天宫 - The Monkey King', 'categories': ['动画', '奇幻'], 'published_at': None, 'drama': '话说在东土傲来国有一座花果山，山上有一尊石猴吸收日精月华化身为一只神猴（邱岳峰 配音），统领着山中的猴子猴孙。为求得一件称心的宝贝，神猴孙大圣潜入龙宫，强硬求来大禹治水时的定海神针如意金箍棒。东海龙王（毕克 配音）心有不甘，于是上天将此事诉诸玉帝（富润生 配音）。玉皇大帝命令太白金星（尚华 配音）下界招安，许以爵位。不知有诈的孙大圣欣然前往，却发现只是负责养马的弼马温。得知受骗的猴王反下天庭，与天兵天将在花果山展开大战……', 'score': 9.0}
        logging.info('save data to json data')
        save_data(data)  # 将获取到的信息进行存储
        logging.info('data saved successfully')

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)  # 构造进程池，并将进程数设为4。
    pages = range(1, TOTAL_PAGE + 1)  # 构造页面数
    pool.map(main, pages)  # 将pages作为参数传入到main()当中，
    # 并将每一次main()函数调用作为一个进程，
    # 加入到进程池当中
    pool.close()  # 等待worker进程结束再关闭进程池
    pool.join()  # 防止主程序在worker进程结束前结束

