# 17.1.4 处理API 响应
import requests
# 执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code) # 请求成功。输出：Status code: 200

# API响应存储在一个变量中
response_dict = r.json()

# 处理结果
print(response_dict.keys()) # 输出：dict_keys(['total_count', 'incomplete_results', 'items'])。 响应字典只包含3个键

# 17.1.5 处理响应字典。 将API调用返回的信息存储到字典中后，就可以处理这个字典中的数据了。
# 下面来生成一些概述这些信息的输出。 这是一种不错的方式，可以去确认收到了期望的信息，进而可以开始研究感兴趣的信息
import requests
# 执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code) # 请求成功。输出：Status code: 200

# API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count']) # 输出：Total repositories: 19216348 github 包含了 1950万个python仓库的信息

# 探索有关仓库的信息
repo_dicts = response_dict['items'] # 将获取的字典列表存储在repo_dicts
print("Repositories returned:", len(repo_dicts)) # 看看我们获取了多少个仓库的信息。 输出：Repositories returned: 30

# 研究第一个仓库
repo_dict = repo_dicts[0] # 提取了repo_dicts中的第一个字典，存储在repo_dict中。
print("\nKeys:",len(repo_dict)) # 打印这个字典包含的键数，看看其中有多少信息。 输出：Keys: 80. 有80个信息。
for key in sorted(repo_dict.keys()): # 打印这个字典的所有信息，看看那包含哪些信息。
    print(key) # 返回这个仓库的大量信息，包含68个键

# 下面提取repo_dict中与一些键相关联的值。
# 研究有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# 研究第一个仓库
repo_dict = repo_dicts[0]

print("\nSelected information about first repository:") # 打印了表示第一个仓库的字典中与很多键相关联的值
print("Name:", repo_dict['name']) # 项目名称。 # 排名第一的为github上星际最高的
print("Owner:", repo_dict['owner']['login']) # 所有者的字典，所有者的登录名
print("Stars:", repo_dict["stargazers_count"]) # 获得了多少个星的评级
print("Repository:",repo_dict['html_url']) # 在github仓库的URL
print("Created:",repo_dict['created_at']) # 项目创建时间
print("Updated:",repo_dict['updated_at']) # 最后一次更新时间
print("Description:",repo_dict['description']) # 仓库描述

# 17。1.6 概述最受欢迎的仓库
# 对这些数据可视化时，需要涵盖多个仓库。 编写一个循环，打印API调用返回的每个仓库的特定信息。 以便可视化包含这些信息
# 研究有关仓库的信息
repo_dicts = response_dict['items'] # 将获取的字典列表存储在repo_dicts
print("Repositories returned:", len(repo_dicts)) # 看看我们获取了多少个仓库的信息。 输出：Repositories returned: 30

print("\nSelected information about each repository:") # 打印了一条说明性信息
for repo_dict in repo_dicts: # 遍历repo_dicts中的所有字典。 在这个循环中，打印每个项目的名称，所有者，星级，在github上的url及描述
    print("Name:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Stars:", repo_dict['stargazers_count'])
    print("Repository:", repo_dict['html_url'])
    print("Description:", repo_dict['description'])

# 17.2 使用pygal可视化仓库
# 有了一些有趣数据后，进行可视化，呈现github上python项目的受欢迎程度。 创建一个交互式条形图，条形的高度表示项目获得了多少颗星
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LS # 导入用于图表的pygal样式。

# 执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code) # 打印状态以便获悉api调用是否出现了问题

# 将响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count']) # 打印找到的仓库总数

# 研究有关仓库的信息
repo_dicts = response_dict['items']

names, stars = [], [] # 创建2个空列表，用于储存将包含在图表中的信息。需要每个项目的名称，项目获得多少个星确定条形高度。
for repo_dict in repo_dicts: # 循环中，将项目名称和获得星数附加到这些列表的末尾。
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS(color='#333366', base_style=LCS) # 书里没有加 color=。 用LightenStyle类定义样式，深蓝色。实参base_style以使用lightcolorrizedstyle类
chart = pygal.Bar(style=my_style,xlabel_rotation=45, show_legend=False) # 使用Bar创建简单条形图，并传递my_style。
# 还传递另外2个样式实参；让标签绕x轴旋转45度，隐藏图例，因为我们只在图表中绘制一个数据系列。
chart.title = "Most-Starred Python Projects on GitHub" # 给图表指定标题
chart.x_labels = names  # 将属性x_labels设置为列表names

