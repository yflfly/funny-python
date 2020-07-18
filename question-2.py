# coding:utf-8

def function_1():
    try:
        return '嘻嘻'
    except:
        return '哈哈'


print(function_1())
'''
输出结果：
嘻嘻
嗯，对呀，结果就是这个
'''

def function_2():
    try:
        return '嘻嘻'
    except:
        return '哈哈'
    finally:
        return '什么鬼'


print(function_2())
'''
输出：
什么鬼

emmmmmm，确实是“什么鬼”

大段的原因：
一般的Python教程会告诉你，当函数执行到第一个return的时候会退出，剩下的语句不再执行。然而如果是这样的话上面的代码中我们的somefunc()应该返回的是'from_try'，但结果却不是。这个现象的原因是finally后面的语句永远会执行，而函数的返回值由最后一个return语句决定，所以函数的返回值是finally语句中的返回值。
'''