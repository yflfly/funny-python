# coding:utf-8

# 1 一行代码交换a,b
a = 1
b = 2
print('''a is {} b is {}'''.format(a, b))
a, b = b, a
print('''a is {} b is {}'''.format(a, b))

'''
输出结果为：
a is 1 b is 2
a is 2 b is 1
'''

# 2 一行代码反转列表
a = [1, 2, 3]
b = a[::-1]
print(a, b)
'''
输出结果为：
[1, 2, 3] [3, 2, 1]
'''

# 3 一行代码合并两个字典
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {**dict1, **dict2}
print(dict3)
'''
输出结果为：
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
'''

# 4 一行代码列表去重
set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# 5一行代码求多个列表中的最大值
max(max([[1, 2, 3], [5, 1], [4]], key=lambda v: max(v)))  # 5

# 6一行代码生成逆序序列
list(range(10, -1, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
