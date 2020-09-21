# coding:utf-8
import docx

# docx 转 txt 传入doc文件的路径，路径必须是绝对路径且返回
def docx2txt(cur_file_docx):
    try:
        doc = docx.Document(cur_file_docx)
        doc_content = []
        for paragraph in doc.paragraphs:
            if paragraph.text.split():
                doc_content.append(paragraph.text)
        return '\n'.join(doc_content)
    except Exception as e:
        print(e)


cur_file_docx = r'D:/Download/funny-python/read_doc_data/1.docx'
print(docx2txt(cur_file_docx))
