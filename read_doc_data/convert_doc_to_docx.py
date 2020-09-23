# coding:utf-8
import docx
import os
import subprocess
import collections


def convert_files(inner_path):  # 将doc文件修改成docx文件
    if os.path.splitext(inner_path)[-1] == '.doc':
        if not os.path.isfile(os.path.splitext(inner_path)[0] + '.docx'):
            output_path = inner_path.split(os.path.basename(inner_path))[0]
            subprocess.call(['soffice', '--headless', '--convert-to', 'docx', inner_path, "--outdir",
                             output_path])
        filepath = os.path.splitext(inner_path)[0] + '.docx'
    else:
        filepath = inner_path
    print(filepath)


path1 = '/data/person/yfl/test.doc'
convert_files(path1)


'''
说明：
在Linux环境下，.doc文件的包暂时未找到，可以将其转换成.docx文件，再对应的进行文件的读取
'''