# coding:utf-8
import docx
import os, shutil
import subprocess
import collections


def convert_files(inner_path):  # 将doc文件修改成docx文件
    if os.path.splitext(inner_path)[-1] == '.doc':
        if not os.path.isfile(os.path.splitext(inner_path)[0] + '.docx'):
            output_path = inner_path.split(os.path.basename(inner_path))[0]
            subprocess.call(['soffice', '--headless', '--convert-to', 'docx', inner_path, "--outdir",
                             output_path,])
        filepath = os.path.splitext(inner_path)[0] + '.docx'
    else:
        filepath = inner_path
    print(filepath)


# dir_path: 文件所在路径， old_file: 原来文件名字， new_file: 改变的文件名字
def re_name(dir_path, old_file, new_file):
    os.renames(os.path.join(dir_path, old_file), os.path.join(dir_path, new_file))


def copy_files(path, file_name):  # 定义函数名称
    new_name = file_name.replace('.doc', '_new.doc')  # 为文件赋予新名字
    shutil.copyfile(os.path.join(path, file_name), os.path.join(path, new_name))  # 复制并重命名文件


def analysis_word(filepath):
    doc = docx.Document(filepath)
    doc_content = []
    for paragraph in doc.paragraphs:
        if paragraph.text.split():
            doc_content.append(paragraph.text)
    print('\n'.join(doc_content))


if __name__ == '__main__':
    path1 = '/data/word_contract/test.doc'
    convert_files(path1)

    # path = os.getcwd()
    # print(path)
    # path1 = '/data/word_contract'
    # # copy_files(path1, "update.doc")
    # # re_name(path1, "update_new.doc", "update_new.docx")
    # analysis_word(os.path.join(path1, "update_new.docx"))

# path1 = '/data/person/yfl/test.doc'
# print(os.path.basename(path1))
'''


'''
