# 16.1.1 fenxi csv文件头。 csv模块包含在python标准苦衷，可用于分析csv文件中的数据行，让我们能够快速提取感兴趣的值
import csv # 引入csv模块

filename = 'sitka_weather_07-2014.csv' # 网上下载的这个书本里的csv文件
with open(filename) as f:
    reader = csv.reader(f) # 调用csv.reader()将前面存储的文件对象作为实参传递给它，从而创建一个与该文件相关的阅读器(reader)对象
    header_row = next(reader) # 模块csv包含函数next()，调用对象并将阅读器对象传给它时，将返回文件中的下一行。
    # next只调用了一次，所以得到的是文件的第一行，包含文件头。
    print(header_row) # 将返回的数据存储在header_row中，header_row包含于天气相关的文件头，指出每行都包含哪些数据
    # #['AKDT', 'Max TemperatureF', 'Mean TemperatureF', 'Min TemperatureF', 'Max Dew PointF', 'MeanDew PointF', 'Min DewpointF', 'Max Humidity', ' Mean Humidit'''

# 16.1.2 打印文件头及其位置
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row): # 调用enumerate获取每个元素的索引及其值。
        print(index,column_header) # 每个文件头的索引
        '''
        0 AKDT # 日期
1 Max TemperatureF # 最高气温
2 Mean TemperatureF
....
20  CloudCover
21  Events
22  WindDirDegrees
'''
# 16.1.3 提取并读取数据
# 首先读取每天的最高气温
import csv

# 从文件中获取最高气温
filename = "sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = [] # 创建一个highs的空列表
    for row in reader: # 遍历余下的各行
         highs.append(row[1]) # 将索引[1]1处(第2列）的数据附加到 highs 末尾。

    print(highs) # 提取了每天的最高气温，并将它们作为字符串整洁的存储在一个类表中。
# 用int()将字符串转换为数字，让matplotlib能够读取他们。
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs) # 为什么是空列表呢？

# 16.1.4 绘制气温图表。 使用matplotlib创建一个现实每日最高气温的简单图形
import csv

from matplotlib import pyplot as plt

# 从文件中获取最高气温
filename = "sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = [] # 创建一个highs的空列表
    for row in reader: # 遍历余下的各行
         highs.append(row[1]) # 将索引[1]1处(第2列）的数据附加到 highs 末尾。

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(highs,c='red')

# 设置图形的格式
plt.title("Daily High temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature(F)", fontsize=16)

plt.show()

# 16.1.6 在图表中添加日期

import csv
from datetime import datetime

from matplotlib import pyplot as plt

# 从文件中获取日期和最高气温
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    reader_row = next(reader)

    dates, highs =[],[]
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates,highs, c='red')

# 设置图形的格式
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel("", fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()

# 16.1.7 涵盖更长的时间 2014整年
filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    reader_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# 设置图形的格式
plt.title("Daily high temperatures, -2014", fontsize=24)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()

# 16.1.8 再绘制一个数据系列
# 从文件中获取日期，最高气温和最低气温
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)
# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')

# 设置图形的格式
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.show()

# 16.1.9 给图表区域着色.方法fill_between()接受一个x和y值

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates,highs, c="red", alpha=0.5)
plt.plot(dates,lows, c="blue", alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.show()

# 16.1.10 错误检查。 缺失数据引发异常。death_valley_2014.csv
# 生成加利福尼亚死亡谷的气温图出现的情况
# 2-16日的数据孔雀，字符串为空，所以无法将空字符串转为整数
filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures - 2014\nDeath Valley,CA", fontsize=24)
plt.show()