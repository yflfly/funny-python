# coding:utf-8
x = 'hello'

res = [x for x in 'ABC']

print(x)

'''
输出结果为：
hello

解释：
列表推导、生成器表达式，以及同它们很相似的集合（set）推导和字典（dict）推导，
在Python 3中都有了自己的局部作用域，就像函数似的。
表达式内部的变量和赋值只在局部起作用，表达式的上下文里的同名变量还可以被正常引用，局部变量并不会影响到它们。
'''