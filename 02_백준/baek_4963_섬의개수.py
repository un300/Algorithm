import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)


def DFS(map_, location) :
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    row, col = location
    
    map_[row][col] = 0

    for dr, dc in direction :
        nr = row + dr
        nc = col + dc
        if (0<=nr<len(map_)) & (0<=nc<len(map_[0])) :
            if map_[nr][nc] == 1 :
                DFS(map_,(nr, nc))


def solution():
    w, h = map(int, input().split())
    while (w!=0) & (h!=0) :
        
        map_ = [ list(map(int, input().split())) for _ in range(h) ] 

        cnt = 0
        for row in range(h) :
            for col in range(w) :
                if map_[row][col] == 1 :
                    location = (row, col)
                    DFS(map_, location)
                    cnt += 1
        print(cnt)
        w, h = map(int, input().split())




solution()