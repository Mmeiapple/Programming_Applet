import math
from math import sqrt

'''

【程序11】
题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数 
　　　本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。  
程序分析：取出个位数的、十位数、百位数，开次方相加和原数对比；


'''
class DaffodilNumber:
    def daffodilnumber(self):
        list_number=[]
        for num in range(100,999):
            single_digits=num%10
            ten_digits=int(num/10%10)
            hundreds_digits=int(num/100)
            if pow(single_digits,3)+pow(ten_digits,3)+pow(hundreds_digits,3)== num:
                list_number.append(num)
        return list_number
if __name__=='__main__':
    print(DaffodilNumber().daffodilnumber())
