import mylist
def my_add(the_list):
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
    this_list = [name,QQ,phone_number,e_mail,"\n"]
    the_list.append(this_list)
    mylist.mylist(the_list, True)