# -*- encoding: utf-8 -*-
"""
@File    : diff.py
@Time    : 2020-09-20
@Author  : kongsh
"""

import difflib


class DiffFile:

    @classmethod
    def compare_text(cls, src_text, target_text):
        """
        比较给定的2个字符串
        :param src_text:
        :param target_text:
        :return:
        """
        d = difflib.Differ()
        return "".join(list(d.compare(src_text, target_text)))

    @classmethod
    def compare_text_to_file(cls, src_text, target_text, out_file):
        """
        比较给定的2个字符串，生成html格式
        :param src_text:
        :param target_text:
        :param out_file:
        :return:
        """
        compare = difflib.HtmlDiff()
        compare_result = compare.make_file(src_text, target_text)
        with open(out_file, 'w', encoding='utf-8') as fp:
            fp.writelines(compare_result)


if __name__ == '__main__':
    text1 = '''
    1. 中文自然语言处理
    2. 自然语言处理哈
    3. 自然语言处理NLP
    4. 自然语言处理
         '''.splitlines(keepends=True)

    text2 = '''
    1. 中文自然语言处理
    2. 自然语言处理
    3. 自然语言处理NLP
    4. 哈喽自然语言处理
         '''.splitlines(keepends=True)
    print(DiffFile.compare_text_to_file(text1, text2, 'data/text_diff.html'))
