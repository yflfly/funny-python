# coding:utf-8
from icecream import ic


def plus_five(num):
    return num + 5


ic(plus_five(4))
ic(plus_five(5))

'''
输出结果：
ic| plus_five(4): 9
ic| plus_five(5): 10

解释：
通过使用icecream，我们不仅可以看到函数输出，还可以看到函数及其参数！
'''