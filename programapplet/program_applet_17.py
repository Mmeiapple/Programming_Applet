'''

【程序17】

题目：题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
　　　第10次落地时，共经过多少米？第10次反弹多高？
解析：

'''


class FreeFall():

    def freefall(self):
        high = 100
        sum = 0
        for i in range(2, 11):
            sum += high
            high /= 2

        print('第10次落地时,一共经过：{}米,第10次反弹的高度为：{}'.format(round(sum,2),round(high,2)))

if __name__=="__main__":
    FreeFall().freefall()
    s='abc'
    it= iter(s)
    print(next(it))
    print(next(it))
    print(next(it))

