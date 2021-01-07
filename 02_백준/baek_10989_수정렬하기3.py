# 카운팅 정렬
import sys

N = int(sys.stdin.readline())

count_array = [0] * 10000
for _ in range(N):
    input_num = int(sys.stdin.readline())
    count_array[input_num - 1] += 1

for num, cnt in enumerate(count_array) :
    for _ in range(cnt) :
        print(num + 1)
