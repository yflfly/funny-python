# coding:utf-8
import win32com.client as wc

cur_file = r'D:\Download\funny-python\read_doc_data\购销合同（百货）.doc'

'''
读取word文档中的数据格式
'''
# doc 转 txt 传入doc文件的路径，路径必须是绝对路径且返回
def doc2txt(file_path, mw):
    try:
        doc = mw.Documents.Open(file_path)
        doc_content = [para.Range.Text for para in doc.Paragraphs]
        doc.Close()
        return '\n'.join(doc_content)
    except Exception as e:
        print(e)


# python 读取.doc文件
word = wc.Dispatch("Word.Application")
print(doc2txt(cur_file, word))
