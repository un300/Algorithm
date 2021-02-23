
import sys
from collections import deque


def BFS(array, node, destination) :
    queue = deque([(node[0], node[1])])
    direction = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]

    array[node[0]][node[1]] = 1

    while True :
        r, c = queue.popleft()

        if (r==destination[0]) & (c==destination[1]) :
            return array[r][c] - 1

        for dr, dc in direction :
            nr = r + dr
            nc = c + dc

            if (0<=nr<len(array)) & (0<=nc<len(array[0])) :
                if not array[nr][nc] :
                    array[nr][nc] = array[r][c] + 1
                    queue.append((nr, nc))
    



def solution() :
    fast_input = sys.stdin.readline
    # 테스트 케이스 수 입력
    T = int(fast_input().rstrip())

    for _ in range(T) :
        # 체스판 한변 길이 입력
        I = int(fast_input().rstrip())
        array = [ [False]*I for _ in range(I) ]

        # 현재위치 입력
        current_location = list(map(int, fast_input().rstrip().split())) 
        
        # 목적지 입력
        destination = list(map(int, fast_input().rstrip().split()))
        answer = BFS(array, current_location, destination)
        print(answer)

solution()