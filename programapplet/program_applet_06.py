import math
from math import sqrt

'''

【程序6】
题目：输入某年某月某日，判断这一天是这一年的第几天？ 
程序分析：平年一年为365天，闰年一年为366天，把十二个月的时间组成一个数组，根据输入的月份去累计和，再加上日的时间，再判断年份
        是不是闰年，闰年被400整除或则被4整除并且不能100整除，再加一天；

'''


class DaysCalculation():
    def __init__(self, year, mother, day):
        self.year = year
        self.mother = mother
        self.day = day
        self.mothers = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

    def days_calculation(self):
        try:
            if 0 <= self.mother <= 12:
                sum = self.mothers[self.mother - 1]

            sum += self.day
        except UnboundLocalError as e:
            print("请输入正常的月份数值！")

        if (self.year % 400 == 0) or ((self.year % 4 == 0) and (self.year % 100 != 0)):
            if self.mother > 2:
                sum += 1

        return sum


if __name__ == "__main__":
    year = int(input("\n" + "请输入年份： " + "\n"))
    mother = int(input("\n" + "请输入月份： " + "\n"))
    day = int(input("\n" + "请输入日期时间: " + "\n"))

    sum = DaysCalculation(year, mother, day).days_calculation()
    print("这是{}年的第{}天！".format(year, sum))
