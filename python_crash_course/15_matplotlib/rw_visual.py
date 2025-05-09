# 下面的代码将随机漫步的所有点都绘制出来
import matplotlib.pyplot as plt

from random_walk import RandomWalk

#创建一个RandomWalk实例，并将其包含的点都绘制出来
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()

# 15.3.4 模拟多次随机漫步

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断的模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk (y/n): ")
    if keep_running == "n":
        break

# 15.3.5 设置随机漫步图的样式
# 15.3.6 给点着色
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolor="none", s=15)
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == "n":
        break

# 15.3.7 重新绘制起点和终点

while True:
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none',s=15)

    # 突出起点和终点
    plt.scatter(0,0,c="green",edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=100)
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == "n":
        break

# 15.3.8 隐藏坐标轴

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values[-1],rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == "n":
        break

# 15.3.9 增加点数
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 绘制点并将图形显示出来
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolor='none', s=1)

    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == "n":
        break

# 15.3.10 调整尺寸以适合屏幕
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10,6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == "n":
        break