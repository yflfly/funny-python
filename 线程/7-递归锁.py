# coding:utf-8
import time
import threading

'''
    递归锁：RLcok类的用法和Lock类一模一样，但它支持嵌套，在多个锁没有释放的时候一般会使用RLock类
'''


def func(lock):
    global gl_num
    lock.acquire()
    gl_num += 1
    time.sleep(1)
    print(gl_num)
    lock.release()


if __name__ == '__main__':
    gl_num = 0
    lock = threading.RLock()
    for i in range(10):
        t = threading.Thread(target=func, args=(lock,))
        t.start()
    '''
    输出结果如下所示：
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    '''
