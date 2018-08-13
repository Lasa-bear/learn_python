# python基本语法


str = "jiushi"

print(str)   #输出字符串
print(str[0:-1])  #输出第一个到倒数第二个字符
print(str[0])  #输出第一个字符串
print(str[2:5])   # 输出从第三个开始到第五个字符
print(str[2:])#输出从第三个开始后的所有字符
print(str * 2)# 输出字符串两次
print(str + 'zenyang ')#  连接字符串

print('--------------------')
print('hello \njiushi')# 使用反斜杠(\)+n转义特殊字符
print(r'hello \njiushi')#在字符串前面添加一个r表示原始字符串不会发生转义
#  空行
'''函数治安或类的方法之间用空行分隔开，表示一段新的代码的开始
类和函数入口之间也用一行空行分隔开，以突出函数入口的开始'''

# input('请输入')

# 同一行显示多条语句
'''python可以在同一行中使用多条语句 语句之间使用；分隔开'''
import sys;x = 'runoob';sys.stdout.write(x + '\n')

# print输出
'''print默认输出是换行的，如果要实现不换行需要在变量末尾加end=""'''

print('jiushi nide ')
x = 'zenyagn '
y = 'ruguo shen'
print (x)
print(y)
print (x,end="")
print(y,end="")

# import 与from ...import
'''在python中用import或者from ，，，import导入相应的模块
将整个模块（somemodule）导入，格式为import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *'''




