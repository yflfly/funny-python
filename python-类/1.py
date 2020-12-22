# coding:utf-8
'''
在学习python代码时，看到有的类的方法中第一参数是cls，有的是self，
经过了解得知，python并没有对类中方法的第一个参数名字做限制，可以是self，也可以是cls，
不过根据人们的惯用用法，self一般是在实例方法中使用，而cls则一般在类方法中使用，
在静态方法中则不需要使用一个默认参数，其实这个默认参数可以换成任何一个名字代替，不会产生任何影响。
'''

'''
在下面的代码中，InstanceMethod类的方法中，第一个参数是默认的self，
在这里可以把self换成任何名字来表示，不会有任何影响。
'''


class InstanceMethod(object):
    pass

    def __init__(self, a):
        self.a = a

    def f1(self):
        print('This is {0}.'.format(self))

    # def f2(self,a):
    def f2(qq, a):
        print('Value:{0}'.format(a))
        print(qq.a)


if __name__ == '__main__':
    im = InstanceMethod('233')
    im.f1()
    im.f2(233)
'''
输出结果：
This is <__main__.InstanceMethod object at 0x000001C7AE33ECF8>.
Value:233
233
'''
