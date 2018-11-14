import mylist
def my_delete(the_list):
    mylist.mylist(the_list)
    command = input("请输入要删除的行数(返回菜单请按【q】)：")
    if (command == 'q'):
        return
    the_number = int(command) - 1
    pity = the_list[the_number]
    the_list.remove(pity)
    mylist.mylist(the_list)
    print("删除成功")