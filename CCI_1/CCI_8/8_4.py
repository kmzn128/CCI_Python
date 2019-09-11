def power_set(_list):
    if(len(_list) > 0):
        yield _list
        e = _list.pop()
        yield _list
        power_set(_list)


def powet_set_main():
    li = ['a','b','c']
    out_list = []
    out_list.append([])
    for elem in li:
        sublist = out_list.copy()
        for elem2 in sublist:
            out_list.append(elem2 + [elem])
    print(out_list)

powet_set_main()
