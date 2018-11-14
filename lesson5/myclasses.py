import random
class Game(object):
    first_num = []
    correct_first_num = []
    second_num = []
    correct_second_num = []
    def __init__(self):
        self.first_num = []
        self.correct_first_num = []
        self.second_num = []
        self.correct_second_num = []


class DoubleBall(Game):
    correct_red_num = 0
    correct_blue_num = 0
    def __init__(self):
        self.first_num = []
        self.second_num = []
        self.correct_first_num = []
        self.correct_second_num = []
        self.correct_red_num = 0
        self.correct_blue_num = 0


    def get_correct_num(self):
        i = 0
        while(i < 6):
            input_num = int (random.uniform(1,33))
            if (input_num in self.first_num):
                continue
            self.correct_first_num.append(input_num)
            i += 1
        input_num = int (random.uniform(1,16))
        self.correct_second_num = input_num
        print("中奖号码为：", end = ' ')
        print(self.correct_first_num, self.correct_second_num)


    def get_num(self):
        i = 0
        while(i < 6):
            input_num = int (input("抽取红球："))
            if (input_num in self.first_num):
                print("你已经取走了该球，请拿别的球。")
                continue
            self.first_num.append(input_num)
            i += 1
        input_num = int (input("请抽取篮球："))
        self.second_num = input_num


    def compair_num(self):
        i = 0
        answer = []
        while(i < 6):
            if (self.correct_first_num[i] == self.first_num[i]):
                DoubleBall.correct_red_num += 1
            i += 1
        if (self.correct_second_num == self.second_num):
            DoubleBall.correct_blue_num += 1
        answer.append(DoubleBall.correct_red_num)
        answer.append(DoubleBall.correct_blue_num)
        return answer


    def print_answer(self,answer):
        if (answer[0] == 6 and answer[1] == 1):
            print("恭喜发财！你得了一等奖！")
        elif (answer[0] == 6 and answer[1] == 0):
            print("恭喜发财！你得了二等奖！")
        elif (answer[0] == 5 and answer[1] == 1):
            print("恭喜发财！你得了三等奖！")
        elif (answer[0] == 5 and answer[1] == 0):
            print("恭喜发财！你得了四等奖！")
        elif (answer[0] == 4 and answer[1] == 1):
            print("恭喜发财！你得了四等奖！")
        elif (answer[0] == 4 and answer[1] == 0):
            print("恭喜发财！你得了五等奖！")
        elif (answer[0] == 3 and answer[1] == 1):
            print("恭喜发财！你得了五等奖！")
        elif (answer[0] == 2 and answer[1] == 1):
            print("恭喜发财！你得了六等奖！")
        elif (answer[0] == 1 and answer[1] == 1):
            print("恭喜发财！你得了六等奖！")
        elif (answer[0] == 0 and answer[1] == 1):
            print("恭喜发财！你得了六等奖！")
        else:
            print("抱歉，没有中奖！")

        
    def run_it(self):
        DoubleBall.get_num(self)
        DoubleBall.get_correct_num(self)
        DoubleBall.print_answer(self,DoubleBall.compair_num(self))


class SuperFunny(Game):
    correct_red_num = 0
    correct_blue_num = 0
    def __init__(self):
        self.first_num = []
        self.second_num = []
        self.correct_first_num = []
        self.correct_second_num = []
        self.correct_red_num = 0
        self.correct_blue_num = 0


    def get_correct_num(self):
        i = 0
        while(i < 5):
            input_num = int (random.uniform(1,35))
            if (input_num in self.first_num):
                continue
            self.correct_first_num.append(input_num)
            i += 1
        i = 0
        while(i < 2):
            input_num = int (random.uniform(1,12))
            if (input_num in self.second_num):
                continue
            self.correct_second_num.append(input_num)
            i += 1
        print("中奖号码为：", end = ' ')
        print(self.correct_first_num, self.correct_second_num)
    

    def get_num(self):
        i = 0
        while(i < 5):
            input_num = int (input("前区号码："))
            if (input_num in self.first_num):
                print("号码不能相同。")
                continue
            self.first_num.append(input_num)
            i += 1
        i = 0
        while(i < 2):
            input_num = int (input("后区号码："))
            if (input_num in self.second_num):
                print("号码不能相同。")
                continue
            self.first_num.append(input_num)
            i += 1

        
    def compair_num(self):
        answer = []
        i = 0
        while(i < 5):
            if (self.correct_first_num[i] in self.first_num):
                SuperFunny.correct_red_num += 1
            i += 1
        i = 0
        while(i < 2):
            if (self.correct_second_num[i] in self.second_num):
                SuperFunny.correct_blue_num += 1
            i += 1
        answer.append(SuperFunny.correct_red_num)
        answer.append(SuperFunny.correct_blue_num)
        return answer


    def print_answer(self,answer):
        if (answer[0] == 5 and answer[1] == 2):
            print("恭喜发财！你得了一等奖！")
        elif (answer[0] == 5 and answer[1] == 1):
            print("恭喜发财！你得了二等奖！")
        elif (answer[0] == 5 and answer[1] == 0):
            print("恭喜发财！你得了三等奖！")
        elif (answer[0] == 4 and answer[1] == 2):
            print("恭喜发财！你得了三等奖！")
        elif (answer[0] == 4 and answer[1] == 1):
            print("恭喜发财！你得了四等奖！")
        elif (answer[0] == 3 and answer[1] == 2):
            print("恭喜发财！你得了四等奖！")
        elif (answer[0] == 4 and answer[1] == 0):
            print("恭喜发财！你得了五等奖！")
        elif (answer[0] == 3 and answer[1] == 1):
            print("恭喜发财！你得了五等奖！")
        elif (answer[0] == 2 and answer[1] == 2):
            print("恭喜发财！你得了五等奖！")
        elif (answer[0] == 3 and answer[1] == 0):
            print("恭喜发财！你得了六等奖！")
        elif (answer[0] == 1 and answer[1] == 2):
            print("恭喜发财！你得了六等奖！")
        elif (answer[0] == 2 and answer[1] == 1):
            print("恭喜发财！你得了六等奖！")
        elif (answer[0] == 0 and answer[1] == 2):
            print("恭喜发财！你得了六等奖！")
        else:
            print("抱歉，没有中奖！")


    def run_it(self):
        SuperFunny.get_num(self)
        SuperFunny.get_correct_num(self)
        SuperFunny.print_answer(self,SuperFunny.compair_num(self))