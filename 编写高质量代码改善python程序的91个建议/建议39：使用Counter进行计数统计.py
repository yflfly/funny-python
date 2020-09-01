# coding:utf-8

# 1、使用dict  P108页
some_data = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
count_frq = dict()
for item in some_data:
    if item in count_frq:
        count_frq[item] += 1
    else:
        count_frq[item] = 1
print(count_frq)
'''
输出结果如下所示：
{'a': 3, '2': 2, 2: 1, 4: 2, 5: 2, 'b': 1, 7: 1, 'd': 1, 'z': 1}
'''

# 2、使用defaultdict
from collections import defaultdict

count_frq_1 = defaultdict(int)
print(count_frq_1)
for item in some_data:
    count_frq_1[item] += 1
print(count_frq_1)
'''
输出结果如下所示：
defaultdict(<class 'int'>, {})
defaultdict(<class 'int'>, {'a': 3, '2': 2, 2: 1, 4: 2, 5: 2, 'b': 1, 7: 1, 'd': 1, 'z': 1})
'''

# 3、使用set和list
count_set = set(some_data)
count_list = []
for item in count_set:
    count_list.append((item, some_data.count(item)))
print(count_list)
'''
输出结果如下所示：
[('d', 1), (2, 1), (4, 2), (5, 2), ('2', 2), (7, 1), ('b', 1), ('a', 3), ('z', 1)]
'''

# 4、Counter
from collections import Counter

print(Counter(some_data))

'''
输出结果如下所示：
Counter({'a': 3, '2': 2, 4: 2, 5: 2, 2: 1, 'b': 1, 7: 1, 'd': 1, 'z': 1})
'''
print(Counter('success'))  # 可迭代对象
print(Counter(s=3, c=2, e=1, u=1))  # 关键字参数
print(Counter({'s': 3, 'c': 2, 'e': 1, 'u': 1}))  # 字典
'''
输出结果如下所示：
Counter({'s': 3, 'c': 2, 'u': 1, 'e': 1})
Counter({'s': 3, 'c': 2, 'e': 1, 'u': 1})
Counter({'s': 3, 'c': 2, 'e': 1, 'u': 1})
'''
# 使用elements()方法来获取Counter中的key值
print(list(Counter(some_data).elements()))
'''
['a', 'a', 'a', '2', '2', 2, 4, 4, 5, 5, 'b', 7, 'd', 'z']
'''
print(Counter(some_data).most_common(2))
'''
利用most_common()方法可以找出前N个出现频率最高的元素以及它们对应的次数
输出结果如下所示：
[('a', 3), ('2', 2)]
'''
