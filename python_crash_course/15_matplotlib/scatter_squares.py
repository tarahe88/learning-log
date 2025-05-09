# 15.2.3 使用scatter()绘制散点图并设置样式
# 绘制单个点，可使用函数scatter()，并向他传递一对x和y坐标，
# 将在指定位置上绘制一个点
import matplotlib.pyplot as plt

plt.scatter(2,4)
plt.show()

#设置输出样式
import matplotlib.pyplot as plt
plt.scatter(2,4,s=200) # 实参s设置了点的尺寸

# 设置图标标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both",which="major",labelsize=14)

plt.show()

# 15.2.4 使用scatter()绘制一系列点
# 要绘制一系列点，向scatter()传递两个分别包含x值和y值的列表
import matplotlib.pyplot as plt

x_values = [1,2,3,4,5] #列表包含要计算平方值的数字
y_values = [1,4,9,16,25] # 列表包含每个数字的平方值
#matplotlib依次从每个列表读取一个值来绘制一给单。要绘制的点的坐标分别为
# (1,1),(2,4),(3,9),(4,16),(5,25)

plt.scatter(x_values,y_values, s=100)

# 设置图标标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both",which="major",labelsize=14)

plt.show()

# 15.2.5 自动计算数据
#  绘制多点时，用python循环来替我们完成计算。下面是1000个点的代码
import matplotlib.pyplot as plt

x_values = list(range(1,1001)) # x值包含数字1-1000
y_values = [x**2 for x in x_values] # 遍历x列表计算平方

plt.scatter(x_values,y_values,s=40) # 输入列表和输出列表传递给scatter()

# 设置图标标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)


# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
#由于数据集较大，将点设置的较小，使用函数axis()制定了每个坐标轴的取值范围
# h函数axis()要求提供4个值：x和y的最小值和最大值

plt.show()  # 这个x 0 200 400, y为什么是0.0, 0.2, 0.4,0.8 1.0

# 15.2.6 删除数据点的轮廓。
# matplotlib默认蓝点黑轮廓，数据点不多时效果好，
# 数据点多的话，黑色轮廓粘在一起。删除数据点的轮廓，调用scatter()时传入实参edgecolor='none'
# plt.scatter(x_value,y_value,edgecolor='none',s=400)

# 15.2.7 自定义颜色。 修改数据点的颜色，可向scatter()传递参数c
# 将其设置为要使用的颜色的名称。
plt.scatter(x_values, y_values,c="red", edgecolor='none',s=40)
plt.show()
# 还可以使用rgb颜色模式自定义颜色。
# 传递参数c，设置元组包含0-1的小数值，分别表示红色，绿色，蓝色分量
plt.scatter(x_values, y_values,c=(0.2,1,0.8), edgecolor='none',s=40)
plt.show()

# 15.2.8 使用颜色映射
# pyplot内置了一组颜色映射。
import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

# 将c设置了一个y值列表，使用参数cmap告诉pyplot使用哪个颜色映射y最小的为浅蓝色，最大为深蓝色
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)

# 设置图标标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.show()

# 15.2.9 自动保存列表
plt.savefig("squares_plot.png", bbox_inches="tight") # 让程序自动将图标保存到文件中
# 对plt.show()的调用替换为对plt.savefig()的调用。第一个实参指定以什么样的文件名保存图表。
# 第二个实参制定将图标多余的空白区域才剪掉。如果要保留空白，可以省略这个实参