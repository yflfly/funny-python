import difflib
import codecs

# ['', '1 line', '2 line']
text1 = '''1. 中文自然语言处理
    2. 自然语言处理哈
    3. 自然语言处理NLP
    5. 哈哈哈哈'''.splitlines(keepends=True)

text2 = '''1. 中文自然语言处理
    2. 自然语言处理
    4. 哈喽自然语言处理
    5. 哈哈哈哈'''.splitlines(keepends=True)

# 1. 以字符串方式展示两个文本的不同， 效果如下:
d = difflib.Differ()
result = list(d.compare(text1, text2))
result = " ".join(result)
print(result)

# 2. 以html方式展示两个文本的不同， 浏览器打开:
d = difflib.HtmlDiff()
with codecs.open("data/diff-zhongwen.html", 'w', 'utf-8') as f:
    f.write(d.make_file(text1, text2))


'''
讲解说明：
class difflib.HtmlDiff类：可用于创建HTML表格(或包含表格的完整HTML文件)以并排地逐行显示比较文本，
行间与2行外的更改将突出显示。此表格可以基于完全或上下文差异模式来生成。
'''