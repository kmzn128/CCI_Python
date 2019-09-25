def add_ampasand_20(str_in):
    li = []
    for c in str_in:
        if c == " ":
            li.append("%20")
        else:
            li.append(c)
    str_out = ""
    return str_out.join(li)

str_in = "Mr John Smith"
print(add_ampasand_20(str_in))