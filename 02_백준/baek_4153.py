import sys

while_boolean = 1
triangle_list = list(map(int, sys.stdin.readline().split()))
while while_boolean:
    x, y, z = sorted(triangle_list)
    flag_boolean = (x**2 + y**2 == z**2)

    if flag_boolean :
        print('right')
    else : 
        print('wrong')

    triangle_list = list(map(int, sys.stdin.readline().split()))
    while_boolean = sum(triangle_list)
