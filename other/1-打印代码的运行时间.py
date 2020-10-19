# coding:utf-8
import time
import datetime
import timeit

# method1
# python 的标准库手册推荐在任何情况下尽量使用time.clock().
# 只计算了程序运行CPU的时间，返回值是浮点数
start = time.clock()
# 中间写上代码块
end = time.clock()
print('Running time: %s Seconds' % (end - start))

# method2
# 该方法包含了其他程序使用CPU的时间，返回值是浮点数
start = time.time()
# 中间写上代码块
end = time.time()
print('Running time: %s Seconds' % (end - start))

# method3
# 该方法包含了其他程序使用CPU的时间
start = datetime.datetime.now()
# 中间写代码块
end = datetime.datetime.now()
print('Running time: %s Seconds' % (end - start))

# method4
# 在 Unix 系统中，建议使用 time.time()，在 Windows 系统中，建议使用 time.clock()
# 实现跨平台的精度性可以使用timeit.default_timer()
start = timeit.default_timer()
# 中间写代码块
end = timeit.default_timer()
print('Running time: %s Seconds' % (end - start))
