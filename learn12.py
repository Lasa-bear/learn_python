# python集合 set
# 集合（set）是一个无序不重复元素的序列
#可以使用大括号{}或者set()函数创建集合，注意：创建一个空集合必须用set（）
#而不是{}因为{}是用来创建一个空字典

p = {2,'56hj', 456,'jiushi'}
print(p)

h = {'apple','orange','apple','banana','orange'}
print(h)   #去重功能

print('orange' in h)  #快速判断元素是否在集合内
print('meiyou' in h)

# 下面展示两个集合之间的运算
a = set('asdffdsdfg')
b = set('aserthvyuj')
print(a)   # a中包含的 元素
print(a - b)  #a中包含b中不包含的元素
print(a|b)   # a或b中包含的所有元素
print(a&b)   # a\b都包含的元素
print(a^b)   #同时包含于a和b的元素

# 集合的基本操作
# 1、添加元素
thisset = set(('jiushi','google','facebook'))
thisset.add('twitter')
print(thisset)

#s.update()也可以添加元素，且参数可以是列表，元组，字典等
thisset.update({'meiyou','shenme'})
print(thisset)

thisset.update([1,3],[4,5])
print(thisset)

#s.remove()移除元素`
my_set1 = set(('apple',))
print(my_set1)
