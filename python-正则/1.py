# coding:utf-8
import re

# \u4E00-\u9FA5a-zA-Z0-9+#&\._ : All non-space characters. Will be handled with re_han
# \r\n|\s : whitespace characters. Will not be handled.
re_han = re.compile("([\u4E00-\u9F5a-zA-Z0-9+#&]+)", re.U)
re_skip = re.compile("(\r\n\\s)", re.U)


def split_2_short_text(text, include_symbol=False):
    """
    长句切分为短句
    :param text: str
    :param include_symbol: bool
    :return: (sentence, idx)
    """
    result = []
    blocks = re_han.split(text)
    print(blocks)
    start_idx = 0
    for blk in blocks:
        if not blk:
            continue
        if include_symbol:
            result.append((blk, start_idx))
        else:
            if re_han.match(blk):
                result.append((blk, start_idx))
        start_idx += len(blk)
    return result


text = '我爱自然语言处理，你呢AA哈哈哈'
result = split_2_short_text(text)
print(result)
