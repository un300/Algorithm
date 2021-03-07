

from collections import deque

def solution() :
    N = int(input())

    queue = deque(list(range(1, N+1)))

    while len(queue)!=1 :
        top = queue.popleft()
        next_top = queue.popleft()
        queue.append(next_top)
    print(queue.popleft())

solution()