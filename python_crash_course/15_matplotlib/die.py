# 15.4 使用Pygal模拟掷骰子
# 将使用python可视化包Pygal来生成可缩放的矢量图形文件。 对于需要在尺寸不同的屏幕上显示的图表，这很有用。
# 15.4.1 安装Pygal
# 15.4.2 pygal可创建什么样的图表，请查看图表类型画廊
# www.pygal.org 单击 documentation, 再单击chart types

from random import randint

class Die():
    # 表示一个骰子的类

    def __init__(self, num_sides=6):
        # 骰子默认为6面
        self.num_sides = num_sides

    def roll(self):
        # 返回一个位于1和骰子面数之间的随机值
        return randint(1, self.num_sides)
