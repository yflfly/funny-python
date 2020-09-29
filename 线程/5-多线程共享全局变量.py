# coding:utf-8
import time
import threading

'''
    多线程共享全局变量
    线程是进程的执行单元，进程是系统分配资源的最小执行单位，所以在同一个进程中的多线程是共享资源的
'''
g_num = 100


def work1():
    global g_num
    for i in range(3):
        g_num += 1
    print('in work1 g_num is : %d' % g_num)


def work2():
    global g_num
    print('in work2 g_num is : %d' % g_num)


if __name__ == '__main__':
    t1 = threading.Thread(target=work1)
    t1.start()
    time.sleep(1)
    t2 = threading.Thread(target=work2)
    t2.start()
    '''
    输出结果如下所示：
    in work1 g_num is : 103
    in work2 g_num is : 103
    '''
