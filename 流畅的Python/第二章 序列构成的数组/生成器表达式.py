# coding:utf-8

'''
讲解：
虽然也可以用列表推导来初始化元组、数组或其他序列类型，但是生成器表达式是更好的选择。
这是因为生成器表达式背后遵守了迭代器协议，可以逐个地产出元素，而不是先建立一个完整的列表，
然后再把这个列表传递到某个构造函数里。前面那种方式显然能够节省内存。
'''