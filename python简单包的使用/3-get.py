# coding:utf-8
'''
描述
Python 字典 get() 函数返回指定键的值。

语法
get()方法语法：

dict.get(key, default=None)
参数
key -- 字典中要查找的键。
default -- 如果指定的键不存在时，返回该默认值。
返回值
返回指定键的值，如果键不在字典中返回默认值 None 或者指定的默认值。

'''
dict = {'Name': 'Runoob', 'Age': 27}

print ("Age 值为 : %s" %  dict.get('Age'))
print ("Sex 值为 : %s" %  dict.get('Sex', "NA"))