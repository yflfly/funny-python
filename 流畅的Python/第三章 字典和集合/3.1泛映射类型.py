# coding:utf-8
import collections

my_dict = {}
print(collections.abc.Mapping)
print(isinstance(my_dict, collections.abc.Mapping))

'''
输出结果：
<class 'collections.abc.Mapping'>
True

这里用isinstance而不是type来检查某个参数是否为dict类型，因为这个参数有可能不是dict，而是一个比较另类的映射类型。

标准库里的所有映射类型都是利用dict来实现的，因此它们有个共同的限制，
即只有可散列的数据类型才能用作这些映射里的键（只有键有这个要求，值并不需要是可散列的数据类型）
'''
