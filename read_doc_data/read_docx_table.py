import os
import docx

from docx.document import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph


def iter_block_items(parent):
    """
    Yield each paragraph and table child within *parent*, in document order.
    Each returned value is an instance of either Table or Paragraph. *parent*
    would most commonly be a reference to a main Document object, but
    also works for a _Cell object, which itself can contain paragraphs and tables.
    """
    if isinstance(parent, Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


def read_table(table):
    # return [[cell.text for cell in row.cells] for row in table.rows]
    res_list = []

    for row in table.rows:
        list1 = []
        for cell in row.cells:
            if cell.text not in list1:
                list1.append(cell.text)
        res_list.append(list1)
    return res_list


def read_word(word_path):
    all_para = []
    doc = docx.Document(word_path)
    for block in iter_block_items(doc):
        if isinstance(block, Paragraph):
            para = block.text
            print("text", [para])
            if para:
                all_para.append(block.text)
        elif isinstance(block, Table):
            list1 = read_table(block)
            for each in list1:
                all_para.append(''.join(each))
            print("table", list1)
    return all_para


if __name__ == '__main__':
    # ROOT_DIR_P = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # 项目根目录
    # word_path = os.path.join(ROOT_DIR_P, "update.docx")  # pdf文件路径及文件名
    # word_path = os.path.join(ROOT_DIR_P, "data/test_to_word2.docx")  # pdf文件路径及文件名
    # read_word(word_path)
    res_list = read_word('update.docx')
    print('*' * 100)
    for each in res_list:
        print('each', each)
