

from collections import deque

def BFS(row, col, arr, visited, height, N) :
    queue = deque([(row, col)])
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue :
        current_row, current_col = queue.popleft()
        visited[current_row][current_col] = True
        for dr, dc in direction :
            nr = current_row + dr
            nc = current_col + dc
            if (0<=nr<N & (0<=nc<N) :
                if (not visited[nr][nc]) & (arr[nr][nc]>height) :
                    queue.append((nr, nc))
                    


def solution() :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_height = min(map(min, arr))
    max_height = max(map(max, arr))

    if min_height == max_height :
        return 1

    answer = 0
    for height in range(min_height, max_height) :
        visited = [[False]*N for _ in range(N)]
        cnt = 0
        for r in range(N) :
            for c in range(N) :
                if (arr[r][c] > height) & (not visited[r][c]) :
                    BFS(r, c, arr, visited, height, N)
                    cnt += 1

        if answer < cnt :
            answer = cnt
    
    print(answer)


solution()