# python 基本数据类型
'''python 中的变量不需要声明。每个变量在使用之前都必须赋值，变量赋值以该变量才会被创建
在python中变量就是变量，它没有类型  我们所说的类型是值内存中对象的类型'''

counter = 100
miles = 12.00
name = 'jiushi '

print(counter)
print(miles)
print(name)
# 多个变量赋值
# python中允许你同时为多个变量赋值
a = b = c = 5
# 以上实例创建一个整型对象 值为1 从后向前赋值 三个变量都指向同一个内存地址

# 也可以为多个对象制定多个变量

a,b,c = 1,2,'jiushi '

# python 中六个标准数据类型中
# 不可变数据 number（数字）、string（字符串）、tuple（元组）
# 可变数据类型 list（列表）、dictionary（字典）、set（集合）

# isinstance（）函数
a = 222
print (isinstance(a,int))

# isinstance 和type
class A:
    pass
class B(A):
    pass

# isinstance(A(),A)    # return Ture
# type(A) == A   # return Ture
# isinstance(B(),A)  # return Ture
# type(B(),A)  #return False