#验证某些网站时，如 https://ssr3.scrape.center 可能会弹出这样的认证窗口。基本身份认证，允许提供用户名和口令
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler,build_opener
from urllib.error import URLError
username ="admin"
password = "admin"
url = "https://ssr3.scrape.center/"

p=HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode("utf-8")
    print(html)
except URLError as e:
    print(e.reason)