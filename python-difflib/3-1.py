import difflib
import codecs

# ['', '1 line', '2 line']
text1 = '''  
    1. Beautiful is better than ugly.
    2. Explicit is better than implicit.
    3. Simple is better than complex.
    4. Complex is better than complicated.
'''.splitlines(keepends=True)

text2 = '''  
    1. Beautifu  is better than ugly.
    2. Explicit is better than implicit.
    3. Simple is better than complex.
    4. Complex is better than complicated.
'''.splitlines(keepends=True)

# 1. 以字符串方式展示两个文本的不同， 效果如下:
d = difflib.Differ()
result = list(d.compare(text1, text2))
result = " ".join(result)
print(result)
"""
 -     1. Beautiful is better than ugly.
 ?                ^
 +     1. Beautifu  is better than ugly.
 ?                ^
       2. Explicit is better than implicit.
       3. Simple is better than complex.
       4. Complex is better than complicated.
"""

# 2. 以html方式展示两个文本的不同， 浏览器打开:
d = difflib.HtmlDiff()
with codecs.open("data/diff.html", 'w', 'utf-8') as f:
    f.write(d.make_file(text1, text2))

'''
各个差异符号表示含义:
'-':包含在第一个序列行中，不包含在第二个序列行中
'+':包含在第二个序列行中，不包含在第一个序列行中
'':两个序列行一致
'?':标志两个序列行存在增量差异
'^':标志出两个序列存在的差异字符
'''
