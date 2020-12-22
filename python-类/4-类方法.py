# coding:utf-8
'''
在Python中还有一个方法@classmethod，使用了这个方法，传入的第一个参数就不是self，而是cls
'''


class Calc(object):
    def add(self, x, y):
        print(x + y)

    @staticmethod
    def minus(x, y):
        print(x - y)

    @classmethod
    def multi(cls, x, y):
        print(x * y)
        print('cls is', cls)


if __name__ == '__main__':
    print('Calc', Calc)
    calc = Calc()
    print('calc', calc)
    calc.add(1, 1)  # 2
    Calc.minus(3, 2)  # 1
    calc.multi(2, 2)  # 4
'''
运行的结果如下所示：
Calc <class '__main__.Calc'>
calc <__main__.Calc object at 0x00000218309CA358>
2
1
4
cls is <class '__main__.Calc'>

解释：
由运行的结果可以看出来，cls与类本身的输出的结果一样
'''
