def get_power(_list, _out):
    if(len(_list) == 0):
        return
    if(len(_list) == 1):
        _out.append([])
        _out.append(_list)
        return _out
    else:
        copy = _list.copy()
        p = copy.pop(0)
        res = get_power(copy, _out).copy()
        for x in res:
            _out.append([p] + x)
        return _out

print(get_power(['a','b','c'], []))