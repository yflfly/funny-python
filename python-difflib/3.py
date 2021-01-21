#!/user/bin/python
# -*- coding: utf-8 -*-
# 2017-9-13
import sys
import difflib
import argparse


# 读取配置文件函数
def read_file(file_name):
    try:
        file_handle = open(file_name, 'r', encoding='utf-8')
        text = file_handle.read().splitlines()  # 读取后以行进行分割
        file_handle.close()
        return text
    except IOError as error:
        print('Read file Error: {0}'.format(error))
        sys.exit()


# 比较两个文件并输出html格式的结果
def compare_file(file1_name, file2_name):
    if file1_name == "" or file2_name == "":
        print('文件路径不能为空：file1_name的路径为：{0}, file2_name的路径为：{1} .'.format(file1_name, file2_name))
        sys.exit()
    text1_lines = read_file(file1_name)
    print(text1_lines)
    text2_lines = read_file(file2_name)
    print(text2_lines)
    diff = difflib.Differ()  # 创建htmldiff 对象
    result = list(diff.compare(text1_lines, text2_lines))
    print('\n'.join(result))


if __name__ == "__main__":
    file1_name = 'data/ceshi1.txt'
    file2_name = 'data/ceshi2.txt'

    compare_file(file1_name, file2_name)

'''
Differ比较之后显示的规则如下： 
1）一行前面有-号是出现在第一个版本，不出现在第二个版本。 
2）一行前面有+号是出现在第二个版本，不出现在第一个版本。 
3）如果一行里有变化，就会在后面的另外一行里增加一个？显示，并且在这行里显示+或-。 
4）如果一行没有变化，就会在一行前面输出一个空格，以便对齐。
'''
