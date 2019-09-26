
def check_flip_bit(in_int):
    li = list(bin(in_int)[2:])
    result_list = []
    first = 1
    second = 0
    second_can_start = False
    for i in range(1, len(li)):
        if(li[i] == '0'):
            second_can_start = True
            if(first > 0 and second > 0):
                result_list.append([first,second])
                first = second
                second = 0
            if(li[i-1] == '0'):
                first = 0
                second_can_start = False
        else:
            if(second_can_start):
                second += 1
            else:
                first += 1
            if(i == len(li)-1):
                result_list.append([first,second])
    return max([sum(x) for x in result_list] )
            

print(check_flip_bit(0b11010111110111101111111))