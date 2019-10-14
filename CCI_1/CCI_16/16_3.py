def calc_point(p1, p2, q1, q2):
    a = (p2[1]-p1[1])/(p2[0]-p1[0])
    b = (q2[1]-q1[1])/(q2[0]-q1[0])
    if(a == b):
        return None
    else:
        x0 = ((a*p1[0]-b*q1[0])-(p1[1]-q1[1]))/(a-b)
        y0 = a*(x0-p1[0])+p1[0]
        return (x0,y0)
    
p1 = (1,1)
p2 = (5,3)
q1 = (1,3)
q2 = (5,1)

print(calc_point(p1, p2, q1, q2))