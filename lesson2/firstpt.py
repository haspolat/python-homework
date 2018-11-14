def num1 ():
    mark = '*'*100
    compony_name = input("公司名称: ")
    consumer_name = input("姓名: ")
    phone_number = input("电话: ")
    email = input("邮箱: ")
    print(mark)
    print("公司名称 %28s" % compony_name)
    print()
    print()
    print("姓名 %32s" % consumer_name)
    print()
    print()
    print("电话 %32s" % phone_number)
    print("邮箱 %32s" % email)
    print(mark)
    return