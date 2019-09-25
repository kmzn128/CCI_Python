def count_coin_pattern(n):
    if(n < 5):
        if(memo[n] != 0):
            memo[n] = n
        

def main(n):
    memo = list(range(n))
    