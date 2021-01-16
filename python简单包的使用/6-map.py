# coding:utf-8
'''
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
'''


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8])
print(r)
print(list(r))

'''
输出结果如下所示：
<map object at 0x000002CFFA11F470>
[1, 4, 9, 16, 25, 36, 49, 64]
解释：
map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
'''
