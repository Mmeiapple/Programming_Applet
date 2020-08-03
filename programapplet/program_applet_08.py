import math
from math import sqrt

'''

【程序8】
题目：输出9*9口诀。
程序分析：分行考虑，两个循环，大循环控制行，小循环控制列，注意输出格式化


'''
class Multiplication():
    def multiplication(self):

        for i in range(1,10):
            for j in range(1,i+1):
                print('%d * %d = % -4d'%(j,i,i*j),end=' ')
            print('\n')



if __name__=="__main__":
    print(Multiplication().multiplication())