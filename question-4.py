# coding:utf-8

row = [''] * 3
board = [row] * 3
print(board)
'''
输出：
[['', '', ''], ['', '', ''], ['', '', '']]

这有啥值得展示的吗？
别急，继续看
'''
board[0][0] = 'X'
print(board)
'''
你是不是想说结果是这个：
[['X', '', ''], ['', '', ''], ['', '', '']]

哈哈哈哈，我就是猜到了

其实输出是这个样子的：
[['X', '', ''], ['X', '', ''], ['X', '', '']]

别急，解释来了：
这是因为[row] * 3这个操作实际上没有复制row，而只是创建了三个object reference，也就是board[0] board[1] board[2]这三个元素其实指向了同一个列表row，那么改变board[0][0]其实就是改变row[0]，也同时改变了board[1][0] board[2][0]。
'''
