# coding:utf-8
import datetime
from time import mktime

try:
    import simplejson as json
except:
    import json


class DateTimeEncoder(json.JSONEncoder):  # 对JSONEncoder进行扩展
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default(self, obj)


d = datetime.datetime.now()
print(json.dumps(d, cls=DateTimeEncoder))  # 使用cls指定编码器的名称

'''
输出的结果如下所示：
"2020-09-02 08:41:30"

JSON:JavaScript Object Notation，是一种轻量级数据交换格式，它基于JavaScript编程语言的一个子集
'''
