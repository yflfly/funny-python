# coding:utf-8
class Tag:
    def __init__(self):
        self.change = {'python': 'This is python'}

    def __getitem__(self, item):
        print('这个方法被调用')
        return self.change[item]


a = Tag()
print(a['python'])

'''
打印结果如下所示：
这个方法被调用
This is python
'''