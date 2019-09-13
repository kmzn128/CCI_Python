def get_permutation(_list):
    if(len(_list) == 0):
        return
    out_list = []
    if(len(_list) == 1):
        out_list.append(_list)
        return out_list
    #elif(len(_list) == 2):
    #    out_list.append(_list)
    #    rev = _list[::-1]
    #    out_list.append(rev)
    #    return out_list
    else:
        for i in range(len(_list)):
            copy = _list.copy()
            p = copy.pop(i)
            ret = get_permutation(copy)
            for x in ret:
                out_list.append([p] + x)
        return out_list


print(get_permutation(['a','b','c']))
