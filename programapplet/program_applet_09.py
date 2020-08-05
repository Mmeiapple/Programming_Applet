import math
from math import sqrt

'''

【程序9】
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月 
　　　后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？ 
程序分析：斐波拉契数列，兔子的规律为数列1,1,2,3,5,8,13,21…

第一个月为1，第二个月为1，第三个月为2,第四个月3，第五个月，5
'''
class RabbitPopulation:
    def rabbitpopulation(self):
        f1 = 0
        f2 = 1
        for i in range(1, 13):
            print("第%d个月，兔子总数为%d " % (i, f2))
            f1, f2 = f2, f1 + f2


if __name__=="__main__":
    RabbitPopulation().rabbitpopulation()