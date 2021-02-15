## 미로찾기
## 개수를 세지말고
## 지금 자리까지 몇번의 셀을 거쳐왔는지
## 행렬에 기록하는 아이디어




from collections import deque

def BFS(row, col, array, visited):
    queue = deque([(row, col)])
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue :
        row, col = queue.popleft()
        visited[row][col] = True

        for dr, dc in direction :
            new_row = row + dr
            new_col = col + dc

            if (new_row>=0) & (new_col>=0) & (new_row<=len(array)-1) & (new_col<=len(array[0])-1):
                if (not visited[new_row][new_col]) & (array[new_row][new_col]==1) :

                    array[new_row][new_col] = array[row][col] + 1
                    queue.append((new_row, new_col))

    r = len(array)-1
    c = len(array[0])-1
    print(array[r][c])






def solution():

    row, col = map(int, input().split())
    array = []
    for _ in range(row):
        input_list = list(map(int, list(input())))
        array.append(input_list)
    visited = [[False]*col for _ in range(row)]
    BFS(0, 0, array, visited)


solution()