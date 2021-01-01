import sys
from itertools import combinations


N, M = map(int, sys.stdin.readline().split())
input_list = list(map(int, sys.stdin.readline().split()))

combination_list = list(combinations(input_list, 3))
sum_list = list(set(map(sum, combination_list)))

sorted_list = sorted(sum_list, reverse=True)

for element in sorted_list:
    if element <= M:
        result = element
        break

print(result)



