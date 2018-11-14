# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f())
#     return fs


# f1, f2, f3 = count()
# print(count())
def yield_test(n):
    for i in range(n):
        yield call(i)
        # print(i)
    print("what do you mean!")
    print("end")


def call(i):
    return i*2


for i in yield_test(5):
    print(i, ',', end = ' ')