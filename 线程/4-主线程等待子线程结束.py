# coding:utf-8
import time
import threading

'''
    主线程等待子线程结束
    为了让守护线程执行结束之后，主线程再结束，我们可以使用join方法，让主线程等待子线程执行
'''


def run(n):
    print('task', n)
    time.sleep(2)
    print(n, '5s')
    time.sleep(2)
    print(n, '3s')
    time.sleep(2)
    print(n, '1s')


if __name__ == '__main__':
    t = threading.Thread(target=run, args=('t1',))
    t.setDaemon(True)  # 把子线程设置为守护线程，必须在start()之前设置
    t.start()
    t.join()  # 设置主线程等待子线程结束
    print('end')
    '''
    输出结果如下所示：
    task t1
    t1 5s
    t1 3s
    t1 1s
    end
    '''
