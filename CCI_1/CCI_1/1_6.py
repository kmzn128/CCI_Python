str_in = "aabcccccaaa"
buf = []
out = []
for c in str_in:
    if (len(buf) == 0):
        buf.append(c)
    else:
        prev = buf[len(buf)-1]
        if(prev == c):
            buf.append(c)
        else:
            out.append(prev)
            out.append(str(len(buf)))
            buf.clear()
            buf.append(c)
out.append(buf[len(buf)-1])
out.append(str(len(buf)))

print("".join(out))
