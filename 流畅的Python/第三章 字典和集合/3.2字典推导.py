# coding:utf-8

canshu = [(1, 'a'), (2, 'b'), (3, 'c')]

my_dict = {shuzi: zimu for shuzi, zimu in canshu}
print(canshu)
print(my_dict)
'''
输出结果如下所示：
[(1, 'a'), (2, 'b'), (3, 'c')]
{1: 'a', 2: 'b', 3: 'c'}

讲解：
字典推导（dictcomp）可以从任何以键值对作为元素的可迭代对象中构建出字典
一个承载成对数据的列表，它可以直接用在字典的构造方法中。
'''
