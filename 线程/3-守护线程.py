# coding:utf-8
import time
import threading

'''
    守护线程
    下面这个例子，这里使用setDaemon(True)把所有的子线程都变成了主线程的守护线程，
    因此当主线程结束后，子线程也会随之结束，所以当主线程结束后，整个程序就退出了。
    所谓’线程守护’，就是主线程不管该线程的执行情况，只要是其他子线程结束且主线程执行完毕，主线程都会关闭。也就是说:主线程不等待该守护线程的执行完再去关闭。
'''


def run(n):
    print('task', n)
    time.sleep(1)
    print(n, '3s')
    time.sleep(1)
    print(n, '2s')
    time.sleep(1)
    print(n, '1s')


if __name__ == '__main__':
    t = threading.Thread(target=run, args=('t1',))
    t.setDaemon(True)
    t.start()
    print('end')
    '''
    输出结果如下所示：
    task t1
    end
    '''
    '''
        通过执行结果可以看出，设置守护线程之后，当主线程结束时，子线程也将立即结束，不再执行
    '''
