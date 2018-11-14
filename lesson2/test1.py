import firstpt
import ziranshuchuli
import zhishuchuli
import lesson2
import tupianchuli
mark = 50*'='
smark = 3*'='
biaoti = "欢迎哈式超级系统V1.0"
print(mark)
print("%s%24s%15s" % (smark,biaoti,smark))
print("%s1.  功能一%37s" % (smark,smark))
print("%s2.  功能二%37s" % (smark,smark))
print("%s3.  功能三%37s" % (smark,smark))
print("%s4.  功能四%37s" % (smark,smark))
print("%s5.  功能五%37s" % (smark,smark))
print("%s6.  退出%39s" % (smark,smark))
print(mark)
command = 0
while(command != 6):
    command = input("请输入你的指令：")
    if (command == "1"):
        #格式化输出
        firstpt.num1()
    elif (command == "2"):
        #自然数处理
        ziranshuchuli.ziranshu()
    elif (command == "3"):
        #质数
        zhishuchuli.zhishu()
    elif (command == "4"):
        #乘法表
        lesson2.chengfabiao()
    elif (command == "5"):
        #图片处理
        tupianchuli.tupianchuli()
    elif (command == "6"):
        break
    else:
        print("wtf")