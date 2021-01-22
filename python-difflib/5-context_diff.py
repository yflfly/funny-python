# coding:utf-8
import difflib

text1 = '''  
    1. 中文自然语言处理
    2. 自然语言处理哈
    3. 自然语言处理NLP
    4. 自然语言处理
'''.splitlines(keepends=True)

text2 = '''  
    1. 中文自然语言处理
    2. 自然语言处理
    3. 自然语言处理NLP
    4. 哈喽自然语言处理
'''.splitlines(keepends=True)

# for line in difflib.context_diff(text1, text2):
#     print(line)

diff = difflib.ndiff(text1, text2)
print(''.join(diff))
