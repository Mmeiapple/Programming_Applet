'''

【程序1】

题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

分析：用循环先组合成一个三位数，然后加三个数不相等的判断条件

'''


class NorepeatThreeDigits():
    def __init__(self):
        self.datalist=[]
        self.count=0
    def norepeat_three_digits(self):
        for one in range(1,5):
            for two in range(1,5):
                for three in range(1,5):
                    if one!=two and two!=three and three!=one:
                        listdata=str(one)+str(two)+str(three)
                        self.count=self.count+1
                        self.datalist.append(listdata)
        self.datalist.append(self .count)
        return self.datalist


if __name__=="__main__":
    data=NorepeatThreeDigits().norepeat_three_digits()
    print(data)




