import math
from math import sqrt

'''

【程序7】
题目：输入三个整数x,y,z，请把这三个数由小到大输出。 
程序分析：冒泡排序算法

'''


class CompareOutput():
    def compare_output(self):
        list_number=[]
        try:
            for i in range(1,4):
                number=int(input("请输入整数:"+"\n"))
                list_number.append(number)
        except ValueError as e:
            print("请输入整数")


        for i in range(len(list_number)):
            for j in range(len(list_number)-1-i):
                if list_number[j]>list_number[j+1]:
                    list_number[j],list_number[j+1]=list_number[j+1],list_number[j]
        return list_number

if __name__=="__main__":
    print(CompareOutput().compare_output())



