# coding:utf-8
import threading
import time


def run(n):
    print('task', n)
    time.sleep(1)
    print(n, '2s')
    time.sleep(1)
    print(n, '1s')
    time.sleep(1)
    print(n, '0s')
    time.sleep(1)


if __name__ == '__main__':
    # target是要执行的函数名（不是函数），args是函数对应的参数，以元组的形式存在
    t1 = threading.Thread(target=run, args=('t1',))
    t2 = threading.Thread(target=run, args=('t2',))
    t1.start()
    t2.start()
    '''
    输出的结果如下所示：
    task t1
    task t2
    t1 2s
    t2 2s
    t1 1s
    t2 1s
    t1 0s
    t2 0s
    '''
