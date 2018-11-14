def make_bond(fun):
    print('----a----')

    def inner():
        print('----1----')
        return '<b>' + fun() + '</b>'

    return inner


def make_italic(fun):
    print('----b----')

    def inner():
        print('----2----')
        return '<i>' + fun() + '</i>'

    return inner


@make_bond
@make_italic
def test():
    print('----c----')
    print('----3----')
    return 'hello python decorator'


ret = test
print(ret())