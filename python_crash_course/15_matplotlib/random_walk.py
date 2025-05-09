# 15.3 随机漫步。 使用python生成随机漫步数据，使用matplotlib以引人瞩目的方式将数据呈现出来
# 15.3.1 创建RandomWallk()类。
# 随机选择前进方向，这个类需要3个属性，1个是存储随机漫步的变量，其他两个是列表，
# 分别存储随机漫步经过的每个点的x和y坐标
# RandomWalk类只包含2个方法：__init__()和fill_walk()，其中后者计算随机漫步经过的所有点

from random import choice
# 所有选择都存储在一个列表，并在每次做决策都使用choice()来决定哪种选择

class RandomWalk:
    # 一个生成随机漫步数据的类
    def __init__(self, num_points=5000): # 随机漫步包含的默认点数设置为5000
        #初始化随机漫步的属性
        self.num_points = num_points

        # 所有随机漫步都始于(0, 0)
        self.x_values = [0] # 每次漫步都从点(0,0)出发
        self.y_values = [0]

# 15.3.2 选择方向。 使用fill_walk()来生车给你漫步包含的点，并决定每次漫步的方向
    def fill_walk(self):
        # 计算随机漫步包含的所有点
        # 不断漫步，知道列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿着方向前进的距离
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step ==0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
