def prime_number(k) :
    if k == 1 :
        return False
    elif k % 2 == 0 :
        return False
    else :
        for i in range( 3, int(k**(1/2))+1, 2 ) :
            if k % i == 0 :
                return False
        return True


n = int(input())


for _ in range(n) :
    number = int(input())
    half = int(number / 2)
    small, big = half, half
    while 1 :
        if prime_number(small) and prime_number(big):
            print(small, big)
            break
        else :
            small, big = int(small-1), int(big+1)



## 왜 런타임에러??????????















