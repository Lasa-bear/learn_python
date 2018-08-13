# python  字典

'''字典是一种可变容器模型，且可以储存任意类类型的对象
字典的 每个键值对用冒号（：）分隔开，每个对之间用逗号（，）分割，整个字典包括在
花括号（{}）中'''

d = {1 : 'h',2 : 'b'}
print(d)

#键必须是唯一的，但是值不必
# 值可以是任何数据类型，但是键必须是不可变的，如字符串，数字，元组

# 创建一个字典

dict = {'alice':'678','benth':'456','cecil':'456'}

# 访问字典里的值

print(dict['alice'])
print(dict['benth'])

# 如果字典里没有键的访问数据就会报错
# print(dict['jiushi'])
# File "C:/Users/silence/PycharmProjects/learn_python/section1/learn11.py", line 23, in <module>
# 456
#     print(dict['jiushi'])
# KeyError: 'jiushi'
#
# Process finished with exit code 1

# 修改字典
#向字典添加新的内容的方法是增加新的的键值对，修改或删除已有的键值对

dict = {'name':'runoob','age':8,'class':'first'}
dict['age'] = 9
dict['school'] = 'beijing university'

print(dict['age'])
print(dict['school'])
print(dict)

# 删除字典元素
# 能够删除单一的元素也能清空字典，清空只需要一项操作
# 显示删除一个字典用del命令 如下实例：

del dict['name']  # 删除键’name‘
print(dict)

dict.clear()   # 清空字典
print(dict)

del dict    # 删除字典

#不允许同一个键出现两次。创建时如果一个键被赋值两次，后一个值会被记住
# dict = {'name':'jiushi','age':5,'name':'小菜鸟'}
#
# print(dict)
# print(dict['name'])

# 键必须是不可变的，所以可以用数字，字符串或者元组充当，而列表就不行
# dict = {['name']:'jiushi','age':7}
# print(dict)
#TypeError: unhashable type: 'list'报错

# 字典内置函数&方法

