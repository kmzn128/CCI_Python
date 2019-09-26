def print_binary_string(in_int):
    if(in_int <= 0 or in_int >= 1):
        print("input error:")
    li = ["0."]
    for i in range(30):
        in_int *= 2
        if(in_int > 1):
            li.append('1')
            in_int -= 1
        else:
            li.append('0')
    out_str = ""
    print(out_str.join(li))

print_binary_string(0.3)
            