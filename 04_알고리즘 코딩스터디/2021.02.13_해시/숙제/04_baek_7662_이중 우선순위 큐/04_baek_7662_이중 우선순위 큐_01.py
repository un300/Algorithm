

# I n  > n 삽입
# D 1  > 최댓값 삭제
# D -1 > 최솟값 삭제



############# 시간초과
from collections import deque


class Solution_class:    
    def __init__(self) :
        self.Q = deque([])

    def dual_priority_queue(self, way, n):
        if way == 'I' :
            self.Q.append(n)
            self.Q = deque(sorted(self.Q))

        elif (n==1) & (len(self.Q)>0) :
            self.Q.pop()

        elif (n==-1) & (len(self.Q)>0):
            self.Q.popleft()
            



def solution():
    T = int(input())
    for _ in range(T) :
        k = int(input())
        instance = Solution_class()
        for _ in range(k) :
            way, n = input().split()
            n = int(n)
            instance.dual_priority_queue(way, n)

        if instance.Q :
            max_value = instance.Q.pop()
            min_value = instance.Q.popleft()

            print('{} {}' .format(max_value, min_value))
        else :
            print('EMPTY')


solution()