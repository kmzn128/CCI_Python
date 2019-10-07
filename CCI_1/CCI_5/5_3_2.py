def calc_maximum(first, second, maximum):
    if( maximum < first + second):
        maximum = first + second
    return maximum

def flip_bit(num):
    first = second = maximum = 0
    second_can_start = False
    while(num != 0):
        if(num % 2 == 1):
            if(not second_can_start):
                first += 1
            else:
                second += 1
        else:
            maximum = calc_maximum(first, second, maximum)
            if(not second_can_start):
                second_can_start = True
                if(second > 0):
                    first = second
            else:
                first = second = 0
                second_can_start = False
        num >>= 1
    return maximum+1        
            
print(flip_bit(0b110101111100111101111111))