# coding:utf-8
import filecmp

res1 = filecmp.cmp(r'data/ceshi1.txt', r'data/ceshi2.txt')
res2 = filecmp.cmp(r'data/ceshi1.txt', r'data/ceshi1.txt')
print(res1)
print(res2)
'''
输出结果为：
False
True

说明：
python中提供了很便捷的方法来判断两个文件的内容是否相同，只要两行代码：
如果两个文件相同，会输出True，否则会输出false。
'''
