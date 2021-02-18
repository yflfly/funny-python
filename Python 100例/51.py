#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
学习使用按位与 &
'''
if __name__ == '__main__':
    a = 0x77
    b = a & 3
    print('a & b = %d' % b)
    b &= 7
    print('a & b = %d' % b)