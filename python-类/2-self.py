# coding:utf-8
'''
这个self到底是什么呢？
'''


class Calc(object):
    def add(self, x, y):
        print(x + y)
        print(self)


if __name__ == '__main__':
    calc = Calc()
    calc.add(1, 1)
    print(calc)
'''
运行结果：
2
<__main__.Calc object at 0x00000146F719ECC0>
<__main__.Calc object at 0x00000146F719ECC0>

解释：
可以看的出来，这个self和实例化出来的calc都是Calc这个对象，并且指向的内存地址是同一个，
也就是他们两个是同一个东西。
'''