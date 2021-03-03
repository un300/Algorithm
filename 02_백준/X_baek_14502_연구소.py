import sys
import copy
from collections import deque


def BFS(map_, N, M, location) :
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque(location)
    
    while queue :
        row, col = queue.popleft()
        map_[row][col] = 2
        print(map_)

        for dr, dc in direction :
            nr = row + dr
            nc = col + dc

            if (0<=nr<N) & (0<=nc<M) :
                if map_[nr][nc] == 0 :
                    queue.append((nr, nc))



## 벽세우는게 어렵다 ㅠㅠ
def set_wall(map_, N, M, wall_cnt) :
    global big_cnt
    if wall_cnt == 3 :
        virus_location = []
        copy_map_ = copy.deepcopy(map_)
        for row in range(N) :
            for col in range(M) :
                if copy_map_[row][col] == 2:
                    virus_location.append((row, col))
        
        BFS(copy_map_, N, M, virus_location)
                    

        temp_cnt = 0
        for element_list in copy_map_ :
            for element in element_list :
                if element == 0 :
                    temp_cnt += 1

        big_cnt = max(temp_cnt, big_cnt)

        return True


    for row in range(N) :
        for col in range(M) :
            if map_[row][col] == 0 :
                map_[row][col] = 1
                set_wall(map_, N, M, wall_cnt+1)
                map_[row][col] = 0



def solution() :
    fast_input = sys.stdin.readline
    N, M = map(int, fast_input().split())
    map_ = [ list(map(int, fast_input().split())) for _ in range(N) ]

    global big_cnt
    big_cnt = 0
    set_wall(map_, N, M, 0)

    return big_cnt




print(solution())


## python / pypy3 시간초과
