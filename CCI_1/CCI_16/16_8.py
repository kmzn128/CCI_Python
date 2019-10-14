dic_num = {0:"Zero",
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four",
        5:"Five",
        6:"Six",
        7:"Seven",
        8:"Eight",
        9:"Nine"
        }

dic_teen = {0:"Ten",
            1:"Eleven",
            2:"Twelve",
            3:"Thirteen",
            4:"Fourteen",
            5:"Fifteen",
            6:"Sixteen",
            7:"Seventeen",
            8:"Eighteen",
            9:"Nineteen"}

dic_twe = {2:"Twenty",
           3:"Thirty",
           4:"Forty",
           5:"Fifty",
           6:"Sixty",
           7:"Seventy",
           8:"Eighty",
           9:"Ninety"}

dic_illion = {0:"",
                1:"Thousand",
              2:"Million",
              3:"Billion"}


def make_chunks(num):
    if(num < 0):
        raise(ArithmeticError())
    st = str(num)
    le = len(st)
    di, mo = divmod(le, 3)
    chunks = []
    if(mo > 0):
        chunks.append(st[:mo].zfill(3))
    for i in range(di):
        chunks.append(st[mo+3*i:mo+3*(i+1)])
    return chunks
        
def make_str_by_chunk(chunk, illion):
    li = []
    int_100 = int(chunk[0])
    int_10 = int(chunk[1])
    int_1 = int(chunk[2])
    if(int_100 > 0):
        li.append(dic_num[int_100]+"Hundred ")
    if(int_10 > 1):
        li.append(dic_twe[int_10] + " ")
    elif(int_10 == 1):
        li.append(dic_teen(int_1) + " ")
        return "".join(li)
    if(int_1 > 0):
        li.append(dic_num[int_1] + " ")
    li.append(dic_illion[illion] + " and ")
    return "".join(li)
    
def declare_english_int(num):
    chunks = make_chunks(num)
    out_list = []
    illion = len(chunks)-1
    for chunk in chunks:
        out_list.append(make_str_by_chunk(chunk, illion))
        illion -= 1 
    print("".join(out_list))
    

declare_english_int(103023353)