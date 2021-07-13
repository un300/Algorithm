'''
1: 익은 토마토
0: 익지않은 토마토
-1: 토마토가 없는 칸
'''
from collections import deque


def BFS():
    m, n, h = map(int, input().split())

    box = []
    for _ in range(h):
        layer = [list(map(int, input().split())) for _ in range(n)]
        box.append(layer)

    rape_location = deque([])  # 토마토 익은 위치
    for i in range(m):
        for j in range(n):
            for k in range(h):
                if box[k][j][i] == 1:
                    rape_location.append((i, j, k))

    direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    
    day = 0
    while rape_location:
        iter_cnt = len(rape_location)
        for _ in range(iter_cnt):
            i, j, k = rape_location.popleft()
            for di, dj, dk in direction:
                ni = i + di
                nj = j + dj
                nk = k + dk

                if (0 <= ni < m) & (0 <= nj < n) & (0 <= nk < h):
                    if box[nk][nj][ni] == 0:
                        box[nk][nj][ni] = 1
                        rape_location.append((ni, nj, nk))
        day += 1
            

    for layer in box:
        for array in layer:
            for element in array:
                if not element:
                    return -1
    return day - 1
    


print(BFS())
