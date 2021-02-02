# coding:utf-8
import difflib

l = len('X this is a test')
matcher = difflib.SequenceMatcher(None, "X this is a test", "this is a test X")
print(matcher.find_longest_match(0, l, 0, l))

'''
输出结果如下所示:
Match(a=2, b=0, size=14)
'''
