


def solution() :
    L, P, V = map(int, input().split())

    cnt = 1
    flag = L + P + V
    while flag :
        mok = V // P
        na  = V % P

        if na >= L :
            print('Case {}: {}' .format(cnt, mok*L + L))
        else :
            print('Case {}: {}' .format(cnt, mok*L + na))
        
        L, P, V = map(int, input().split())
        flag = L + P + V
        cnt += 1
        
solution()