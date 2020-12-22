# coding:utf-8
'''
在看别人的代码的时候，经常会看到一个@staticmethod。这个东西是静态方法，在类中的方法都必须要传self对象，
但是一旦被@staticmethod装饰器装饰后的方法，就不需要传入self这个参数
'''


class Calc(object):
    def add(self, x, y):
        print(x + y)

    @staticmethod
    def minus(x, y):
        print(x - y)


if __name__ == '__main__':
    calc = Calc()
    calc.add(1, 1)
    Calc.minus(3, 2)

'''
在Python这个装饰器只是一个基于类设计的一个方法。你用一个def来实现，或者就用类方法来实现影响其实并不大。
当然，你实例化了，也是可以通过实例来调用静态方法的。
'''
