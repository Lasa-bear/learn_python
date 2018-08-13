# python函数
print('*******************')
'''函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段
函数能够提高如应用的模块性，和代码的重复利用率。你已经知道python提供了很多内建函数
比如print（）。但是你有可以自己创建函数，这叫做用户自定义函数
'''

# 定义一个函数
'''你可以定义一个由自己想要功能的函数，以下是简单的规则
    1、函数代码块以def关键词开头，后接函数标识符名称和圆括号（）
    2、任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数
    3、函数的第一行语句可以选择性地使用文档字符串用于存放函数说明
    4、函数内容以冒号起始，并且缩进
    5、return [表达式]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回None
    '''
# 语法
def hello():
    print("hello world!")

hello()

def area(width,height):
    return width * height

print(area(100,200))

def print_welcome(name):
    print('welcome '+name)

print_welcome('xiaona')

# 函数调用
'''定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构
这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从python命令提示符执行
'''

def printme(str):
    print(str)
    return
printme('我要调用用户自定义函数！')
printme('再次调用同一函数')

'''参数传递
在python中，类型属于对象，变量是没有类型的'''

a = [1,2,3]
a = 'runoob'

'''以上代码中，[1,2,3]是list类型。‘runoob’是string类型而变量a 是没有类型的，它仅仅是一个对象的引用（一个指针）
可以是指向list类型对象，也可以是指string类型对象'''
# 可更改和不可更改对象
'''在python中string tuples和number是不可更改的对象 而list和dict是可以修改的对象
    不可变类型;变量赋值a = 5后再赋值 a = 10，这里实际是新生成一个int值对象10 再让a指向它，而
    5被丢弃，不是改变a的值，相当于新生成了a。

    可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
    
    python 函数的参数传递：

不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。

可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。'''

def changeint(a):  # python 传不可变对象
    a = 10
    print(a)
b = 2
changeint(b)
print(b)    #2

def changeme(mylist):       #传可变对象实例
    mylist.append([1,2,3,4])
    print(mylist)
    return
mylist = [10,20,30]
changeme(mylist)        #可变对象实例在函数中修改了参数，那么在调用这个函数的函数中原始的参数也被改变
print(mylist)

# 参数
'''以下是调用函数时可使用的正式参数类型
    必需参数
    关键字参数
    默认参数
    不定长参数
    '''
# 必需参数
'''必需参数须以正确的顺序入函数 调用时的数量必须和声明时的一样
调用priintme（）函数你必须传入一个参数不然会报错
'''

# def printme(str):
#     print(str)
#     return

#关键字参数
'''关键字参数和函数调用关系紧密 函数调用使用关键字参数来确定传入的参数值
使用关键字参数允许函数调用时参数的 顺序与声明时不一致 因为python解释器能够用参数名匹配参数值
一下实例在函数printme（）调用时使用函数名'''
#
# def printme(str):
#     print(str)
#     return
#
# printme(str = '菜鸟教程')

def printinfo(name,age):
    print('name',name)
    print('age',age)
    return

printinfo(age = 50,name = 'jisuhi')  # 函数的参数使用不需要指定顺序

# 默认参数
#调用函数时，如果没有传递参数，则会使用默认参数，一下如果没有传入age参数则使用默认参数

# 可写函数说明
# def printinfo(name, age=35):
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
#
#
# # 调用printinfo函数
# printinfo(age=50, name="runoob")
# print("------------------------")
# printinfo(name="runoob")

# 不定长参数
#你可能需要一个函数能够处理比当初声明时更多的参数，这些参数叫做不定长参数和上述两种参数以通声明时不会明名

# 加*的参数会以元组（tuple）的形式导入存放所有未命名的变量参数
def printinfo(arg1,*vartuple):
    print(arg1)
    print(vartuple)
    return
printinfo(70,80,69)

#匿名函数
'''lambda只是一个表达式，函数体比def简单很多
lambda的主题时一个表达式，而不是一个代码块，仅仅能在lambda中封装有限的逻辑
lambda函数拥有自己的明名空间，且不能访问自有参数列表之外或全局明名空间里的参数
虽然lambda函数看起来只能写一行，却不同于c或者c++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率
'''
# 实例
sum = lambda arg1,arg2:arg1 + arg2

#调用sum函数
print('相加以后的值为：',sum(10,20))
print('相加以后的值：',sum(20,30))

#return 语句
'''return语句[表达式]退出函数，选择性地调用方返回一个表达式。不带参数值的return语句返回None。之前的例子都没有示范如何返回数值，下边实例告诉你怎么做
'''

def sum(arg1,arg2):
    total = arg1 +arg2
    print(total)
    return total
total = sum(20,60)

#变量作用域
'''一个程序的所有变量并不是在那个位置都可以访问的，访问权限据定于这个变量是在哪里赋值的
变量的作用域决定了在那一部分程序你可以访问哪个特定的变量名称，两种最基本的变量作用域如下
全局变量
局部变量
'''

# 全局变量和局部变量
'''定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域
局部变量只能在其被声明的函数的内部访问，而全局变量可以在整个程序内访问。调用函数时，所有在函数内声明的变量名称都将被加到作用域中
'''

total = 0;  # 这是一个全局变量
# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total;
# 调用sum函数
sum(10, 20);
print("函数外是全局变量 : ", total)



