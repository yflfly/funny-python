from difflibparser import *

file1 = '''
line1
lineTwo
lineThrees
line4
line6
'''

file2 = '''
line1
xlineTw0
lineThree
line4
line66
'''

diff = difflib.ndiff(file1.splitlines(), file2.splitlines())
for line in diff:
    print(line)

print('---------\n')

differ = DifflibParser(file1.splitlines(), file2.splitlines())

for line in differ:
    print(line)

'''
{'line': '', 'code': 0}
{'line': 'line1', 'code': 0}
{'line': 'lineTwo', 'code': 3, 'leftchanges': [6], 'rightchanges': [0, 7], 'newline': 'xlineTw0'}
{'line': 'lineThrees', 'code': 3, 'leftchanges': [9], 'rightchanges': [], 'newline': 'lineThree'}
{'line': 'line4', 'code': 0}
{'line': 'line6', 'code': 3, 'leftchanges': [], 'rightchanges': [5], 'newline': 'line66'}
'''