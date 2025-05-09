#urllib   提供parse模块，处理URL标准接口。返回6个结果
from urllib.parse import urlparse
result = urlparse("https://www.baidu.com/index.html;user?id=#5comment")
print(type(result))
print(result)#scheme协议，netloc域名，path路径，params参数，query查询条件，fragment锚点
#标准的链接格式： schemes://netloc/path;params?query#fragment

#urlunparse  构造URL
from urllib.parse import urlunparse
data = ["https", "www.baidu.com", "index.html", "user", "a=6", "comment"] #这里除了用列表累心更，还可以用其他类型，元组或特定的数据结构
print(urlunparse(data))

#urlsplit  返回5个结果。不再单独解析params，params会合并到path中
from urllib.parse import urlsplit
result = urlsplit("https://www.baidu.com/index.html;user?id=#5comment") #没有参数params
print(result) #path='/index.html;user'

#urlunsplit  将各个部分组合成完整链接。
from urllib.parse import urlunsplit
data = ["https", 'www.baidu.com', "index.html;user", "a=6", "comment"]
print(urlunsplit(data))

#urljoin 轻松完成链接的解析，拼合，生成。比urlunparse和urlunsplit方便.
#提供一个基础链接作为第一个参数，新链接为第二个参数，分析基础链接里的scheme,netloc,path
#新链接里的协议，域名，路径优先于基础链接。如果没用，直接调用基础链接里的来补充新链接。
from urllib.parse import urljoin
print(urljoin("https://www.baidu.com","FAQ.html")) #协议，域名，路径 https://www.baidu.com/FAQ.html
print(urljoin("https://www.baidu.com","https://cuiqingcai.com/FAQ.html")) #https://cuiqingcai.com/FAQ.html
print(urljoin("https://www.baidu.com/about.html","https://cuiqingcai.com/FAQ.html")) #都有路径
print(urljoin("https://www.baidu.com/about.html","https://cuiqingcai.com/FAQ.html?question=2")) #https://cuiqingcai.com/FAQ.html？question=2
print(urljoin("www.baidu.com","?category=2")) #www.baidu.com?category=2

#urllencode  用字典将参数表示出来，然后用urlencode将字典转化为URL参数
from urllib.parse import urlencode
params = {
    "name": "pony",
    "age": 30
}
base_url = "https://www.baidu.com?"
url = base_url +urlencode(params)
print(url) #https://www.baidu.com?name=pony&age=30

#parse_qs     与urlencode相反，将url get请求参数转回为字典
from urllib.parse import parse_qs
query = "name=pony&age=30"
print(parse_qs(query)) #{'name': ['pony'], 'age': ['30']} 将url参数成功转为字典

#parse_qsl  #将url参数转化为由远足组成的列表
from urllib.parse import parse_qsl
query = "name=pony&age=30"
print(parse_qsl(query)) #[('name', 'pony'), ('age', '30')] 参数名，参数值

#quote 将参数转变为URL编码的格式。比如中文容易乱码，要转为URL格式
from urllib.parse import quote
keyword = "壁纸"
url = "https://www.baidu.com" +quote(keyword)
print(url) #https://www.baidu.com%E5%A3%81%E7%BA%B8

#unquote 将url进行解码
from urllib.parse import unquote
url = "https://www.baidu.com%E5%A3%81%E7%BA%B8"
print(unquote(url)) #https://www.baidu.com壁纸
