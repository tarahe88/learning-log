'''
在爬虫开发中，反爬虫策略是一个必须面对的挑战。网站为了防止被爬虫抓取数据，通常会采取多种反爬虫措施，
如 User-Agent 检测、IP 封禁、验证码 等。以下是新手高效学习反爬虫策略的核心知识和技巧。
'''
# 1. User-Agent伪装
# 1.1 什么是User-Agent? User-Agent是HTTP请求头的一部分，用于标识客户端（如浏览器，爬虫）的累心更合版本。
# 网络通过检测user=agent来判断请求是否来自爬虫。
# 1.2 如何伪装useragent.
# 随机切换user-agent:使用多个user-agent随机切换，模拟不同浏览器
# 使用第三方库，如fake-useragent，自动生成随机user-agent.
# 示例：随机切换user-agent
import requests
from fake_useragent import UserAgent
#创建useragent对象
ua = UserAgent()
#随机生成user_agent
headers = {
    "User-Agent": ua.random
}
# 发送请求
response = requests.get("https://www.example.com", headers=headers)
print(response.text)
# 2 IP 代理
# 2.1 什么是IP代理。 IP代理是通过第三方服务器装请求，隐藏真实IP地址，防止被网站封禁。
# 2.2 如何使用 IP 代理？
# 免费代理：从免费代理网站获取 IP，但稳定性较差。
# 付费代理：使用付费代理服务，如 Luminati、ProxyMesh 等。
# 自建代理池：通过爬取免费代理或购买代理 IP，构建自己的代理池
# 示例：使用IP代理
import requests
#设置代理
proxies = {
    "http": "http://123.45.67.89:8080",
    "https": "http://123.45.67.89:8080",
}
# 发送请求
response = requests.get("https://www.example.com", proxies=proxies)
print(response.text)
# 3.验证码识别
# 3.1什么是验证码？验证码是一种人机验证机制，用于区分人类用户和爬虫，常见的验证码类型包括：
#图片验证码：包含数字、字母或文字的图片。
#滑动验证码：通过滑动拼图完成验证。
#点选验证码：点击图片中的指定内容。
# 3.2 如何应对验证码？
#手动输入：对于少量请求，可以手动输入验证码。
#自动识别：使用 OCR 技术或第三方验证码识别服务。
#示例：使用 OCR 识别验证码
import requests
from PIL import Image
import pytesseract
#下载验证码图片
url = "https://www.example.com/captcha"
response = requests.get(url,stream=True)
with open("captcha,png","wb") as f:
    f.write(response.content)
# 使用OCR识别验证码
image = Image.open("captcha.png")
captcha_text = pytesseract.image_to_string(image)
print("验证码:",captcha_text)
# 使用第三方验证码识别服务
import requests
# 使用第三方验证码识别服务
def solve_captcha(image_path):
    with open(image_path,"rb") as f:
        response = requests.post(
            "https://api.captcha-solver.com/solve",
            files={"file":f},
            data={"api_key":"your_api_key"}
        )
        return response.json()["captcha_text"]
captcha_text = solve_captcha("captcha.png")
print("验证码：", captcha_text)
# 4. 其他反爬虫策略
# 4.1 请求频率控制
# 降低请求频率：通过设置延迟（如time.sleep())避免触发饭爬虫机制
# 随机化请求间隔：模拟人类浏览行为，随机化请求间隔。
# 示例： 随机化请求间隔。
import time
import random
for i in range(10):
    response = requests.get("https://www.example.com")
    print(response.status_code)
    time.sleep(random.uniform(1,3)) #随机等待 1-3秒
# 4.2 使用 Cookies
# 模拟登陆，通过登录获取cookies，用于后续请求
# 维护cookies, 使用requests.session 自动管理cookies
# 示例：使用cookies模拟登陆
import requests
#创建 session 对象
session = requests.session()
# 登录
login_data = {
    "username": "your_username",
    "password": "your_password"
}
session.post("https://www.example.com/login,data=login_data")
#使用登录后的cookies访问页面
response = session.get("https://www.example.com/protected")
print(response.text)
# 4.3 动态加载内容
# 使用selenium：处理通过javascript动态加载的内容
# 分析api请求：通过浏览器开发者工具分析动态加载的api请求，直接抓取数据。
# 示例： 使用selenium处理动态内容。
from selenium import webdriver
# 启动浏览器
driver = webdriver.Chrome()
driver.get("https://www.example.com")
# 等待动态内容加载
element = webdriver.Chrome()
print("动态内容:", element.text)
# 关闭浏览器
driver.quit()
    # 5. 综合应对策略. 实际爬虫开发中，通常需要结合多种反爬虫策略：
    # 1. 伪装user-agent: 随机切换user-agent
    # 2. 使用IP 代理：通过代理池隐藏真实ip
    # 3. 控制请求频率： 模拟人类浏览行为
    # 4. 处理验证码：使用ocr或第三方服务识别验证码
    # 5. 维护cookies: 模拟登陆并保持会话。
# 6. 学习建议
# 多实践：通过实际项目练习反爬虫策略。
# 分析目标网站：使用浏览器开发者工具分析目标网站的反爬虫机制。
# 阅读文档：学习相关库和工具的官方文档。
# 参与社区：加入爬虫开发者社区，学习他人的经验和技巧。
# 7. 示例：综合反爬虫策略
# 以下是一个综合使用反爬虫策略的示例：
import requests
from fake_useragent import UserAgent
import time
import random
#创建 useragent 对象
ua = UserAgent()
#代理池
proxies = [
    "http://123.45.67.89:8080",
    "http://98.76.54.32:8080",
    "http://11.22.33.44:8080",
]
# 模拟请求
for i in range(10):
    try:
        # 随机切换 User-Agent 和代理
        headers = {"User-Agent": ua.random}
        proxy = {"http": random.choice(proxies),"https": random.choice(proxies)}
    # 发送请求
    response = requests.get("https://www.example.com", headers=headers, proxies=proxy)
    print("状态码：", response.status_code)
    print("内容:", response.text[:100]) # 打印前 100个字符

    #随机等待 1-3 秒
    time.sleep(random.uniform(1,3))
except Exception as e:
print("请求失败：", e)











