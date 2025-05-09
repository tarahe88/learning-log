# 使用die类创建图表前，先来掷D6骰子，将结果打印出来，检查是否合理
from die import Die

# 创建一个D6
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(100): # 扔骰子100次
    result = die.roll()
    results.append(result) # 存到result列表里

print(results)

# 15.4.5 分析结果
# 分析掷一个D6骰子的结果，计算每个点数出现的次数
# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

    # 分析结果
    frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

# 15.4.6 绘制直方图。
# 有了频率列表后，就可以绘制一个表示结果的直方图。
# 直方图是一种条形图，直出了各种结果出现的频率。
import pygal
# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000times."
hist.x_labels = ["1","2","3","4","5","6"]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6", frequencies)
hist.render_to_file("die_visul.svg")

