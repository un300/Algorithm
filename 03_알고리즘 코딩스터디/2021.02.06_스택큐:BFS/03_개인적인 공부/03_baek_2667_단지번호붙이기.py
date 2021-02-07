### 1. DFS구현

def DFS(row, col, array, visited):
    if (row<0) | (col<0) | (row>N-1) | (col>N-1):
        return False
    elif array[row][col] == 0:
        visited[row][col] = True
        return False
    elif visited[row][col] :
        return False
    else :
        global cnt
        cnt += 1
        visited[row][col] = True

        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dx, dy in direction:
            next_row = row + dx
            next_col = col + dy
            DFS(next_row, next_col, array, visited)
        


### 2. 입력
N = int(input())
array = []
visited = []
for _ in range(N):
    input_list = list(map(int, list(input())))
    array.append(input_list)
    visited.append([False] * N)


### 3. 문제해결
def solution():
    answer = []
    for row in range(N):
        for col in range(N):
            global cnt
            cnt = 0
            DFS(row, col, array, visited)
            if cnt != 0:
                answer.append(cnt)

    answer = sorted(answer)
    print(len(answer))
    for element in answer:
        print(element)

solution()