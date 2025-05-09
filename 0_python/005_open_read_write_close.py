# 学习爬虫时，掌握文件的读写操作是非常重要的，因为爬虫通常需要将抓取到的数据保存到文件中，或者从文件中读取配置信息。
# 以下是 Python 中文件读写的基本操作
# 1 打开文件。 python中，使用open()函数打开文件。open()函数的基本语法如下：
file = open(filename,mode)
# filename; 文件的路径和名称。
# mode: 打开文件的模式，常见的模式有：
    # ‘r': 只读模式（默认）
    # 'w': 写入模式，会覆盖文件内容
    # 'a'： 追加模式，在文件末尾添加内容
    # 'b': 二进制模式，与其他模式结合使用，如"rb"或'wb"
    # 'x':独占创建模式，如果文件已存在则报错
    # '+': 读写模式，与其他模式结合使用，如'r+'或'w+'.
# 2. 读取文件。读取整个文件。使用read()方法可以读取整个文件内容。
file = open('example.txt','r')
content = file.read()
print(content)
file.close()
# 逐行读取。 使用readline()方法可以逐行读取文件内容

file = open('example.txt','r')
line = file.readline()
while line:
    print(line.strip()) # 使用strip()去除行末的换行符
    line = file.readline()
file.close()
# 读取所有行。使用readlines()方法可以读取所有行并返回一个列表
file = open('example.txt',"r")
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()
# 3. 写入文件。 写入字符串。使用write()方法可以将字符串写入文件。
file = open('example.txt','w')
file.write("Hello,World!\n")
file.write('This is a new line.')
file.close()
# 写入多行。使用writelines()方法可以将一个字符串列表写入文件
lines = ['First line\n', 'Second line\n', 'Third line\n']
file = open("example.txt","w")
file.writelines(lines)
file.close()
# 4. 关闭文件。使用close()方法可以关闭文件，释放资源。
# 为了确保文件总是被正确关闭，可以使用with语句。这样文件会在with块结束后自动关闭
with open("example.txt",'r') as file:
    content = file.read()
    print(content)
# 文件会自动关闭。
# 5. 综合示例。综合示例展示了如何读取一个文件的内容，修改后写入另一个文件。
# 读取文件内容
with open('input.txt','r') as infile:
    lines = infile.readlines
# 修改内容
modified_lines = [line.upper() for line in lines]
#写入新文件
with open('output.txt','w') as outfile:
    outfile.writelines(modified_lines)
'''
6. 练习
创建一个文本文件 data.txt，并写入一些内容。
编写代码读取 data.txt 文件的内容，并将其中的每一行反转后写入 reversed_data.txt 文件。
使用 with 语句确保文件在操作完成后自动关闭。'''
with open("data.txt","r") as file:
    lines = file.readlines()
    reversed_lines = [lines.reverse()for line in lines]
# 不会了。


