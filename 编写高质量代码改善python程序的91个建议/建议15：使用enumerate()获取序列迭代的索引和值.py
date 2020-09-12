# coding:utf-8

'''
基本上所有的项目都存在对序列进行迭代并获取序列中元素进行处理的场景
'''
# 方法一 在每次循环中对索引变量进行自增
list1 = ['a', 'b', 'c', 'd', 'e']
index = 0
for each in list1:
    print('index:', index, 'element:', each)
    index += 1

# 方法二 使用range()和len()方法结合
list1 = ['a', 'b', 'c', 'd', 'e']
for i in range(len(list1)):
    print('index:', i, 'element:', list1[i])

# 方法三 使用while循环，用len()获取循环次数
list1 = ['a', 'b', 'c', 'd', 'e']
index = 0
while index < len(list1):
    print('index:', index, 'element:', list1[index])
    index += 1

# 方法四 使用zip()方法
list1 = ['a', 'b', 'c', 'd', 'e']
for i, e in zip(range(len(list1)), list1):
    print('index:', i, 'element:', e)

# 方法五 使用enumerate()获取序列迭代的索引和值
list1 = ['a', 'b', 'c', 'd', 'e']
for i, e in enumerate(list1):
    print('index:', i, 'element:', e)

'''
上面代码每一个的输出结果如下所示：
index: 0 element: a
index: 1 element: b
index: 2 element: c
index: 3 element: d
index: 4 element: e
'''

'''
这里推荐的是使用方法五，因为它代码清晰简洁，可读性好

'''


# enumerate()函数的内部实现非常简单，代码相当于如下代码表示：
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
