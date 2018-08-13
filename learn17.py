#python数据结构

from collections import deque
print('*******************')
'''python中列表是可变的，这是区别于字符串和元组的最重要特点，一句话概括：列表可以修改，而字符串和元组不能
以下是python中列表的方法

list.append(x)	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L)	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x)	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i])	从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear()	移除列表中的所有项，等于del a[:]。
list.index(x)	返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x)	返回 x 在列表中出现的次数。
list.sort()	对列表中的元素进行排序。
list.reverse()	倒排列表中的元素。
list.copy()	返回列表的浅复制，等于a[:]。

'''
a = [1,2,33,56,8989,33]
print(a.count(33),a.count(1),a.count(0))  #list.count()统计列表中元素出现的的次数

a.insert(2,-1)   # list.insert()在指定位置插入元素
print(a)

a.append(100 )  #list.append()在list末尾添加元素
print(a)

print(a.index(33))  #list.index()返回某指定元素的索引

a.remove(1) #list.remove()删除指定元素
print(a)

a.reverse() #list.reverse()将列表倒序
print(a)

a.sort()
print(a)    #list.sort()给列表中的元素排序

print(a.pop())  #list.pop()删除最后一个元素，并将其值返回
print(a)

print(a.pop(2))
print(a)

#将列表当作堆栈使用
'''列表方法使列表可以很方便的作为一个堆栈使用，堆栈作为特定的数据结构 最先进入的元素最后一个被释放（先进后出）
用append()方法可以把一个元素添加到堆栈顶。用不指定索引的pop（）方法可以用把一个元素从堆栈顶释放出来'''

stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)

print(stack.pop())
print(stack)

print(stack.pop())
print(stack)

print(stack.pop())
print(stack)

#将列表当作队列用，只是在队列中第一加入的元素，第一个取出来，但是拿列这样的目的效率不熬
#在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头目弹出的速度却不快（因为所有其他元素都得一个一个的移动）

# 在上边已经导入 deque模块

queue = deque(['Eric','Jhon','Michael'])
queue.append('Terry')  # Terry 来了
queue.append('Graham')   # Graham 来了

print(queue.popleft())

print(queue.popleft())

print(queue)

#列表推导式

'''列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。

每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。

这里我们将列表中每个数值乘三，获得一个新的列表：'''

vec = [2,4,6]
then = [x*3 for x in vec]
print(then)

then1 = [[x,x*2] for x in vec]
print(then1)

freshfruit = ['banana','logberry','passion fruit']
print([weapon.strip() for weapon in freshfruit])    #x.strio()输出字符串的副本

#可以用if字句作为过滤器
print([x*3 for x in vec if x > 3])
print([x*3 for x in vec if x < 3])

vec1 = [2,4,6]
vec2 = [4,6,8]

print([x*y for x in vec1 for y in vec2])
print([vec1[i] * vec[2] for i in range(len(vec1))])

# 嵌套列表解析
'''python 的列表还可以嵌套
'''
matrix = [
    [1,2,3,4]
    [5,6,7,8]
    [9,10,11,12]
]
print(matrix)
#将3x4 的矩阵列表转化为 4x3 的列表
print([row[i] for row in matrix] for i in range(4))

#del 语句
'''使用del语句可以从一个列表中依索引而不是值来 删除一个元素。这与使用pop（）返回一个值不同。可以使用del语句从列表
中删除一个切割，或者清空整个列表
'''
a = [-1,1,2,66.24,33,33,12,3]
del a[0]
print(a)

