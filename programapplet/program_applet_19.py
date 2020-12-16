import random
import string

'''

【程序18】

题目：python 随机生成汉字

解析：
   1、gbk2312对字符的编码采用两个字节相组合,第一个字节的范围是0xB0-0xF7, 第二个字节的范围是0xA1-0xFE.
对GBK2312编码方式详细的解释请参看GBK2312编码
   
'''

"""
使用列表推导式把列表中的单个元素全部转化为str类型，
把列表中的元素放在空串中，元素间不隔开，然后返回值

"""

class RandomChinese():
    def __init__(self, length):
        self.length = length

    def randomchinese(self):
        listvale = []
        for i in range(1,self.length):
            head = random.randint(0xB0,0xF7)
            body = random.randint(0xA1,0xFE)
            value = f'{head:x}{body:x}'
            str1 = bytes.fromhex(value).decode('gb2312')
            listvale.append(str1)

        liststr1 = [str (i) for i in listvale]
        liststr2= ''.join(liststr1)
        return liststr2
if __name__=="__main__":
    print(RandomChinese(7).randomchinese())