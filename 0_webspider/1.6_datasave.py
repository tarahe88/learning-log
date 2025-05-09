# 1 文件存储。 最简单的存储方式，适合小规模数据。常见文件格式包括文本文件(TXT,CSV,JSON,EXCEL)
# 1.1 文本文件(TXT) 适合简单的文本数据，使用python的内置函数open()进行读写。
# 写入数据
from lxml.includes.etreepublic import textOf

with open("data.txt","w",encoding="utf-8") as file:
    file.write("Hello, World!\n")
    file.write("这是第二行。")
# 读取数据
with open ("data.txt","r", encoding="utf-8") as file:
    content = file.read()
    print(content)
# 1.2 CSV文件。CSV(逗号分隔值）适合存储表格数据。使用python的csv模块进行读写。
import csv
# 写入数据
data = [["Name", "Age"]],["Alice", 25], ["Bob", 30]
with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)
#读取数据
with open("data.csv","r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
#1.3 JSON文件。 （Javascript object notation)适合存储结构化数据。使用python 的json模块进行读写。
import json
#写入数据
data = {"name": "Alice", "age":25}
with open("data.json","w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
#读取数据
with open("data.json","r",encoding="utf-8") as file:
    data = json.load(file)
    print(data)
# 1.4 Excel文件。适合存储复杂的表格数据，使用openpyxl或pandas库进行读写。
import pandas as pd
#写入数据
data = {"Name":["Alice","Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
df.to_excel("data.xlsx", index=False)
#读取数据
df = pd.read_excel("data.xlsx")
print(df)

# 2 数据库存储。数据库存书适合存储大规模，结构化数据。常见数据库包括MySql(关系型数据库）和MongoDB(非关系型数据库）
# 2.1 MySQL 是一种关系型数据库，适合存储结构化数据。使用pymysql或mysql-connector-python库操作MySQL.
#安装库
#pip install pymysql
#链接数据库并操作
import pymysql
#连接数据库
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="test_db"
)
#创建表
with connection.cursor() as cursor:
    sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT
    )
    """
    cursor.execute(sql)
    connection.commit()
#插入数据
with connection.cursor() as cursor:
    sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
    cursor.execute(sql,("Alice",25))
    connection.commmit()
#查询数据
with connection.cursor() as cursor:
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)
#关闭连接
connection.close()

#2.2 MongoDB. mongodb是一种非关系型数据库，适合存储半结构化或非结构化数据。 使用pymongo库操作mongodb
#安装库 pip install pymongo
#连接数据库并操作。
from pymongo import MongoClient
#链接数据库
client = MongoClient("mongodb://localhost:27017")
db = client["test_db"]
collection = db["users"]
#插入数据
data = {"name":"Alice", "age": 25}
collection.insert_one(data)
#查询数据
result = collection.find({"name": "Alice"})
for document in result:
    print(document)
#更新数据
collection.update_one({"name":"Alice"}, {"$set": {"age: 26"}})
#删除数据
collection.delete_one({"name":"ALice"})
#关闭连接
client.close()

# 5. 示例：爬虫 + 数据存储
#爬取数据并存储到 CSV
import requests
import csv
from bs4 import BeautifulSoup

url = "https://example.com" #目标网站
response = requests.get(url) #requests库获取
soup = BeautifulSoup(response.text, "html.parser") #beautifulsoup解析

data = []
for item in soup.find_all("div", class_="item"): #查找数据
    title = item.find("h2").text #提取信息
    description = item.find("h2").text() #提取信息
    data.append([title,description]) #将提取的数据添加到data列表中
# 存储到CSV
with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Description"])
    writer.writerows(data)
# 存储到MySQL
import pymysql
#连接数据库
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="test_db"
)
#插入数据
with connection.cursor() as cursor:
    sql = "INSERT INTO items (title, description) VALUES (%s, %s"
    for item in data:
        cursor.execute(sql, (item[0],item[1]))
    connection.commit()
# 关闭连接
connection.close()









c







































