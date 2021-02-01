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

'''
解释：
s=difflib.SequenceMatcher(isjunk=None,a,b, autojunk=True) ：构造函数，主要创建任何类型序列的比较对象。
isjunk是关键字参数，主要设置过滤函数，如想丢掉a和b比较序列里特定的字符，就可以设置相应的函数

s.get_opcodes()函数每执行一次返回5个元素的元组，元组描述了a和b比较序列的相同不同处。
5个元素的元组表示为(tag, i1, i2, j1, j2)，其中tag表示动作，i1表示序列a的开始位置，i2表示序列a的结束位置，
j1表示序列b的开始位置，j2表示序列b的结束位置。

tag表示的字符串为：
replace 表示a[i1 : i2]将要被b[j1 : j2]替换。
delete  表示a[i1 : i2]将要被删除。
insert  表示b[j1 : j2]将被插入到a[i1 : i1]地方。
equal  表示a[i1 : i2] == b[j1 : j2]相同。

'''