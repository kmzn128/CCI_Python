def sort_str(s):
    li = list(s)
    for i in range(len(li)-1):
        min_idx = i
        for j in range(i+1, len(li)):
            if li[i] > li[j]:
                min_idx = j
        li[i], li[min_idx] = li[min_idx], li[i]
    return li

def check_permutation(str_a, str_b):
    sorted_a = sort_str(str_a)
    sorted_b = sort_str(str_b)
    return sorted_a == sorted_b

a = "abcd"
b = "bcdae"

print(check_permutation(a, b))