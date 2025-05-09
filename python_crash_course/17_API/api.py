# 17.1 使用 Web API
# web api 是网站的一部分，用于与使用非常具体的url请求特定信息的程序交互。这种请求为api调用。
# 请求的数据以易处理的格式(json或csv）返回。 依赖外部数据源的大多数应用程序都依赖api调用。入集成社交媒体网站的应用程序。
# 17.1.1 Git 和 GitHub
# 17.1.2 使用 API 调用请求数据
# github的api能够让你通过api调用来请求各种信息。
# https://api.github.com/search/repositories?q=language:python&sort=stars
# 响应的前几行代码："total_count": 19070355, 截止今天2025-04-09, 一共有1907万个python项目
# 响应的 "items": 列表显示包含github上最受欢迎的python项目的详细信息
# 17.1.3 安装requests

# 17.1.7  监视api的速率限制
# 大多数api都存在速率限制，即你在特定时间内可执行的请求数存在限制。 要获悉是否接近github限制，浏览器中输入
# https:api.github.com/rate_limit
# 看 search, 每分钟10个请求，在当前这一分钟内，还可以执行10个请求。
'''
{"resources":{"core":{"limit":60,"remaining":59,"reset":1744165224,"used":1,"resource":"core"},
"graphql":{"limit":0,"remaining":0,"reset":1744168632,"used":0,"resource":"graphql"},
"integration_manifest":{"limit":5000,"remaining":5000,"reset":1744168632,"used":0,"resource":"integration_manifest"},
"search":{"limit":10,"remaining":10,"reset":1744165092,"used":0,"resource":"search"}},"rate":{"limit":60,"remaining":59,"reset":1744165224,"used":1,"resource":"core"}}
'''

# 很多api都要求你注册获得api密钥后才能执行api调用。 便携式，github没有这样的要求，但获得api密钥后，配额将高很多。

# 17.3. Hacker News API.
# 探索使用其他网站的API调用看看 Hacker News（https://news.ycombinator.com/)
#下面的调用返回本书编写时最热门的文章的信息：
# https://hacker-news.firebaseio.com/v0/item/9884165.json
# 响应是一个字典，包含ID为9884165的文章的信息：
'''
{"by":"nns",
"descendants":297, # 文章被评论的次数 文章的后代。
"id":9884165,
"score":558,
"time":1436875181,
"title":"New Horizons: Nasa spacecraft speeds past Pluto",
"type":"story",
"url":"http://www.bbc.co.uk/news/science-environment-33524589",
"kids":[9885099,9884723,9885165,9884789,9885604,9884137,9886151,9885220,9885790,9884661,9885844,9885029,9884817,9887342,9884545,9884372,9884499,9884881,9884109,9886496,9884342,9887832,9885023,9884334,9884707,9887008,9885348,9885131,9887539,9885880,9884196,9884640,9886534,9885152],}
# kids是评论的ID。后代数量大于kids因为每个评论自己也可能有kid
'''
# 这个字典包含很多键，比如url和title。与decendants相关联的值时文章被评论的次数。与键kids相关联的事对文章所做的所有评论的ID

