def my_system():
    mark = 57*'#'
    sys_name = "你的名字"
    command_a = "添加数据请按【a】"
    command_b = "查看数据请按【s】"
    command_c = "删除数据请按【d】"
    command_d = "修开数据请按【m】"
    command_q = "返回菜单请按【q】"
    print(mark)
    print(sys_name.center(50))
    print()
    print(command_a.center(50))
    print(command_b.center(50))
    print(command_c.center(50))
    print(command_d.center(50))
    print()
    print(command_q.rjust(50))
    print(mark)