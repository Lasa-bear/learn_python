#python3 面向对象
'''Python从设计之初就已经是一门面向对象的语言，正因为如此，在Python中创建一个类和对象是很容易的。本章节我们将详细介绍Python的面向对象编程。
如果你以前没有接触过面向对象的编程语言，那你可能需要先了解一些面向对象语言的一些基本特征，在头脑里头形成一个基本的面向对象的概念，这样有助于你更容易的学习Python的面向对象编程。
接下来我们先来简单的了解下面向对象的一些基本特征。'''

#面向对象技术 简介
'''(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    方法：类中定义的函数。
    类变量：类类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
    方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
    实例变量：定义在方法中的变量，只作用于当前实例的类。
    继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
    实例化：创建一个类的实例，类的具体对象。
    对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
和其它编程语言相比，Python 在尽可能不增加新的语法和语义的情况下加入了类机制。
Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。 
对象可以包含任意数量和类型的数据。 '''
#类实例化后，可以使用其属性，实际上创建一个类之后，可以通过类名访问其属性
#类对象
'''类对象支持两种操作：属性引用和实例化
属性引用使用个python中所有的属性引用一样的标准语法：obj.name
类对象创建后，类命名空间中所有的命名都是有效属性名。所以如果类属性是这样
'''
# class Myclass:
#     i = 12344
#     def __init__(self):
#         self.date = []
#     def function(self):
#         return 'hello world'

#实例化
# x = Myclass()

#访问类的属性和方法
# print('myclass 类的属性i为',x.i)
# print('myclass 类的方法function输出为',x.function())
#
# '''很多类都倾向于将对象创建为有初始状态 因此类可能定义一个名为 __init__()的特殊构造方法
# '''
#
# class Complex :
#     def __init__(self,realpart,imagpart):
#         self.r = realpart
#         self.i = imagpart
# x = Complex(3,5)
# print(x.i,x.r)

#self代表类的实例，而非类
#类的方法于普通方法的函数只有一个特别的区别--它们必须有一个额外的第一参数名称，按照惯例它的名称是self
# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
#
# t = Test()
# t.prt()

#从执行结果可以明细那的看出，self代表的是类的实例，代表当前对象的地址，而self。class则指向类
# self不是python关键字，把它换成其他也可以正常执行的

#类的方法
#在类的内部，使用def关键字来定义一个方法，与一般函数不同，类方法必须包含参数self，且为第一个参数，self代表的是类的实例

# class People:
#     #定义类的基本属性
#     name = ''
#     age = 0
#     # 定义私有属性，私有属性在类外部无法直接进行访问
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print('%s 说：我%d岁了！'%(self.name,self.age))
#
# #实例化类
# p = People('JIUSHI',3,4)
# p.speak()

#继承
#python同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示
# class DerivedClassName(BaseClassName1):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>

'''需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索，即方法在字类中
未找到时，从左到右查找基类中是否包含方法
BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点
非常有用
class DerivedClassName(modname.BaseClassName):'''

# class Student(People):
#     grade = 0
#     def __init__(self,n,a,w,g):
#         # 调用父类的构造函数
#         People.__init__(self,n,a,w)
#         self.grade = g
#     #覆盖父类的方法
#     def speak(self):
#         print('%s说：我%d岁了，我在读%d年级'%(self.name,self.age,self.grade))
#
# s = Student('haishi',4,5,6)
# s.speak()

# 多继承
#python同样有限的支持多继承形式。多继承的类定义如下
# class DerivedClassName(Base1, Base2, Base3):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>

#要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在字类在使用时未指定，python从左至右搜索，方法在字类中为找到时，从左至右
# 查找父类中是否包含方法
class people():
    name = ''
    age = 0
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print('%s 说：我今年%d岁了'%(self.name,self.age))

class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade = g
    def speak(self):
        print('%s 说：我今年%d岁了，在读%s年级'%(self.name,self.age,self.grade))

class spaker():
    name = ''
    topic = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t

    def speak(self):
        print('我是%s，我演讲的题目是%s'%(self.name,self.topic))


class sample(spaker,student):


    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        spaker.__init__(self,n,t)


test = sample('jisuhini',5,67,8,'奋斗')
test.speak()

#方法重写
#如果你的父类方法的功能不能满足你的需求，你可以在字类重写你父类的方法

class Parent(): #定义父类
    def myMthod(self):
        print('调用父类方法')

class Child(Parent):    #定义字类
    def myMthod(self):
        print('调用字类方法')

c = Child() #实例化子类对象
c.myMthod()     #字类调用重写方法
super(Child,c).myMthod()

#super()函数是用于调用父类（超类）的一个方法

# 类属性与方法
#类的私有属性
'''__private_attrs:俩个下划线开头，声明属性为私有，不能再类外部被使用或直接访问。再类内部的方法中使用时self.__private_attrs
'''
#类的方法
'''再类的内部，使用def关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数self且为第一个参数，self代表的是类的实例
self的名字并不是规定死的，也可以是this，但是最好是self
'''
#类的私有方法
'''__private_method:两个下划线开头，声明该方法为私有方法，只能再类地内部调用，不能再类的外部调用，不能在类的外部调用
self.__private_method
'''
class JustCount:
    __ssecretCount = 0
    publicCount = 0

    def count(self):
        self.__ssecretCount += 1
        self.publicCount += 1
        print(self.__ssecretCount)

c = JustCount()
c.count()
c.count()
print(c.publicCount)
# print(c.__secretCount)   # 会报错 实例不能访问私有变量

class Site:
    name = ''
    url = ''
    def __init__(self,n,u):
        self.name = n
        self.url = u

    def who(self):
        print('name:',self.name)
        print('url:',self.url)

    def __foo(self):
        print('这是一个私有方法')

    def foo(self):
        print('这是一个公共方法')
        self.__foo()   # 可以在类中调用类中的私有方法

s = Site('就是这么没意思','www.meiyisi.com')
s.who()
#s.__foo()   # 在类外部调用类中的私有方法会报错
s.foo()

'''类的专有方法
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 乘方'''

#运算符重载

