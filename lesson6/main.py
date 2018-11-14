def log(level, name = None, message = None):
    

    def decorate(func):
        if(name is None):
            the_name = func.__module__
        else:
            the_name = name
        if(message is None):
            the_message = func.__name__
        else:
            the_message = message
        the_level = level
        print("-记录日志-  等级{}，名字{}，描述{}".format(the_level,the_name,the_message))


        def inner(*args):
            func(*args)
        return inner
    return decorate


@log(0,"add","add them")
def add(x, y):
    return x + y


@log(2)
def spam():
    print("spam")


add(1,2)
spam()