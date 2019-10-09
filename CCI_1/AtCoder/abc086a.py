inp = list(map(int, input().rstrip().split(' ')))
if((inp[0]*inp[1])%2 == 0):
    print("Even")
else:
    print("Odd")