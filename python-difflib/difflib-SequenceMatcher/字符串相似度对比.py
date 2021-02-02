# coding:utf-8
import difflib


def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()


print(string_similar('爱尔眼科沪滨医院', '沪滨爱尔眼科医院'))
print(string_similar('北戴河阿那亚隐庐酒店', '北戴河阿那亚隐庐酒店'))
print(string_similar('北戴河阿那亚隐庐酒店', '北戴河阿那亚隐庐酒店式公寓'))
print(string_similar('安定区妇幼保健站', '定西市安定区妇幼保健站'))
print(string_similar('广州市医院', '广东省中医院'))
print(string_similar('北京北辰五洲皇冠国际酒店', '北京北辰洲际酒店'))
print(string_similar('北京钓鱼台大酒店', '百时快捷酒店(北京西钓鱼台地铁站店)'))
print(string_similar('ClubMed joyview北戴河黄金海岸度假村', 'Club Med Joyview北戴河黄金海岸度假村'))
print(string_similar('张家口太舞滑雪小镇太舞酒店', '张家口太舞滑雪小镇雪麓居酒店'))

'''
输出结果如下所示：
1.0
1.0
0.8695652173913043
0.8421052631578947
0.5454545454545454
0.8
0.5384615384615384
0.9411764705882353
0.8148148148148148
'''
