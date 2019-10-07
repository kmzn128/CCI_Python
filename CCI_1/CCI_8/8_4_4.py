def get_power(elms, res):
    if(len(elms) == 1):
        res.append([])
        res.append(elms)
    else:
        right = elms.pop()
        ress = get_power(elms, res)
        for e in ress:
            res.append(e + [right])
    return res.copy()

print(get_power(['a','b','c'], []))