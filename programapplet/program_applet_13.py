import math
from math import sqrt

'''

【程序12】

题目：题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示， 
　　　60分以下的用C表示。 
程序分析：


'''
class IfNested():

    def if_nested(self,score):
        grade='A' if score>=90 else ('B' if score>=60 else 'C')
        return grade

if __name__=="__main__":
    print(IfNested().if_nested(59))