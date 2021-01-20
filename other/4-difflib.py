# coding:utf-8
import difflib

input_and_output = [1, 2, '你好', '世界', 12.34, 45.6, -21, '中国', '美丽']

test1 = ['你好', '我是谁']
test2 = ['你好啊', '我谁']
test3 = [12, 'nihao']
test4 = ['你好', 'woshi']

print(difflib.SequenceMatcher(a=test1, b=test2).quick_ratio())
print(difflib.SequenceMatcher(a=test1, b=test4).ratio())

'''
输出结果：
0.0
0.5
'''