def hanoi(a,b,c,n):
    if(n == 1):
        b.append(c.pop())
        return
    if(n == 2):
        a.append(c.pop())
        hanoi(a,b,c,1)
        b.append(a.pop())
    if(n >= 3):
        hanoi(a,b,c,n-1)
        a.append(c.pop())
        hanoi(a,c,b,n-1)
        b.append(a.pop())
        hanoi(a,b,c,n-1)

    
    


a = []
b = []
c = [6,5,4,3,2,1]

def main():
    length = len(c)
    hanoi(a,b,c,length)
    print(a)
    print(b)
    print(c)
    
main()