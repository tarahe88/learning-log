from urllib.robotparser import RobotFileParser

rp = RobotFileParser() #首先建立一个robotfileparser对象rp
rp.set_url("https://www.baidu.com/robots.txt") #通过set_url设置robots.txt文件链接。
# 也可以rp = RobotFileParser(“https://www.baidu.com/robts.txt”)
rp.read()
print(rp.read())
print(rp.can_fetch("Baiduspider", "https://www.baidu.com")) #True #利用can_fetch判断网页是否能被抓取
print(rp.can_fetch("Baiduspider", "https://www.baidu.com/homepage/")) #True #利用can_fetch判断网页是否能被抓取
print(rp.can_fetch("Googlebot", "https://www.baidu.com/homepage/"))# False #利用can_fetch判断网页是否能被抓取



