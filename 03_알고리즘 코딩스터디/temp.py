

import bisect
from collections import deque


a = deque([2])
b = [3, 4]

bisect.insort(a, 1)
bisect.insort(b, 1)
print(a)
print(b)
