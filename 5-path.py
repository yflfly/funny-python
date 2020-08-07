# coding:utf-8
import os

print(os.path.abspath(__file__))


'''
输出结果：
D:\Download\funny-python\5-path.py

作用：
获取当前脚本的完整路径
'''

print(os.path.basename(__file__))
'''
输出结果：
5-path.py

作用:
返回当前脚本的文件名
'''

'''
关于os.path()模块的使用可以参考下面网址：
https://www.runoob.com/python/python-os-path.html
'''