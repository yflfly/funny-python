# coding:utf-8
import difflib

print(difflib.get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'], n=3, cutoff=0.2))

'''
输出结果为：
['apple', 'ape', 'puppy']

解释：
difflib.get_close_matches(word, possibilities, n=3, cutoff=0.6)
返回由最佳“近似”匹配构成的列表。 word 为一个指定目标近似匹配的序列（通常为字符串），
possibilities 为一个由用于匹配 word 的序列构成的列表（通常为字符串列表）。

可选参数 n (默认为 3) 指定最多返回多少个近似匹配； n 必须大于 0.
可选参数 cutoff (默认为 0.6) 是一个 [0, 1] 范围内的浮点数。 与 word 相似度得分未达到该值的候选匹配将被忽略。
候选匹配中（不超过 n 个）的最佳匹配将以列表形式返回，按相似度得分排序，最相似的排在最前面。
'''
str_1 = '自然语言处理'
candi_list = ['自然语言处理', '语言处理', '我爱自然语言处理', '自然语言处理简称为NLP']
print(difflib.get_close_matches(str_1, candi_list, n=3, cutoff=0.5))
'''
输出结果如下所示：
['自然语言处理', '我爱自然语言处理', '语言处理']
'''
