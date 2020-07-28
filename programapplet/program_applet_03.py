'''

【程序3】

题目：选择排序

分析：
    1、设第一个元素值为最小值，当做比较元素，依次和后面的元素比较，找到更小的元素，就将他与第一个元素交换位置
    2、重复循环，找到第二小的，就和第二第二小的位置交换，第三小的交换，依次排序，直到比较完毕，完成排序呢

'''


class SelectionSort():
    def __init__(self,datalist):
        self.datalist=datalist
        self.lenth=len(self.datalist)
    def selection_sort(self):
        for i in range(self.lenth):
            min_index=i
            for j in range(i+1,self.lenth):
                if self.datalist[j]<self.datalist[min_index]:
                   min_index=j
            self.datalist[min_index],self.datalist[i]=self.datalist[i],self.datalist[min_index]
        return self.datalist

if __name__=="__main__":
    data=[2,0,344,1231,1,23,12,]
    sortdata=SelectionSort(data).selection_sort()
    print(sortdata)







