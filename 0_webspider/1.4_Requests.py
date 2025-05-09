# Requests库，Python的第三方库，用于发送HTTP请求。
# 1 安装 requests pip install requests
# 2 发送HTTP请求
# Get 请求：获取资源，参数在URL中。
import requests
import requests.exceptions

response = requests.get("https://www.example.com")
print(response.text) #打开网页HTML内容
## Post请求：提交数据，参数在请求体中。
import requests
data = {"username": "admin", "password": "123456"}
response = requests.post("https://www.example.com/login", data=data)
print(response.text)
#其他请求方法：put, delete, head, options
# 3 设置请求头。模拟浏览器请求，避免被网站反爬。
import requests
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
response = requests.get("https://www.example.com", headers=headers)
print(response.text)
# 4 处理响应。
# 状态码：response.status_code
if response.status_code == 200:
    print("请求成功")
#响应头: response.headers
print(response.headers["Content-Type"])
#响应体：
# 文本： response.text
# 二进制：response.content
# JSON：response.json()
print(response.text) # 打印网页HTML内容

# 5 处理异常，捕获请求过程中可能出现的错误。
import requests
try:
    response = requests.get("https://www.example.com")
    response.raise_for_status() #抛出HTTP错误
except requests.exceptions.RequestException as e:
    print(e)

# 7  高级用法： session 保持会话，使用代理，SSL证书验证
# session：保持会话，自动处理cookie.
session = requests.Session()
session.get("https://www.example.com/login")  # 登录
response = session.get("https://www.example.com/profile") #访问其他页面
print(response.text)
#代理：使用代理服务器发送请求。
import requests
proxies = {"http": "http://127.0.0.1:8080", "https": "https://127.0.0.1:8080"}
response = requests.get("https://www.example.com/", proxies=proxies)
print(response.text)
#SSL证书验证：忽略SSL证书验证。
import requests
response = requests.get("https://www.example.com", verify=False)
print(response.text)

# 代码示例
import requests
#创建session对象
session = requests.Session()
#设置请求头
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
#发送登录请求
login_url = "https://www.example.com/login"
data = {"username":"admin", "password":"123456"}
session.post(login_url, data=data, headers=headers)

#登录成功后，访问其他页面
profile_url = "https://www.example.com/profile"
response = session.get(profile_url, headers=headers)
print(response.text)



















