import difflib


class DiffFile:
    """文件比较类"""

    @classmethod
    def _read_file(cls, file):
        """
        读取文件内容，以列表形式返回
        :param file: 文件路径
        :return:
        """
        try:
            with open(file, "rb") as fp:
                # 二进制方式读取文件内容，并转换为str类型
                lines = fp.read().decode('utf-8')
                # 按行进行分割
                text = lines.splitlines()
                # print text
                return text
        except Exception as e:
            print("ERROR: %s" % str(e))

    @classmethod
    def compare_file(cls, file1, file2, out_file):
        """
        比较文件，生成html格式
        :param file1: 第1个文件路径
        :param file2: 第2个文件路径
        :param out_file: 比较结果文件路径
        :return:
        """
        file1_content = cls._read_file(file1)
        file2_content = cls._read_file(file2)
        compare = difflib.HtmlDiff()
        compare_result = compare.make_file(file1_content, file2_content)
        with open(out_file, 'w', encoding='utf-8') as fp:
            fp.writelines(compare_result)


if __name__ == '__main__':
    DiffFile.compare_file('data/ceshi1.txt', "data/ceshi2.txt", 'data/res_diff.html')
