import random
import string

'''

【程序18】

题目：生成200个指定长度的随机码

解析：
   1、外循环控制字符串个数，内循环控制字符串长度
   
'''

class RandomCode():
    def __init__(self, number, length):
        self.number = number
        self.length = length

    def randomcode(self):
        count = 1
        file = open('randomfile.txt', 'w')
        for i in range(self.number):
            value=''
            content = string.ascii_lowercase + string.digits
            for j in range(self.length):
                value += random.choice(content)

            file.write(str(count)+' : '+value+'\n')
            count = count+1
        file.close()


if __name__=="__main__":
    RandomCode(200,7).randomcode()