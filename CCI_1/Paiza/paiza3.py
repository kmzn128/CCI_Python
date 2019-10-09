i = input().rstrip().split(' ')
k = int(i[0])
s = int(i[1])
t = int(i[2])

memos = [None for i in range(k)]

def make_str(n):
    if(n == 1):
        if(not memos[0]):
            memos[0] = "ABC"
        return memos[0]
    if(n >= 2):
        if(not memos[n-2]):
            memos[n-2] = make_str(n-1)
        if(not memos[n-1]):
            memos[n-1] = "A" + memos[n-2] + "B" + memos[n-2] + "C"
        return memos[n-1]

print(make_str(k)[s:t])        
