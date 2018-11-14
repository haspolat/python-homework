import myclasses
while (True):
    command = input("请输入要玩的玩法(1.双色球 2.超级大乐透): ")
    if (command == '1'):
        doubel_ball = myclasses.DoubleBall()
        doubel_ball.run_it()
    elif(command == '2'):
        super_funny = myclasses.SuperFunny()
        super_funny.run_it()