# coding:utf-8
import pycorrector

pycorrector.set_log_level('INFO')
error_sentences = [
    '买iPhone差，要多少钱',
    '共同实际控制人萧华、霍荣铨、张旗康',
]
for line in error_sentences:
    print(pycorrector.correct(line))

print('*' * 53)
pycorrector.set_custom_confusion_dict(path='data/my_custom_confusion.txt')
for line in error_sentences:
    print(pycorrector.correct(line))
