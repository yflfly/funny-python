# coding:utf-8

print('a' * 20 is 'aaaaaaaaaaaaaaaaaaaa')
print('a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa')
'''
输出结果：
True
False

是不是很神奇？？
'''

print('a' * 20 == 'aaaaaaaaaaaaaaaaaaaa')
print('a' * 21 == 'aaaaaaaaaaaaaaaaaaaaa')
'''
True
True
嗯？？？一脸问号
'''

print(id('a' * 20), id('aaaaaaaaaaaaaaaaaaaa'))
print(id('a' * 21), id('aaaaaaaaaaaaaaaaaaaaa'))
'''
2459422467464 2459422467464
2459422467320 2459422466744
'''

'''
所以 is 比较的是字符串的 id
用is判断两个字符串是不靠谱滴，慎用
'''
