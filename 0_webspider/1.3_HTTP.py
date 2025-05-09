'''
HTTP 协议是爬虫的基础，理解请求方法、状态码、请求头和响应头是关键。
通过分析 HTTP 请求和响应，可以更好地编写爬虫程序。
'''
import requests
#设置请求头
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
#发送GET请求
response = requests.get("https://www.example.com", headers = headers)
#打印状态码
print(response.status_code)
#打印响应头
print(response.headers)
#打印响应体
print(response.text)
