'''

【程序16】

题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程
　　　找出1000以内的所有完数。
解析：
    先分解这个数，然后判断相加是否等于这个数；
'''


class PerfectNumber():

    def perfectnumber(self):
        for i in range(1, 1000):
            lista = []
            for j in range(1, i):
                if i % j == 0:
                    lista.append(j)
            if i == sum(lista):
                print(f"{i}={'+'.join(map(str, lista))}")

if __name__ == "__main__":
    PerfectNumber().perfectnumber()

