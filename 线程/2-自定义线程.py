# coding:utf-8
import time
import threading

'''
    自定义线程：继承threading.Thread来定义线程类，其本质是重构Thread类中的run方法
'''


class MyThread(threading.Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()  # 重构run函数必须写
        self.n = n

    def run(self):
        print('task', self.n)
        time.sleep(1)
        print(self.n, '2s')
        time.sleep(1)
        print(self.n, '1s')
        time.sleep(1)
        print(self.n, '0s')
        time.sleep(1)


if __name__ == '__main__':
    t1 = MyThread('t1')
    t2 = MyThread('t2')
    t1.start()
    t2.start()
    '''
    输出结果如下所示：
    task t1
    task t2
    t1 2s
    t2 2s
    t1 1s
    t2 1s
    t1 0s
    t2 0s
    '''
