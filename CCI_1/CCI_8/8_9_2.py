def add_parens(li, lnum, rnum, eli, ind):
    if(lnum < 0 or rnum < lnum):
        return 
    if(lnum == 0 and rnum == 0):
        st = ""
        li.append(st.join(eli))
    else:
        eli[ind] = '('
        add_parens(li, lnum-1, rnum, eli, ind+1)
        
        eli[ind] = ')'       
        add_parens(li, lnum, rnum-1, eli, ind+1)

def main(n):
    li = []
    e = ['x' for i in range(n*2)]
    add_parens(li, n, n, e, 0)
    print(li)
    
main(3)
    