def pair_swap(num):
    i = 0
    bit_num = num.bit_length()
    while(i <= bit_num):
        upper_cut = num % 2**(i+2)
        lower_cut = upper_cut - (upper_cut % 2**i)
        if(lower_cut == 2**i):
            num += 2**i
        elif(lower_cut == 2**(i+1)):
            num -= 2**1
        i += 2
    print(bin(num))
        
pair_swap(0b010100111001)