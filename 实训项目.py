import random
import time as ti
from datetime import *

now_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S').split('-')
now_time = '{}年{}月{}日 {}时{}分{}秒'.format(now_time[0], now_time[1], now_time[2], now_time[3], now_time[4], now_time[5])


class count_subject(object):
    def __init__(self):
        # T_answer_list:保存正确答案，F_answer_list:保存输入的答案，sign:运算符
        self.T_answer_list = []
        self.F_answer_list = []
        self.sign = None
        self.fp = None

    def judge(self):
        """判断答对多少道"""
        k = 0
        for i in self.F_answer_list:
            if i in self.T_answer_list:
                k += 1
        return k

    def calculate(self):
        """进行题目计算与保存"""
        self.fp = open(f'{now_time}的做题记录.txt', 'a+', encoding='utf8')
        self.fp.writelines('题目\t\t你的结果\t正确答案\n')
        start_time = ti.time()
        for i in range(10):
            n1, n2 = random.randint(10, 99), random.randint(10, 99)
            self.fp.writelines(f'{n1}{self.sign}{n2}\t')
            f_answer = int(input(f'{n1}{self.sign}{n2}='))
            t_answer = eval(f'{n1}{self.sign}{n2}')  # eval函数可以将传入的字符串表达式计算出结果输出，返回浮点型
            self.fp.writelines(f'{f_answer}\t\t{t_answer}\n')
            self.T_answer_list.append('{:.1f}'.format(t_answer))
            self.F_answer_list.append('{:.1f}'.format(f_answer))
        end_time = ti.time()
        print('您一共用了：{:.2f}s'.format((end_time - start_time)))
        print('一共做对了{}个题目'.format(self.judge()))
        self.fp.writelines('完成时间：{:.2f}s\n做对题目数:{}道\n'.format((end_time - start_time), self.judge()))
        self.T_answer_list, self.F_answer_list = [], []  # 进行一轮计算后，将保存答案的列表清空，方便下一轮计算使用

    def start(self):
        """开始菜单栏"""
        print('结果有小数部分请保留一位小数！')
        while True:
            symbol = int(input('1.加法\n2.减法\n3.乘法\n4.除法\n5.求余数\n0.退出\n请输入：'))
            if symbol in dict_1.keys():
                self.sign = dict_1[symbol]
            elif symbol == 0:
                self.fp.close()
                return
            self.calculate()


if __name__ == "__main__":
    dict_1 = {1: '+', 2: '-', 3: '*', 4: '/', 5: '%'}
    count = count_subject()
    count.start()
