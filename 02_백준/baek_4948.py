# pypy3로는 통과지만..
# python3는 통과못함

def prime_number(k):
    if k == 1:
        return False
    elif k % 2 == 0:
        return False
    else :
        for i in range(3, int(k**(1/2))+1):
            if k % i == 0:
                return False
        return True


n = 1

while n :
    n = int(input())
    if n==0:
        break
    elif n==1:
        print(1)
        continue
    cnt = 0
    for num in range(n+1, 2*n+1):
        cnt += prime_number(num)
    print(cnt)