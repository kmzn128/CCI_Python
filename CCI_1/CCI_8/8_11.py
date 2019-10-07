def count_pattern(coin_list, n, ind):
    coin = coin_list[ind]
    if(ind == len(coin_list)-1):
        rem = n % coin
        return 1 if rem == 0 else 0
    ways = 0
    amount = 0
    i = 0
    while(n >= amount):
        amount = i * coin
        ways += count_pattern(coin_list, n - amount, ind + 1)
        i += 1
    return ways


def coin_pattern(n):
    coin_list = (25,10,5,1)
    count_pattern(coin_list, n, 0)
        

print(coin_pattern(67))
    