# python 运算符

'''python 语言主要支持一下运算符
算术运算符
比较（关系）运算符
赋值运算符
逻辑运算符
位运算符
成员运算符
身份运算符
运算符优先级
'''
a = 10
b = 21
print(b % a)# % 为取余
print(a ** b) # 输出a 的 b次幂
print(a / b)# 输出为浮点数
print(a // b)# 输出为商

# 运算结果
# 1
# 1000000000000000000000
# 0.47619047619047616
# 0

# 比较运算符
# == 、 ！= 、> 、<、>=、<=、
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# python 赋值运算符
# =	简单的赋值运算符	c = a + b 将 a + b 的运算结果赋值为 c
# +=	加法赋值运算符	c += a 等效于 c = c + a
# -=	减法赋值运算符	c -= a 等效于 c = c - a
# *=	乘法赋值运算符	c *= a 等效于 c = c * a
# /=	除法赋值运算符	c /= a 等效于 c = c / a
# %=	取模赋值运算符	c %= a 等效于 c = c % a
# **=	幂赋值运算符	c **= a 等效于 c = c ** a
# //=	取整除赋值运算符	c //= a 等效于 c = c // a

# python位运算符
# 按位运算符是把数字看作是二进制来进行计算的
# />>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数	a >> 2 输出结果

# python逻辑运算符

x = 10
y = 20
print(x and y)
print(x or y)
print(not x)

# and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
# or	x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
# not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False

# python 成员运算符
'''除了以上的运算符之外，python还支持成员运算符，测试实例中包含一系列的
成员，包括list tuple String
in	如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。'''

list = [1,3,4,'jishi ','nishuo d ']
print(x in list)   # 返回False
print(y not in list)

# 身份运算符
'''身份运算符 用于比较两个对象的存储单元
is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。'''
 # 标注：id（）函数用于获取对象的内存地址

a = 20
b = 20
if (a is b):
    print('1 - a 和 b 有相同的标识符')
else:
    print('1 - a 和 b 没有相同的标识符')
if (id(a) == id(b)):
    print('2- a和b 有相同的标识')
else:
    print('2 - a 和 b 没有相同的标识')

b = 30

if (a is b):
    print('3 - a 和 b 有i是相同的标识')
else:
    print('3 - a  和 b没有相同的标识')

'''is 与 == 的区别
is 用于判断两个变量 引用对象是否为同一个， == 用于判断引用的值是否相等'''

# python运算符的优先级


