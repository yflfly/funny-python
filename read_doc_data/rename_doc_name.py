# coding:utf-8
import os, shutil


# dir_path: 文件所在路径， old_file: 原来文件名字， new_file: 改变的文件名字
def re_name(dir_path, old_file, new_file):
    os.renames(os.path.join(dir_path, old_file), os.path.join(dir_path, new_file))


def copy_files(path, file_name):  # 定义函数名称
    new_name = file_name.replace('.doc', '_new.doc')  # 为文件赋予新名字
    shutil.copyfile(os.path.join(path, file_name), os.path.join(path, new_name))  # 复制并重命名文件


if __name__ == '__main__':
    path1 = '/data/word_contract'
    copy_files(path1, "update.doc")  # 先对文件进行copy并修改名字
    re_name(path1, "update_new.doc", "update_new.docx")  # 强制修改文件的后缀名字
