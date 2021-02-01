n = int(input())

for _ in range(n) :
    test_vps = list(input())    
    s = 0
    while test_vps :
        if s > 0:
            break
        pop_element = test_vps.pop()
        if pop_element == '(' :
            s += 1
        else : 
            s -= 1

    if s == 0:
        print('YES')
    else :
        print('NO')