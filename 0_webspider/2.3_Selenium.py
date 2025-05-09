# Selenium: 强大的web自动化测试工具，用于动态网页爬取。尤其是处理动态加载的网页（如通过 JavaScript 渲染的内容）
# 1. selenium作用：
# 1自动化浏览器操作:模拟用户操作点击，输入，滚动等 2处理动态内容:获取js动态加载的数据 3解决反爬虫机制:模拟真实用户行为，绕过简单反爬虫策略
# 2 2. Selenium 的安装与配置 pip install selenium 2.2 下载浏览器驱动
# 3. Selenium 的基本用法
# 3.1 启动浏览器
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.ie.webdriver import WebDriver

#启动chrome浏览器
driver = webdriver.Chrome() # 如果驱动不存在系统路径中，需要指定路径webdriver.Chrome('/path/to/chromed
#打开网页
driver.get("https://www.example.com")
#关闭浏览器
driver.quit()
# 3.2 定位元素
'''
方法 说明 示例
find_element(By.ID,"id")             通过ID定位         driver.find_element(By.ID, "username")
find_element(By.NAME,"name")         通过Name定位       driver.find_element(By.NAME, "password")
find_element(By.XPATH,"xpath")       通过XPath定位      driver.find_element(By.XPATH,"//div[@class='title']")
find_element(By.CLASS_NAME,"class")  通过Class定位。    driver.find_element(By.CLASS_NAME,"content")
find_element(By.TAG_NAME,"tag")      通过标签名定位。    driver.find_element(By.TAG_NAME,"h1")
find_element(By.CSS_SELECTOR,"css")  通过CSS选择器定位   driver.find_element(By.CSS_SELECTOR,".title")
'''
# 3.3 操作元素
    # 输入文本：send_keys()
    # 点击元素：click()
    # 获取文本：text
    # 获取属性：get_attribute()
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.example.com")

#输入文本
input_box = driver.find_element(By.NAME,"q")
input_box.send_keys("Selenium")

#点击按钮
button = driver.find_element(By.XPATH,"//button[@type='submit']")
button.click()
#获取文本
title = driver.find_element(By.TAG_NAME,"h1").text
print("标题：",title)
#获取属性
link = driver.find_element(By.XPATH,"//a").get_attribute("href")
print("链接：",link)
driver.quit()

# 3.4 等待页面加载。  动态网页需要等待元素加载完成后再操作，Selenium提供了两种等待方式
# 显式等待。 等待某个条件成立后再继续执行
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.example.com")
#等待标题出现，属于显式等待。
title = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME,"h1"))
)
print("标题：", title.text)
driver.quit()

#隐式等待。 设置一个全局的等待时间。
driver.implicitly_wait(10)  #等待最多10秒

#3.5 执行 JavaScript。 selenium通过execute_script()执行javascript代码
#滚动页面到底部
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#修改元素属性
driver.execute_script("document.getElementByID('id').style.display=‘block’;")

#4. Selenium 在爬虫中的应用
#4.1 处理动态加载内容。有些网页数据是通过javascript动态加载的，selenium可以获取这些数据
driver.get("https://www.example.com")
#等待动态内容加载
element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.CLASS_NAME,"dynamic-content")))
print("动态内容：",element.text)

# 4.2 模拟用户操作。   Selenium可以模拟用户点击，输入等操作。
# 点击分页按钮
next_button = driver.find_element(By.XPATH,"//a[@class='next-page']")
next_button.click()

#4.3 处理弹窗。 selenium可以处理浏览器的弹窗。
alert = driver.switch_to.alert
print("弹窗内容：", alert.text)
alert.accept() #点击确认

# 6. 示例：爬虫 + Selenium 以下是一个简单的爬虫示例，使用 Selenium 提取动态加载的新闻标题。
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 启动浏览器
driver = webdriver.Chrome()
driver.get("https://www.example.com/news")

#等待新闻标题加载
titles = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME,"news-title"))
)
# 提取标题
for title in titles:
    print(title.text)
# 关闭浏览器
driver.quit()





'''
5. Selenium 学习建议
掌握基础操作：先熟悉启动浏览器、定位元素、操作元素等基础操作。
练习动态网页：找一些动态加载数据的网页进行练习。
使用开发者工具：通过浏览器的开发者工具（F12）查看网页结构，辅助定位元素。
结合爬虫项目：在实际爬虫项目中应用 Selenium，提升实战能力。
'''
