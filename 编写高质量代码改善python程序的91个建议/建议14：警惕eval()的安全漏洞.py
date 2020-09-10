# coding:utf-8

# 建议14：警惕eval()的安全漏洞
# 进行判断
print(eval("1+1==2"))  # True
# 字符连接
print(eval("'a'+'b'"))  # ab
# 数字相加
print(eval("1+2"))  # 3
'''
Python中eval()函数将字符串str当成有效的表达式来求值并返回计算结果

'''