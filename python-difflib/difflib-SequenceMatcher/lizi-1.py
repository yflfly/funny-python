# coding:utf-8
import difflib
from pprint import pprint

a = 'pythonclub.org is wonderful'
b = 'Pythonclub.org also wonderful'
# 构造SequenceMatcher类
s = difflib.SequenceMatcher(None, a, b)

# 得到相同的block
print("s.get_matching_blocks():")
pprint(s.get_matching_blocks())
print('---------------------------------------------')
print("s.get_opcodes():")
for tag, i1, i2, j1, j2 in s.get_opcodes():
    print("%7s a[%d:%d] (%s) b[%d:%d] (%s)" % (tag, i1, i2, a[i1:i2], j1, j2, b[j1:j2]))
    # 在此实现你的功能

'''
输出结果如下所示：
s.get_matching_blocks():
[Match(a=1, b=1, size=14),
 Match(a=16, b=17, size=1),
 Match(a=17, b=19, size=10),
 Match(a=27, b=29, size=0)]
---------------------------------------------
s.get_opcodes():
replace a[0:1] (p) b[0:1] (P)
  equal a[1:15] (ythonclub.org ) b[1:15] (ythonclub.org )
replace a[15:16] (i) b[15:17] (al)
  equal a[16:17] (s) b[17:18] (s)
 insert a[17:17] () b[18:19] (o)
  equal a[17:27] ( wonderful) b[19:29] ( wonderful)

'''