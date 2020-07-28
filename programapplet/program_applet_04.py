'''

【程序4】
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高
　　　于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提
　　　成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
　　　40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于
　　　100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
分析：利润数和奖金数依次叠加相加

'''

class CalculateProfit():
    def __init__(self):
        self.profit=int(input("请输入当月利润： "))
    def  calculate_profit(self):
        if self.profit<=100000:
            bonus=self.profit*0.1
        elif self.profit<=200000:
            bonus=100000*0.1+(self.profit-100000)*0.075
        elif self.profit<=400000:
            bonus=100000*0.1+100000*0.075+(self.profit-200000)*0.05
        elif self.profit<=600000:
            bonus=100000*0.1+100000*0.075+200000*0.05+(self.profit-400000)*0.03
        elif self.profit<=1000000:
            bonus=100000*0.1+100000*0.075+200000*0.05+200000*0.03+(self.profit-600000)*0.015
        else:
            bonus=100000*0.1+100000*0.075+200000*0.05+200000*0.03+400000*0.015+(self.profit-1000000)*0.01
        return bonus



if __name__=="__main__":
    bonus=CalculateProfit().calculate_profit()
    print("奖金数为：{}".format(bonus))


