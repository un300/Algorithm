import sys
from collections import Counter

x_list = []
y_list = []
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

x_dict = dict(map(reversed, Counter(x_list).items()))
y_dict = dict(map(reversed, Counter(y_list).items()))

print(x_dict[1], y_dict[1])


# python3로 품