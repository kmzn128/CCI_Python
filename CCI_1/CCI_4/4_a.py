def func():
    for i in range(5):
        yield i
def func_b():
    for i in func():
        print(i)

func_b()


