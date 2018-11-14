import test3
import add
import mylist
import mdelete
import modify
test3.my_system()
the_list = [["123","123","123","123"],["haha","123","123","123"]]
while(True):
    command = input("输入命令(返回菜单请按【q】)：")
    if (command == 'q'):
        test3.my_system()
    elif (command == 'a'):
        add.my_add(the_list)
    elif (command == 's'):
        mylist.mylist(the_list)
    elif (command == 'd'):
        mdelete.my_delete(the_list)
    elif (command == 'm'):
        modify.modify(the_list)
    else:
        print("wtf")