chart.add('', stars) # 添加数据时，将标签设置成了空字符串。
chart.render_to_file('python_repos.svg')

# 17.2.1 改进Pygal图表
# 可视化
my_style = LS(color='# 33366', base_style=LCS)

my_config = pygal.Config() # 创建pygal类Config的实例，将其命名为my_config. 通过修改my-config的属性，可定制图表的外观
my_config.x_label_rotation = 45 # 属性x_label是创建Bar实例时以关键字实参的方式传递
my_config.show_legend = False # 属性show_legend是创建Bar实例时以关键字实参的方式传递
my_config.title_font_size = 24 # 图表标题的字体大小
my_config.label_font_size = 14 # 副标签字体大小
my_config_major_label_font_size = 18 # 主标签字体大小
my_config_truncate_label = 15 # 使用truncate_label将较长的项目名缩短为15哥自负
my_config_show_y_guide = False # 隐藏图表中的水平线
my_config.width = 1000 # 自定义宽度

chart = pygal.Bar(my_config, sytle=my_style) # 创建Bar实例，将my_config作为第一个实参，从而通过一个实参传递了所有的配置设置
                                            # 我们可以通过上面my_config做任意数量的样式和配置修改，而这处的代码行将保持不变
chart.title = "Most-Starred Python Projects on Github"
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')

# 17.2.3 根据数据绘图。 自动生成plot_dicts，其中包含api调用返回的30个项目的信息
# 研究有关仓库的信息
repo_dicts = response_dict['items'] # 将获取的字典列表存储在repo_dicts
print("Number of items:", len(repo_dicts)) # 看看我们获取了多少个仓库的信息。 输出：Repositories returned: 30

names, plot_dicts = [], [] # 创建了2个空列表names和plot_dicts。为生成x轴上的标签。依然需要列表names
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS(color='# 33366', base_style=LCS)

my_config = pygal.Config() # 创建pygal类Config的实例，将其命名为my_config. 通过修改my-config的属性，可定制图表的外观
my_config.x_label_rotation = 45 # 属性x_label是创建Bar实例时以关键字实参的方式传递
my_config.show_legend = False # 属性show_legend是创建Bar实例时以关键字实参的方式传递
my_config.title_font_size = 24 # 图表标题的字体大小
my_config.label_font_size = 14 # 副标签字体大小
my_config_major_label_font_size = 18 # 主标签字体大小
my_config_truncate_label = 15 # 使用truncate_label将较长的项目名缩短为15哥自负
my_config_show_y_guide = False # 隐藏图表中的水平线
my_config.width = 1000 # 自定义宽度

chart = pygal.Bar(my_config, sytle=my_style) # 创建Bar实例，将my_config作为第一个实参，从而通过一个实参传递了所有的配置设置
                                            # 我们可以通过上面my_config做任意数量的样式和配置修改，而这处的代码行将保持不变
chart.title = "Most-Starred Python Projects on Github"
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

# 17.2.4 在图表中添加可单机的链接。
# pygal还允许你将图表中的每个条形用作网站的链接。 只需加一行代码，在为每个项目创建的字典中，添加一个键为'xlink'的键值对
names, plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label':repo_dict['description'],
        'xlink':repo_dict['html_url'], # 每个项目点击条形，就会跳出链接。
    }
    plot_dicts.append(plot_dict)
# 可视化
my_style = LS(color='# 33366', base_style=LCS)

my_config = pygal.Config() # 创建pygal类Config的实例，将其命名为my_config. 通过修改my-config的属性，可定制图表的外观
my_config.x_label_rotation = 45 # 属性x_label是创建Bar实例时以关键字实参的方式传递
my_config.show_legend = False # 属性show_legend是创建Bar实例时以关键字实参的方式传递
my_config.title_font_size = 24 # 图表标题的字体大小
my_config.label_font_size = 14 # 副标签字体大小
my_config_major_label_font_size = 18 # 主标签字体大小
my_config_truncate_label = 15 # 使用truncate_label将较长的项目名缩短为15哥自负
my_config_show_y_guide = False # 隐藏图表中的水平线
my_config.width = 1000 # 自定义宽度

chart = pygal.Bar(my_config, sytle=my_style) # 创建Bar实例，将my_config作为第一个实参，从而通过一个实参传递了所有的配置设置
                                            # 我们可以通过上面my_config做任意数量的样式和配置修改，而这处的代码行将保持不变
chart.title = "Most-Starred Python Projects on Github"
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')