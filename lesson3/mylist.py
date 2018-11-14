def mylist(the_list,adjust = False):
    the_name = "通讯录数据列表"
    name = "姓名"
    QQ = "QQ"
    phone_number = "电话"
    e_mail = "邮箱"
    print(the_name.center(50,"~"))
    print(name.ljust(10),QQ.ljust(10),phone_number.ljust(10),e_mail.ljust(20))
    if (adjust == False):
        for i in the_list:
            print(i[0].ljust(12),i[1].ljust(10),i[2].ljust(12),i[3].ljust(20))
    else:
        the_len = len(the_list) - 1
        print(the_list[the_len][0].ljust(12),the_list[the_len][1].ljust(10),the_list[the_len][2].ljust(12),the_list[the_len][3].ljust(20))
    print("END".center(57,"~"))