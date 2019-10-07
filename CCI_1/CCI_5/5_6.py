def conv(x,y):
    xord = x^y
    s = str(bin(xord))
    return s[2:].count('1')

print(conv(29, 15))