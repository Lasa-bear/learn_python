# python 列表

'''序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。

Python有6个序列的内置类型，但最常见的是列表和元组。

序列都可以进行的操作包括索引，切片，加，乘，检查成员。

此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。

列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。

列表的数据项不需要具有相同的类型'''

for x in [1,2,3]:
    print(x,)    # 迭代

# 列表还支持拼接操作

squares = [1,2,3,4,4,5,]
squares += [98,65,4,34]
print(squares)

# 嵌套列表
a = ['a','b','c']
n = [1,2,3]
x = [a,n]
print(x)
print(x[1])
print(x[0][1])

print(len(a))   # len()输出list的长度
print(max(a))   # max()输出list中的最大值
print(min(a))   # min()输出list中的最小值

t = (2,2,3,4)
print(t)

h = list(t)   # 将元组转化为列表
print(h)

h.append(5) # 在list末尾添加新的对象
print(h)

print(h.count(2))   # 统计某个人元素在list中出现的次数

h.extend((1,2,3,5))  # 在列表末尾一次性追加另一个序列中的多个值
print(h)

h.extend([1,2,3,5])
print(h)

print(h.index(3))   # 从列表中找出某一个值第一个匹配项的索引位置

h.insert(3,100)     #在某个位置插入某个元素
print(h)

h.pop()    # 默认删除list中的最后一个元素并返回该元素的值
print(h)
print(h.pop())

h.reverse()     # 将列表反向
print(h)

h.sort()        # 对原列表进行排序
print(h)

h.clear()       # 清空列表
print(h)

t = h.copy()        # 复制列表
print(t)

