def y1():
    for i in range(10):
        yield i

for x in y1():
    print(x)
