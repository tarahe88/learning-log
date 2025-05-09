# 17.2.2 添加自定义工具提示
# pygal中，将鼠标指向条形将显示它表示的信息，通常为工具提示。
import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LS

my_style = LS(color="#333366",base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie','django','flask']

plot_dicts = [ # 定义了名为plot_dicts的列表，包含3个字典，分别针对项目httpe, django和flask。
    {'value': 16101,'label': "Description of httpie."}, # 没个字典包含2个键：value和label。
    {'value': 15028,'label': 'Description of django.'}, # 根据VALUE相关的数字来确定条形高度
    {'value': 14798,'label': "Description of flask."}  # 使用label相关的字符串给条形创建工具提示
]
chart.add('', plot_dicts) # 方法add接受一个字符串和一个列表。调用add()时，传入了一个由表示条形的字典组成的列表plot_dicts
chart.render_to_file('bar_descriptions.svg')

