# coding:utf-8
import json

'''
简介：
JSON是一种非常好的数据序列化的形式，被如今的各种API和web service大量的使用。使用python内置的json处理，可以使JSON串具有一定的可读性，但当遇到大型数据时，它表现成一个很长的、连续的一行时，人的肉眼就很难观看了
'''

data = {'status': 'ok', 'count': 2, 'results': [{'age': 28, 'name': 'baolibin'}, {'age': 28, 'name': 'yangfl'}]}

# 普通打印
print(json.dumps(data))

# 漂亮的打印
print(json.dumps(data, indent=2))

'''
运行的结果分别如下所示：
普通打印：
{"status": "ok", "count": 2, "results": [{"age": 28, "name": "baolibin"}, {"age": 28, "name": "yangfl"}]}

漂亮的打印：
{
  "status": "ok",
  "count": 2,
  "results": [
    {
      "age": 28,
      "name": "baolibin"
    },
    {
      "age": 28,
      "name": "yangfl"
    }
  ]
}
'''