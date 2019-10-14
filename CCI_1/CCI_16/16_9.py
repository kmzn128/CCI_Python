def minus(a,b):
    num = 0
    while(True):
        if(a == b + num):
            break
        num += 1
    return num

def multiply(a,b):
    sum = 0
    for i in range(b):
        sum += a
    return sum

def divide(a,b):
    num = 0
    index = 0
    while(True):
        num += b
        if(num > a):
            break
        index += 1
    return index

print(minus(5,3))        
print(multiply(5,3))
print(divide(5,3))        