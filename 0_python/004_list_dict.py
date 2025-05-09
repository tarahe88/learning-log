# 学习 Python 中的列表（List）和字典（Dictionary）是掌握基础数据结构的重要一步
# 1.列表（list)是python中最常用的数据结构之一，是一个有序的元素集合，可以包含不同类型的元素
# 创建列表
my_list = [1,2,3,4,5]
mixed_list = [1, "Hello", 3.14, True]
# 访问列表元素。 列表中的元素可以通过索引访问，索引从0开始
print(my_list[0]) # 输出: 1
print(mixed_list[1]) # 输出：Hello
# 修改列表元素。 可以通过索引来修改列表中的元素。
my_list[0] = 10
print(my_list) # 输出： [10, 2, 3, 4, 5]
# 列表常用操作
# 添加元素：使用append()方法在列表末尾添加元素。
my_list.append(6)
print(my_list) # 输出： [10, 2, 3, 4, 5, 6]
# 插入元素：使用insert()方法在指定位置插入元素
my_list.insert(1,20)
print(my_list) # [10, 20, 2, 3, 4, 5, 6]
# 删除元素：使用remove()方法删除指定元素，或使用pop()方法删除置顶索引的元素。
my_list.remove(20)
print(my_list) # 输出：[10, 2, 3, 4, 5, 6]
my_list.pop(0)
print(my_list) # 输出：[2, 3, 4, 5, 6]
# 列表长度：使用len()函数获取列表长度
print(len(my_list)) # 输出：5
# 列表切片：使用切片操作获取子列表。
print(my_list[1:3]) # 输出：[3,4]

# 2. 字典（dictionary)。 字典是python中另外一种功能重要数据结构，它是一个无序的键值对(key-value)集合。
my_dict = {"name": "Alice","age": 25, "city": "New York"}
# 访问字典元素。 通过键来访问字典中的值
print(my_dict["name"]) # 输出：Alice
# 修改字典元素。 可以通过键来修改字典中的值
my_dict["age"] = 26
print(my_dict) # 输出: {'name': 'Alice', 'age': 26, 'city': 'New York'}
# 字典常用操作。
# 添加元素： 直接通过新的键来添加元素
my_dict["email"] = "alice@example.com"
print(my_dict) # # 输出: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}
# 删除元素： 使用pop()方法删除指定键的元素。
my_dict.pop("age")
print(my_dict) # 输出: {'name': 'Alice', 'city': 'New York', 'email': 'alice@example.com'}
# 获取所有键： 使用keys()方法获取所有键
print(my_dict.keys())  # 输出: dict_keys(['name', 'city', 'email'])
# 获取所有值： 使用values()方法获取所有值
print(my_dict.values()) #
# 获取所有键值对：使用items()方法获取所有键值对
print(my_dict.items())  # # 输出: dict_items([('name', 'Alice'), ('city', 'New York'), ('email', 'alice@example.com')])

# 3. 列表与字典的结合。列表和字典可以结合使用，形成更复杂的数据结构。如列表中可以包含字典，字典中也可以包含列表。
# 列表中包含字典
users = [
    {"name":"Alice", "age": 25},
    {"name":"Bob", "age": 30}
]
print(users[0]["name"])  # 输出: Alice
# 字典中包含列表
person = {
    "name": "Alice",
    "hobbies": ["reading", "traveling", "coding"]
}
print(person["hobbies"][1]) # 输出：traveling

# 4. 练习。 创建一个包含多个字典的列表，每个字典表示一个学生，包含姓名，年龄和成绩
students = [
    {"name":"Anna","age": 9, "score": 90 },
    {"name":"Betty","age":10, "score":98},
    {"name": "Kevin","age": 10, "score": 100}
]
for student in students:
    print(student)
'''{'name': 'Anna', 'age': 9, 'score': 90}
{'name': 'Betty', 'age': 10, 'score': 98}
{'name': 'Kevin', 'age': 10, 'score': 100}'''






