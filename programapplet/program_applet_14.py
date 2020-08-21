import math
from math import sqrt
import re

'''

【程序14】

题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。 
程序分析：对字符串进行分解，然后判断类型计算个数

'''


class CountChar():
    def count_char(self):
        char=number=sapce=other=0
        s=input("请输入内容： ")
        for i in s:
            if (i>='a' and i<='z') or (i>='A' and i<='Z'):
                char+=1
            elif (i>='0') and (i<='9'):
                number+=1
            elif i==' ':
                sapce+=1
            else:
                other+=1
        print('字符串： %s,数字： %s,空格： %s,其他： %s' % (char, number, sapce, other))


if __name__=="__main__":
    CountChar().count_char()

# char=number=sapce=other=0
#
# s = input("请输入内容： ")
# for i in s:
#     if (i>='a' and i<='z') or (i>='A' and i<='Z'):
#         char+=1
#     elif (i>='0') and (i<='9'):
#         number+=1
#     elif i==' ':
#         sapce+=1
#     else:
#         other+=1
#
# print('字符串： %s,数字： %s,空格： %s,其他： %s'%(char,number,sapce,other))
