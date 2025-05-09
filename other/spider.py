from bs4 import BeautifulSoup  #beautiful soup 4 网页解析，获取数据
import re #正则表达式进行文字匹配
import urllib.error #制定url,获取网页数据
import urllib.request #制定url,获取网页数据
import xlwt #进行excel操作
import sqlite3 #进行SQLite数据库操作
# urllib-给网页就能爬， bs4-爬完网页解析，re-解析后数据提炼， xlwt-数据存到excel, sqlite3-数据存到数据库


def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影top250.xls"
    #3.保存数据
    saveData(savepath)

#爬取网页。其实边爬取变解析
def getData(baseurl):
    datalist = []
    #2.逐一解析数据
    return datalist

#保存数据
def saveData(savepath):
    print("save....")


if __name__ == "__main__": #当程序执行时。保证程序的入口是在这。 程序入口。
    main() #调用函数