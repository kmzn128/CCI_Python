def string_comp(st):
    res = []
    count = 0
    former = None
    for c in st:
        count += 1
        if(not former):
            former = c
            res.append(c)
        elif(former == c):
            continue
        else:
            res.append(str(count))
            count = 0
            res.append(c)
            former = c
    res.append(str(count))
    ret_st = ""    
    return ret_st.join(res)

st = "aabcccccaaa"

print(string_comp(st))