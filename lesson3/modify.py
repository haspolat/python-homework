import mylist
def modify(the_list):
    mylist.mylist(the_list)
    command = input("请输入要修改的行数(返回菜单请按【q】)：")
    if (command == 'q'):
        return
    number = int(command) - 1
    name = input("输入姓名(返回菜单请按【q】)：")
    if (name == 'q'):
        return
    QQ = input("输入QQ(返回菜单请按【q】)：")
    if (QQ == 'q'):
        return
    phone_number = input("输入电话(返回菜单请按【q】)：")
    if (phone_number == 'q'):
        return
    e_mail = input("输入邮箱(返回菜单请按【q】)：")
    if (e_mail == 'q'):
        return
    this = the_list[number]
    if (name != ""):
        this[0] = name
    if (QQ != ""):
        this[1] = QQ
    if (phone_number != ""):
        this[2] = phone_number
    if (e_mail != ""):
        this[3] = e_mail
    print("修改成功！")
    mylist.mylist(the_list)