#python 迭代器和生成器
'''迭代器是欧阳通红最强大的功能之一，是访问集合元素的一种方式
迭代器是一个可以记住遍历的位置的对象
迭代器对象从集合的第一个元素开始访问，直到所有元素被访问完结束，迭代器只能向前不能向后
迭代器有两个基本的方法 ：iter（）和next（）
字符串，列表或元组对象都可以用于创建迭代器
'''

import sys
list = [1,2,3,4,5]
it = iter(list)# 创建迭代器
print(next(it)) #输出迭代器的下一个元素
print(next(it))

# 迭代器对象可以使用常规语句进行遍历
list = [1,2,3,4,5]
it = iter(list)
for x in it:
    print(x, end=" ")

#也可以使用next（）函数
list = [1,2,3,4,5]
it = iter(list)

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

# 生成器
'''在python中使用yield 的函数被称为生成器（generator）
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器
在调用生成器的运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值，并在下一次运行next（）方法
时从当前位置继续运行
调用一个生成器函数，返回的是一个迭代器对象
'''

def fibonacci(n):
    a,b,counter = 0,1,0
    while True:
        if (counter > 0):
            return
        yield a
        a, b = b, a+b
        counter += 1
f = fibonacci(10)

while True :
    try :
        print(next(f),end = " ")
    except StopIteration:
        sys.exit()