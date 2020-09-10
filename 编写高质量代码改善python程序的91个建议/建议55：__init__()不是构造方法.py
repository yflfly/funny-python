# coding:utf-8

class A(object):
    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args)
        print(kwargs)
        print('------------------')
        instance = object.__new__(cls, *args, **kwargs)
        print(instance)

    def __init__(self, a, b):
        print('init gets called')
        print('self is', self)
        self.a = a
        self.b = b


a1 = A(1, 2)
print(a1.a, a1.b)
