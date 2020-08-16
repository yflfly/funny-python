# coding:utf-8

list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4]
for e1, e2 in zip(list1, list2):
    print(e1 + ' vs ' + str(e2))

'''
输出的结果如下所示：
a vs 1
b vs 2
c vs 3
d vs 4
'''