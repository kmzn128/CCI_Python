def get_power(_list):
    if(len(_list) == 0):
        return
    out_list = []
    if(len(_list) == 1):
        yield []
        yield _list
    else:
        copy = _list.copy()
        p = copy.pop(0)
        for x in get_power(copy):
            yield [p] + x

for x in get_power(['a','b','c']):
    print(x)