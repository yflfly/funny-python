from difflibparser import *

file1 = '''
1. 中文自然语言处理
2. 自然语言处理哈
3. 自然语言处理NLP
5. 哈哈哈哈
'''

file2 = '''
1. 中文自然语言处理
2. 自然语言处理
4. 哈喽自然语言处理
5. 哈哈哈哈
'''

diff = difflib.ndiff(file1.splitlines(), file2.splitlines())
# for line in diff:
#     print(line)

print('---------\n')

differ = DifflibParser(file1.splitlines(), file2.splitlines())

for line in differ:
    print(line)

'''
输出结果如下所示：
{'line': '', 'code': 0}
{'line': '1. 中文自然语言处理', 'code': 0}
{'line': '2. 自然语言处理哈', 'code': 3, 'leftchanges': [9], 'rightchanges': [], 'newline': '2. 自然语言处理'}
{'line': '3. 自然语言处理NLP', 'code': 2}
{'line': '4. 哈喽自然语言处理', 'code': 1}
{'line': '5. 哈哈哈哈', 'code': 0}

'''