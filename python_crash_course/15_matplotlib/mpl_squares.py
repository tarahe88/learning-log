import matplotlib.pyplot as plt
# 15.2 绘制简单的折线图
squares = [1,4,9,16,25]
plt.plot(squares)
plt.show()

# 15.2.1 修改标签文字和线条粗细
squares  = [1,4,9,16,25]
plt.plot(squares, linewidth=5) #线条粗细

# 设置图片标题，并给坐标加上标签
plt.title("Square Numbers", fontsize=24) # 图标标题和文字大小
plt.xlabel("Value", fontsize=14) # x轴标题和大小
plt.ylabel("Square of Value", fontsize=14) # y轴标题和大小

#设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14) # 刻度大小
plt.show()

# 15.2.2 矫正图形
import matplotlib.pyplot as plt

input_values = [1,2,3,4,5] # 不写这个，x轴默认0开始。
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)

# 设置图标标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24) # 图标标题和文字大小
plt.xlabel("Value", fontsize=14) # x轴标题和大小
plt.ylabel("Square of Value", fontsize=14) # y轴标题和大小

#设置刻度标记的大小
plt.tick_params(axis="both", labelsize=14) # 刻度大小
plt.show()


