# coding:utf-8
import re

text_string = '沈阳航空航天大学人工智能实验室，毕业生杨凤玲。已经毕业了。目前杨凤玲在航天科工进行工作。'
regex = '杨凤玲'
p_string = text_string.split('。')
for line in p_string:
    if re.search(regex, line) is not None:
        print(line)

'''
打印结果如下所示：
沈阳航空航天大学人工智能实验室，毕业生杨凤玲
目前杨凤玲在航天科工进行工作
'''