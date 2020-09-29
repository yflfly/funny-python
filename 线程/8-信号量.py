# coding:utf-8
import time
import threading

'''
    信号量（BoundedSemaphore类）
    互斥锁同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据，比如厕所有3个坑，
    那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去
'''


def run(n, semaphore):
    semaphore.acquire()  # 加锁
    time.sleep(3)
    print('run the thread:%s\n' % n)
    semaphore.release()  # 释放


if __name__ == '__main__':
    num = 0
    semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
    for i in range(22):
        t = threading.Thread(target=run, args=('t-%s' % i, semaphore))
        t.start()
    while threading.active_count() != 1:
        pass
    else:
        print('----------all threads done-----------')
'''
输出结果如下所示：
run the thread:t-1
run the thread:t-0

run the thread:t-2
run the thread:t-4


run the thread:t-3


run the thread:t-5

run the thread:t-7
run the thread:t-6


run the thread:t-8
run the thread:t-9


run the thread:t-11
run the thread:t-10
run the thread:t-12



run the thread:t-13

run the thread:t-14

run the thread:t-15

run the thread:t-16

run the thread:t-17

run the thread:t-19

run the thread:t-18

run the thread:t-20
run the thread:t-21


----------all threads done-----------
'''