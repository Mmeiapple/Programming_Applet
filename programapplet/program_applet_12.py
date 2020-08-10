import math
from math import sqrt

'''

【程序12】

题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。 
程序分析：对整数进行逐步分解，找到所有质因数；
        1、判断该数不等于N，否则输出
        2、如果该数能被N整除，就输出N的值，并用n除以k的商,作为新的正整数你n, 
        3、如果n不能被k整除，则用k+1作为k的值,重复执行第一步。


'''
class FactorizationPrimeFactor():
    def  factorization_prime_factor(self):
        number = int(input("请输入整数！"))
        list_number = []
        for i in range(2, number + 1):
            if number % i == 0:
                number = number / i
                list_number.append(i)
        return list_number
if __name__=="__main__":
    print(FactorizationPrimeFactor().factorization_prime_factor())