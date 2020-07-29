import math
from math import sqrt

'''

【程序5】
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后
　　　　　　相乘等于那个100+1和1168+i，即是结果。请看具体分析：

'''
class SqrtNumber():
    def __init__(self):
        self.numberlist=[]

    def sqrtnumber(self):
        for i in range(1, 100000):

            x = int(sqrt(i + 100))

            y = int(sqrt(i + 268))

            if (x * x == i + 100) and (y * y == i + 268):
                self.numberlist.append(i)
        return self.numberlist

if __name__=="__main__":
    print('满足条件的数为： ',SqrtNumber().sqrtnumber())