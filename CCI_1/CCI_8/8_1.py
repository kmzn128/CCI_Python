
def count_step(n, memo):
    if(n == 1):
        if(memo[0] == 0):
            memo[0] = 1
        return
    if(n == 2):
        if(memo[1] == 0):
            memo[1] = 2
        return
    if(n == 3):
        if(memo[2] == 0):
            memo[2] = 4
        return 
    if(n > 3):
        if(memo[n-2] == 0):
            count_step(n-1, memo)
        if(memo[n-3] == 0):
            count_step(n-2, memo)
        if(memo[n-4] == 0):
            count_step(n-3, memo)
        memo[n-1] = memo[n-2] + memo[n-3] + memo[n-4]

def count_step_main(n):
    memo = [0 for x in range(n)]
    count_step(n, memo)
    print(memo[-1])
    
count_step_main(20)

        

