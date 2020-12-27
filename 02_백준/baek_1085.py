import sys

x, y ,w, h = map(int, sys.stdin.readline().split())

garo = w - x
sero = h - y
zero_garo = x
zero_sero = y

temp_list = [garo, sero, zero_garo, zero_sero]
sorted_list = sorted(temp_list)

print(sorted_list[0])


# python3 통과