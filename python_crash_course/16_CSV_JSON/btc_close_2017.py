# 需要翻墙打开url，否则报错。 json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"

# 下载json格式的交易收盘价数据，并使用模块json来处理它们。 pygal绘图工具对收盘价数据进行可视化。。
# btc_close_2017是一个很长的python列表，其中每个元素都是一个包含5个键的字典。统计日期，月份，周数，周几以及收盘价。
# 用函数urlopen来下载数据
from __future__ import absolute_import, division, print_function, unicode_literals # 书里面有错误，不该加括号。
from urllib.request import urlopen # 函数urlopen的代码稍微复杂些， 第三方模块requests更简单封装了许多常用的方法，让数据下载和读取方式变得非常简单
import json

json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
response = urlopen(json_url)
# 读取数据
req = response.read()
# 将数据写入文件
with open("btc_close_2017_urllib.json","wb") as f:
    f.write(req)
# 加载json格式
file_urllib = json.loads(req)
print(file_urllib)

# 函数urlopen的代码稍微复杂些， 第三方模块requests更简单封装了许多常用的方法，让数据下载和读取方式变得非常简单
import requests
json_url = "https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
req = requests.get(json_url) # 通过get方法向GitHub服务器发送请求。 像影后，返回的结果处处在req变量中。
# 将数据写入文件
with open("btc_close_2017_request.json","w") as f:
    f.write(req.text) # req.text属性可以直接读取文件数据，返回格式是字符串。保存为文件btc_close_2017_request.json
file_requests = req.json() # 直接用req.json()可以讲btc_close_2017.json文件的数据转换成python列表file_requests.

# 16.2.2 提取相关的数据
# 编写一个小程序提取btc_close_2017.json文件中的相关信息
import json
# 将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

# 打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    month = btc_dict['month']
    week = btc_dict['week']
    weekday = btc_dict['weekday']
    close = btc_dict['close']
    print("{} is month {} week {},{},the close price is {} RMB". format(date, month, week, weekday, close))

# 16.2.3 将字符串转换为数字值
# # 实际工作中，原始数据的格式经常是不同意的，此类数值类型转换造成的value error异常十分普遍。
# # 原因在于python不能直接将包含小数点的字符串"6928.6492"转换为整数
# btc_close_2017.json 中的每个键和值都是字符串，为了能在后面的内容中对教育数据进行计算，需要先将表示周数和收盘价的字符串转换为数值。

# 打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = (btc_dict['weekday'])
    close = int(float(btc_dict['close']))
    print("{} is month{}week{},{},the close price is {} RMB".format(date, month, week, weekday, close))

# 16.2.4 绘制收盘价折线图
# 用pygal实现折线图。需要获取x与y轴数据，创建几个列表来存储数据，遍历btc_data。转换为适当格式的数据存储到对应的列表中
# 创建5个列表，分别存储日期和收盘价.
#
dates = []
months = []
weeks = []
weekdays = []
close = []
# 每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
# 有了x和y轴，可以绘制折线图。数据点多，x有346个日期，回永济，要利用pygal的配置参数，对图形进行适当调整
import pygal # 导入模块pygal

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False) # 设置x_label_和show_作为初始化参数。false告诉图形不用显示所有的x轴标签
line_chart.title = '收盘价（¥）'
line_chart.x_labels = dates
N = 20 # x坐标轴每隔20天显示一次
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价',close)
line_chart.render_to_file('收盘价折线图(¥).svg')

# 16.2.5 时间序列特征初探。
import pygal
import math
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False) # 注意Line大写。
line_chart.title = '收盘价对数变换（¥)'
line_chart.x_labels = dates
N = 20 # x 轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close] # 注意是_ in 不是 _in 中间要有空格
line_chart.add('log收盘价',close_log)
line_chart.render_to_file("收盘价对数变换折线图(¥).svg")

# 16.2.6 收盘价均值

from itertools import groupby

def draw_line(x_data, y_data, title, y_legend):
    xy_map = [ ]
    for x, y in groupby(sorted(zip(x_data, y_data), key=lambda _: _[0])):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart
# 收盘价月日均值
idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], close[:idx_month],'收盘价月日均值(¥)','月日均值')
line_chart_month
# 收盘价周日均值
idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week], close[1:idx_week],'收盘价周日均值(¥)','周日均值')
line_chart_week
# 收盘价星期均值
idx_week = dates.index('2017-12-11')
wd = ["Monday",'Tuesday','Wednesday', 'Thursday',"Friday","Saturday","Sunday"]
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, close[1:idx_week],'收盘价星期均值(¥)','星期均值')

line_chart_weekday.x_labels = ["周一","周二","周三","周四","周五","周六","周日"]
line_chart_weekday.render_to_file('收盘价星期均值(¥).svg') # 书里缩进了，但是现实缩进报错。另外最终图与书里不一样

# 16.2.27 收盘价数据仪表盘
with open('收盘价Dashboard.html','w',encoding='utf-8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
        '收盘价折线图(¥).svg','收盘价对数变换折线图(¥).svg','收盘价月均值(¥).svg','收盘价周日均值(¥).svg','收盘价星期均值(¥).svg'
    ]:
        html_file.write('<object type="image/svg+xml" data="{0}" height =500></object>\n'.format(svg))
        html_file.write('</body></html>')