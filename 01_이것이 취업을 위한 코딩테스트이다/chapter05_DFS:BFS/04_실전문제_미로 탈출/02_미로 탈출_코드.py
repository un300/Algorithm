def BFS(maze, visited_maze, N, M) :
    row = 0
    col = 0

    visited_maze[row][col] = True
    route                  = [(row, col)]

    while True :
        change_location = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for row_change, col_change in change_location :
            row += row_change
            col += col_change
            if (row < 0) | (col < 0) | (row > N-1) | (col > M-1) :
                row -= row_change
                col -= col_change
                continue
            elif (maze[row][col] == 1) & (not visited_maze[row][col]) :
                route.append((row, col))
                visited_maze[row][col] = True
                break
            else :
                row -= row_change
                col -= col_change

        if (row == N-1) & (col == M-1) :
            break
    
    return len(route)


N, M = map(int, input().split())
maze = []
visited_maze = []
for _ in range(N) :
    input_list = list(map(int, input()))
    maze.append(input_list)
    visited_maze.append([False] * M)


print(BFS(maze, visited_maze, N, M))