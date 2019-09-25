from argparse import ArgumentError

def count_bin_digit(bin_in):
    st = str(bin(bin_in))
    if(not st.startswith("0b")):
        raise ArgumentError("not start 0b")
    return len(list(st[2:]))

def insertion(in_num, inserted_num, index):
    in_digit = count_bin_digit(in_num)
    inserted_digit = count_bin_digit(inserted_num)
    mask_list = []
    for i in range(in_digit):
        if(i >= index and i < inserted_digit + index):
            mask_list.append('0')
        else:
            mask_list.append('1')
    mask_list.reverse()
    st = ""
    st = st.join(mask_list)
    mask = int(st, base=2)
    return bin((mask & in_num) + (inserted_num << index))

print(insertion(0b1010100000000, 0b10111, 2))