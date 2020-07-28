'''

【程序2】

题目：冒泡排序

分析：从左向右，两两比较，大的往后面，小的排前面，像气泡一样，小的冒上来，大的沉下去。
    循环走过每一轮，可以保证一个数是正确的排序位置，所以内层循环次数可以减一、不考虑已经排好的的元素了
    直到所以轮次走完，次序没有交换；

'''


class BubbleSort():
    def __init__(self,datalist):
        self.datalist=datalist
        self.lenth=len(self.datalist)
    def bubble_sort(self):
        for i in range(self.lenth):
            for j in range(self.lenth-i-1):
                if self.datalist[j]>self.datalist[j+1]:
                    self.datalist[j],self.datalist[j+1]=self.datalist[j+1],self.datalist[j]
        return self.datalist


if __name__=="__main__":
    data=[1,33,3,2,9,2]
    number=BubbleSort(data).bubble_sort()
    print(number)






