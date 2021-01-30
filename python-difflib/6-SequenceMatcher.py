# coding:utf-8
import difflib

s1 = '''1. 中文自然语言处理
    2. 自然语言处理哈
    3. 自然语言处理NLP
    5. 哈哈哈哈'''.splitlines(keepends=True)
s2 = '''1. 中文自然语言处理
    2. 自然语言处理
    4. 哈喽自然语言处理
    5. 哈哈哈哈'''.splitlines(keepends=True)

print('Initial data:')
print('s1 =', s1)
print('s2 =', s2)
print('s1 == s2:', s1 == s2)
print()

matcher = difflib.SequenceMatcher(None, s1, s2)
# for tag, i1, i2, j1, j2 in reversed(matcher.get_opcodes()):
for tag, i1, i2, j1, j2 in matcher.get_opcodes():
    print(11111, tag, i1, i2, j1, j2)

    if tag == 'delete':
        print('Remove {} from positions [{}:{}]'.format(
            s1[i1:i2], i1, i2))
        print('  before =', s1)
        del s1[i1:i2]

    elif tag == 'equal':
        print('s1[{}:{}] and s2[{}:{}] are the same'.format(
            i1, i2, j1, j2))

    elif tag == 'insert':
        print('Insert {} from s2[{}:{}] into s1 at {}'.format(
            s2[j1:j2], j1, j2, i1))
        print('  before =', s1)
        s1[i1:i2] = s2[j1:j2]

    elif tag == 'replace':
        print(('Replace {} from s1[{}:{}] '
               'with {} from s2[{}:{}]').format(
            s1[i1:i2], i1, i2, s2[j1:j2], j1, j2))
        print('  before =', s1)
        s1[i1:i2] = s2[j1:j2]

    print('   after =', s1, '\n')

print('s1 == s2:', s1 == s2)
print(matcher.get_opcodes())
