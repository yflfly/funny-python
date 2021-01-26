# coding:utf-8

x = 'ABC'

dumpy = [ord(each) for each in x]
print(x)
print(dumpy)
'''
输出结果为：
ABC
[65, 66, 67]

讲解：
1）x的值被保留了。
2）列表推导也创建了正确的列表。列表推导可以帮助我们把一个序列或是其他可迭代类型中的元素过滤或是加工，然后再新建一个列表。
Python内置的filter和map函数组合起来也能达到这一效果，但是可读性上打了不小的折扣。

'''

'''
filter和map合起来能做的事情，列表推导也可以做，而且还不需要借助难以理解和阅读的lambda表达式。
后面详细讲解
'''
