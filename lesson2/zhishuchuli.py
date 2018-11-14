def zhishu():
    mylist = []
    num = int(input())
    i = num - 1
    while (num > 1):
        while (i >= 1):
            if (num % i == 0):
                if (i == 1):
                    mylist.append(num)
                else:
                    break
            i -= 1
        num -= 1
        i = num - 1
    print(mylist)