## 내일 다시풀자


N = int(input())


array = []
visited = []
for _ in range(N):
    input_list = list(map(int, list(input())))
    array.append(input_list)
    visited.append([False] * N)


direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def DFS(row, col, array, visited, direction):
    visited[row][col] = True
    for row_plus, col_plus in direction :
        row += row_plus
        col += col_plus

        if (row<0) | (col<0) | (row>N-1) | (col>N-1):
                break
        elif (array[row][col] == 1) & (not visited[row][col]) :
            cnt += 1
            DFS(row, col, array, visited, direction)



answer_list = []
for row in range(N):
    for col in range(N):
        if array[row][col] == 0 :
            visited[row][col] = True
        else:
            DFS(row, col, array, visited, direction)

print(answer_list)