#tamrin_paskal_khayam
def paskal_khayam(n) : 
    for j in range(0, n) : 
        for i in range(0, j + 1) : 
            print(answer(j, i), " ", end = "") 
        print() 
def answer(n, k) : 
    result = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        result = result * (n - i) 
        result = result // (i + 1) 
    return result 
n = 7 
paskal_khayam(n)