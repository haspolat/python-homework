def ziranshu():
    num = input()
    mylen = len(num) - 1
    num = int(num)
    result = 0
    while (mylen >= 0):
        result += num // (10 ** mylen)
        num -= (num // (10 ** mylen)) * (10 ** mylen)
        mylen -= 1
    print(result)