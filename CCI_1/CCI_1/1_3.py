
str_input = "Mr John Smith"
list_input = list(str_input)

list_output = []
for c in list_input:
    if(c == " "):
        list_output.append("%")
        list_output.append("2")
        list_output.append("0")
    else:
        list_output.append(c)
str_output = ""
print(str_output.join(list_output))