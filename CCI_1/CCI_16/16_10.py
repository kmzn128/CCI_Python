import random

def living_people():
    N = 100
    li = []
    for i in range(N):
        a = random.randint(1900, 2000)
        b = random.randint(1900, 2000)
        born = min(a,b)
        dead = max(a,b)
        li.append([born, dead])
    
    histo = [0 for i in range(100)]
    
    for born, dead in li:
        for j in range(born-1900, dead-1900):
            histo[j] += 1
    print(histo)

living_people()