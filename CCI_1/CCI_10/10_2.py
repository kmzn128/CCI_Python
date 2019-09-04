anagrams = ["abc",
            "bda",
            "cab",
            "eee"
    ]

def compare_anagrams(str_a, str_b):
    return sorted(str_a) == sorted(str_b)

k = 1
for i in range(len(anagrams)):
    if(i < k and i > 0):
        continue
    for j in range(i+1, len(anagrams)):
        if(compare_anagrams(anagrams[i], anagrams[j])):
            anagrams[k], anagrams[j] = anagrams[j], anagrams[k]
            k += 1

print(anagrams)