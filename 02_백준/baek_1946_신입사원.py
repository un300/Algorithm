


import sys

def solution() :
    fast_input = sys.stdin.readline
    T = int(fast_input())
    for _ in range(T) :
        N = int(fast_input())
        record = []
        cnt = 0

        for _ in range(N) :
            x, y = map(int, fast_input().rstrip().split())
            record.append((x, y))
        record.sort(key=lambda x : x[0])
    
        min_rank = N+1

        for _, rank in record :
            if min_rank > rank :
                min_rank = rank
                cnt += 1
        print(cnt)
        
solution()