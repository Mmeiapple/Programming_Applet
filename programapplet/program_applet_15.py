import math
from math import sqrt
import re

'''

【程序15】

题目：求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如2+22+222+2222+22222(此时 
　　　共有5个数相加)，几个数相加有键盘控制。  
程序分析：先分析得出循环的值，然后取循环的值进行相加

'''
class CycleSum():
    def __init__(self):
        self.number=int(input("请输入该数: "))
        self.cycle=int(input("请输入循环次数:"))
        self.list_nember=[]
        self.num=0
        self.sum_value=0
    def cycle_sum(self):


        for i in range(self.cycle):
            self.num+=self.number*(10**i)
            self.list_nember.append(self.num)


        for value in self.list_nember:
            self.sum_value+=value
        return self.sum_value

if __name__=="__main__":
    print(CycleSum().cycle_sum())




