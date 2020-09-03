# coding:utf-8
import traceback

list1 = [1, 2, 3]


def f():
    return list1[5]


try:
    f()
except:
    print('出现了错误')

'''
输出的结果为：
出现了错误

仅仅有错误的输出，但是具体哪行代码出现了问题，无法定位，且具体的什么错误也未知
'''

try:
    f()
except:
    print('sorry 出现了错误')
    traceback.print_exc()

'''
traceback模块可以解决错误定位问题，它会输出完整的栈信息
输出的结果如下所示：
Traceback (most recent call last):
  File "D:/Download/funny-python/编写高质量代码改善python程序的91个建议/建议46：使用traceback获取栈信息.py", line 23, in <module>
    f()
  File "D:/Download/funny-python/编写高质量代码改善python程序的91个建议/建议46：使用traceback获取栈信息.py", line 7, in f
sorry 出现了错误
    return list1[5]
IndexError: list index out of range
'''
'''
程序运行会输出完整的栈信息，包括调用顺序、异常发生的语句、错误类型等等
traceback.print_exc()方法打印出的信息包括3部分：错误类型、错误对应的值、具体的trace信息，包括文件名、具体的行号、函数名以及对应的源代码
'''
