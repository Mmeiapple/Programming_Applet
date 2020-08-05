import math
from math import sqrt

'''

【程序10】
题目：判断101-200之间有多少个素数，并输出所有素数。 
程序分析：直观方法，如果被除数设置为从2到number-1的整数，如果都不等0，那么就是素数
        简化直观方法，我们可以将试除数范围扩小，设置为2到这个数的开平方数，如果整除都不等于0，那么就是素数


'''

class IfPrimenumber():

    def if_primenumber(self):
        list_number=[]
        for i in range(101,201):
            sqrt_number=int(sqrt(i))
            leap=1
            for j in range(2,sqrt_number+1):
                if i%j==0:
                    leap=0
                    break
            if leap==1:
                list_number.append(i)
        return list_number


if __name__=="__main__":
    print(IfPrimenumber().if_primenumber())

