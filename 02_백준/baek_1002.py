# python3 통과


import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    small_r, big_r = sorted([r1, r2])
    center_distance = ( (x1 - x2)**2 + (y1 - y2)**2 )**(1/2)


    if (center_distance==0) & (r1 == r2):
        print(-1) 
    elif center_distance < big_r :
        if big_r > center_distance + small_r:
            print(0)
        elif big_r == center_distance + small_r:
            print(1)
        else :
            print(2)
    
    elif center_distance >= big_r:
        if r1 + r2 > center_distance:
            print(2)
        elif r1 + r2 == center_distance:
            print(1)
        else :
            print(0)




