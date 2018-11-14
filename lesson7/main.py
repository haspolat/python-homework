class Mixed(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    

    def __iter__(self):
        return self.left


    def __getitem__(self,item):
        return self.right

def generator(func):
    yield func.__iter__()
    yield func.__getitem__(0)


test = Mixed(['a', 'b', 'c'],[1, 2, 3])
for i in generator(test):
    print(i)