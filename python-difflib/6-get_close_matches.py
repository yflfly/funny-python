# coding:utf-8
import difflib

print(difflib.get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy']))

'''
输出结果为：
['apple', 'ape']

解释：
difflib.get_close_matches(word, possibilities, n=3, cutoff=0.6)
返回由最佳“近似”匹配构成的列表。 word 为一个指定目标近似匹配的序列（通常为字符串），
possibilities 为一个由用于匹配 word 的序列构成的列表（通常为字符串列表）。
'''
